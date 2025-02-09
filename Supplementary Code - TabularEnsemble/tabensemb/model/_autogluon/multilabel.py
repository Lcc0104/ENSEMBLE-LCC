# Modified version of https://auto.gluon.ai/stable/tutorials/tabular/advanced/tabular-multilabel.html
from autogluon.tabular import TabularDataset, TabularPredictor
from autogluon.common.utils.utils import setup_outputdir


class MultilabelPredictor:
    """Tabular Predictor for predicting multiple columns in table.
    Creates multiple TabularPredictor objects which you can also use individually.
    You can access the TabularPredictor for a particular label via: `multilabel_predictor.get_predictor(label_i)`

    Parameters
    ----------
    labels : List[str]
        The ith element of this list is the column (i.e. `label`) predicted by the ith TabularPredictor stored in this object.
    path : str, default = None
        Path to directory where models and intermediate outputs should be saved.
        If unspecified, a time-stamped folder called "AutogluonModels/ag-[TIMESTAMP]" will be created in the working directory to store all models.
        Note: To call `fit()` twice and save all results of each fit, you must specify different `path` locations or don't specify `path` at all.
        Otherwise files from first `fit()` will be overwritten by second `fit()`.
        Caution: when predicting many labels, this directory may grow large as it needs to store many TabularPredictors.
    problem_types : List[str], default = None
        The ith element is the `problem_type` for the ith TabularPredictor stored in this object.
    eval_metrics : List[str], default = None
        The ith element is the `eval_metric` for the ith TabularPredictor stored in this object.
    consider_labels_correlation : bool, default = True
        Whether the predictions of multiple labels should account for label correlations or predict each label independently of the others.
        If True, the ordering of `labels` may affect resulting accuracy as each label is predicted conditional on the previous labels appearing earlier in this list (i.e. in an auto-regressive fashion).
        Set to False if during inference you may want to individually use just the ith TabularPredictor without predicting all the other labels.
    kwargs :
        Arguments passed into the initialization of each TabularPredictor.

    """

    multi_predictor_file = "multilabel_predictor.pkl"

    def __init__(
        self,
        labels,
        path=None,
        problem_types=None,
        eval_metrics=None,
        consider_labels_correlation=True,
        **kwargs,
    ):
        if len(labels) < 2:
            raise ValueError(
                "MultilabelPredictor is only intended for predicting MULTIPLE labels (columns), use TabularPredictor for predicting one label (column)."
            )
        if (problem_types is not None) and (len(problem_types) != len(labels)):
            raise ValueError(
                "If provided, `problem_types` must have same length as `labels`"
            )
        if (eval_metrics is not None) and (len(eval_metrics) != len(labels)):
            raise ValueError(
                "If provided, `eval_metrics` must have same length as `labels`"
            )
        self.path = setup_outputdir(path, warn_if_exist=False)
        self.labels = labels
        self.consider_labels_correlation = consider_labels_correlation
        self.predictors = (
            {}
        )  # key = label, value = TabularPredictor or str path to the TabularPredictor for this label
        if eval_metrics is None:
            self.eval_metrics = {}
        else:
            self.eval_metrics = {labels[i]: eval_metrics[i] for i in range(len(labels))}
        problem_type = None
        eval_metric = None
        for i in range(len(labels)):
            label = labels[i]
            path_i = self.path + "Predictor_" + label
            if problem_types is not None:
                problem_type = problem_types[i]
            if eval_metrics is not None:
                eval_metric = eval_metrics[i]
            self.predictors[label] = TabularPredictor(
                label=label,
                problem_type=problem_type,
                eval_metric=eval_metric,
                path=path_i,
                **kwargs,
            )

    def fit(self, train_data, tuning_data=None, **kwargs):
        """Fits a separate TabularPredictor to predict each of the labels.

        Parameters
        ----------
        train_data, tuning_data : str or autogluon.tabular.TabularDataset or pd.DataFrame
            See documentation for `TabularPredictor.fit()`.
        kwargs :
            Arguments passed into the `fit()` call for each TabularPredictor.
        """
        if isinstance(train_data, str):
            train_data = TabularDataset(train_data)
        if tuning_data is not None and isinstance(tuning_data, str):
            tuning_data = TabularDataset(tuning_data)
        train_data_og = train_data.copy()
        if tuning_data is not None:
            tuning_data_og = tuning_data.copy()
        else:
            tuning_data_og = None
        save_metrics = len(self.eval_metrics) == 0
        for i in range(len(self.labels)):
            label = self.labels[i]
            predictor = self.get_predictor(label)
            if not self.consider_labels_correlation:
                labels_to_drop = [l for l in self.labels if l != label]
            else:
                labels_to_drop = [
                    self.labels[j] for j in range(i + 1, len(self.labels))
                ]
            train_data = train_data_og.drop(labels_to_drop, axis=1)
            if tuning_data is not None:
                tuning_data = tuning_data_og.drop(labels_to_drop, axis=1)
            print(f"Fitting TabularPredictor for label: {label} ...")
            predictor.fit(train_data=train_data, tuning_data=tuning_data, **kwargs)
            self.predictors[label] = predictor
            if save_metrics:
                self.eval_metrics[label] = predictor.eval_metric

    def predict(self, data, **kwargs):
        """Returns DataFrame with label columns containing predictions for each label.

        Parameters
        ----------
        data : str or autogluon.tabular.TabularDataset or pd.DataFrame
            Data to make predictions for. If label columns are present in this data, they will be ignored. See documentation for `TabularPredictor.predict()`.
        kwargs :
            Arguments passed into the predict() call for each TabularPredictor.
        """
        return self._predict(data, as_proba=False, **kwargs)

    def predict_proba(self, data, **kwargs):
        """Returns dict where each key is a label and the corresponding value is the `predict_proba()` output for just that label.

        Parameters
        ----------
        data : str or autogluon.tabular.TabularDataset or pd.DataFrame
            Data to make predictions for. See documentation for `TabularPredictor.predict()` and `TabularPredictor.predict_proba()`.
        kwargs :
            Arguments passed into the `predict_proba()` call for each TabularPredictor (also passed into a `predict()` call).
        """
        return self._predict(data, as_proba=True, **kwargs)

    def evaluate(self, data, **kwargs):
        """Returns dict where each key is a label and the corresponding value is the `evaluate()` output for just that label.

        Parameters
        ----------
        data : str or autogluon.tabular.TabularDataset or pd.DataFrame
            Data to evalate predictions of all labels for, must contain all labels as columns. See documentation for `TabularPredictor.evaluate()`.
        kwargs :
            Arguments passed into the `evaluate()` call for each TabularPredictor (also passed into the `predict()` call).
        """
        data = self._get_data(data)
        eval_dict = {}
        for label in self.labels:
            print(f"Evaluating TabularPredictor for label: {label} ...")
            predictor = self.get_predictor(label)
            eval_dict[label] = predictor.evaluate(data, **kwargs)
            if self.consider_labels_correlation:
                data[label] = predictor.predict(data, **kwargs)
        return eval_dict

    def get_predictor(self, label):
        """Returns TabularPredictor which is used to predict this label."""
        predictor = self.predictors[label]
        return predictor

    def _get_data(self, data):
        if isinstance(data, str):
            return TabularDataset(data)
        return data.copy()

    def _predict(self, data, as_proba=False, **kwargs):
        data = self._get_data(data)
        if as_proba:
            predproba_dict = {}
        for label in self.labels:
            print(f"Predicting with TabularPredictor for label: {label} ...")
            predictor = self.get_predictor(label)
            if as_proba:
                predproba_dict[label] = predictor.predict_proba(
                    data, as_multiclass=True, **kwargs
                )
            data[label] = predictor.predict(data, **kwargs)
        if not as_proba:
            return data[self.labels]
        else:
            return predproba_dict

    def persist_models(self, *args, **kwargs):
        for predictor in self.predictors.values():
            try:
                predictor.persist_models(*args, **kwargs)
            except:
                predictor.persist(*args, **kwargs)
