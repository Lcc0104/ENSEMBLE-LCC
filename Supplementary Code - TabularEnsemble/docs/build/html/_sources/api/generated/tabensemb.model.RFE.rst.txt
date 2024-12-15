tabensemb.model.RFE
===================

.. currentmodule:: tabensemb.model

.. autoclass:: RFE
   :show-inheritance:
   
   .. rubric:: Methods
   .. automethod:: __init__

   
   .. autosummary::
   
      ~RFE.run
   
      ~RFE._get_model_names
      ~RFE._get_program_name
      ~RFE._new_model
      ~RFE._predict
      ~RFE._predict_all
      ~RFE._train
   

   


   .. HACK -- the point here is that we don't want this to appear in the output, but the autosummary should still generate the pages.
      .. autosummary::
         :toctree:
      
         RFE._bayes_eval
         RFE._check_params
         RFE._check_space
         RFE._check_train_status
         RFE._conditional_validity
         RFE._custom_training_params
         RFE._data_preprocess
         RFE._default_metric_sklearn
         RFE._generate_dataset
         RFE._generate_dataset_for_required_models
         RFE._generate_dataset_from_tensors
         RFE._get_model_names
         RFE._get_params
         RFE._get_program_name
         RFE._get_required_models
         RFE._initial_values
         RFE._mkdir
         RFE._new_model
         RFE._pred_single_model
         RFE._predict
         RFE._predict_all
         RFE._predict_model
         RFE._predict_model_on_partition
         RFE._prepare_custom_datamodule
         RFE._prepare_tensors
         RFE._run_custom_data_module
         RFE._space
         RFE._train
         RFE._train_data_preprocess
         RFE._train_single_model
         RFE._update_optimizer_lr_scheduler_params
         RFE.cal_feature_importance
         RFE.cal_shap
         RFE.count_params
         RFE.detach_model
         RFE.fit
         RFE.get_full_name_from_required_model
         RFE.get_model_names
         RFE.inspect_attr
         RFE.new_model
         RFE.predict
         RFE.predict_proba
         RFE.required_models
         RFE.reset
         RFE.run
         RFE.save_kwargs
         RFE.set_path
         RFE.train



   .. HACK -- the point here is that we don't want this to appear in the output, but the autosummary should still generate the pages.
      .. autosummary::
         :toctree:
      
         RFE._support_warm_start
         RFE._trained
         RFE.device
