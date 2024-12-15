tabensemb.model.TorchModel
==========================

.. currentmodule:: tabensemb.model

.. autoclass:: TorchModel
   :show-inheritance:
   
   .. rubric:: Methods
   .. automethod:: __init__

   
   .. autosummary::
   
      ~TorchModel.cal_feature_importance
      ~TorchModel.cal_shap
      ~TorchModel.count_params
      ~TorchModel.get_full_name_from_required_model
   
      ~TorchModel._data_preprocess
      ~TorchModel._generate_dataset
      ~TorchModel._generate_dataset_for_required_models
      ~TorchModel._generate_dataset_from_tensors
      ~TorchModel._initial_values
      ~TorchModel._pred_single_model
      ~TorchModel._prepare_custom_datamodule
      ~TorchModel._prepare_tensors
      ~TorchModel._run_custom_data_module
      ~TorchModel._space
      ~TorchModel._train_data_preprocess
      ~TorchModel._train_single_model
   

   


   .. HACK -- the point here is that we don't want this to appear in the output, but the autosummary should still generate the pages.
      .. autosummary::
         :toctree:
      
         TorchModel._bayes_eval
         TorchModel._check_params
         TorchModel._check_space
         TorchModel._check_train_status
         TorchModel._conditional_validity
         TorchModel._custom_training_params
         TorchModel._data_preprocess
         TorchModel._default_metric_sklearn
         TorchModel._generate_dataset
         TorchModel._generate_dataset_for_required_models
         TorchModel._generate_dataset_from_tensors
         TorchModel._get_model_names
         TorchModel._get_params
         TorchModel._get_program_name
         TorchModel._get_required_models
         TorchModel._initial_values
         TorchModel._mkdir
         TorchModel._new_model
         TorchModel._pred_single_model
         TorchModel._predict
         TorchModel._predict_all
         TorchModel._predict_model
         TorchModel._predict_model_on_partition
         TorchModel._prepare_custom_datamodule
         TorchModel._prepare_tensors
         TorchModel._run_custom_data_module
         TorchModel._space
         TorchModel._train
         TorchModel._train_data_preprocess
         TorchModel._train_single_model
         TorchModel._update_optimizer_lr_scheduler_params
         TorchModel.cal_feature_importance
         TorchModel.cal_shap
         TorchModel.count_params
         TorchModel.detach_model
         TorchModel.fit
         TorchModel.get_full_name_from_required_model
         TorchModel.get_model_names
         TorchModel.inspect_attr
         TorchModel.new_model
         TorchModel.predict
         TorchModel.predict_proba
         TorchModel.required_models
         TorchModel.reset
         TorchModel.save_kwargs
         TorchModel.set_path
         TorchModel.train



   .. HACK -- the point here is that we don't want this to appear in the output, but the autosummary should still generate the pages.
      .. autosummary::
         :toctree:
      
         TorchModel._support_warm_start
         TorchModel._trained
         TorchModel.device
