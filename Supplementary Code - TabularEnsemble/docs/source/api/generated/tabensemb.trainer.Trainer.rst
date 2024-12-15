tabensemb.trainer.Trainer
=========================

.. currentmodule:: tabensemb.trainer

.. autoclass:: Trainer
   :show-inheritance:
   
   .. rubric:: Methods
   .. automethod:: __init__

   
   .. autosummary::
   
      ~Trainer.add_modelbases
      ~Trainer.cal_feature_importance
      ~Trainer.cal_partial_dependence
      ~Trainer.cal_partial_dependence_2way
      ~Trainer.cal_shap
      ~Trainer.clear_modelbase
      ~Trainer.copy
      ~Trainer.cross_validation
      ~Trainer.detach_model
      ~Trainer.detach_modelbase
      ~Trainer.get_approx_cv_leaderboard
      ~Trainer.get_best_model
      ~Trainer.get_leaderboard
      ~Trainer.get_modelbase
      ~Trainer.get_modelwise_cv_metrics
      ~Trainer.get_predict_leaderboard
      ~Trainer.load_config
      ~Trainer.load_data
      ~Trainer.load_state
      ~Trainer.plot_categorical_presence_ratio
      ~Trainer.plot_corr
      ~Trainer.plot_corr_with_label
      ~Trainer.plot_err_hist
      ~Trainer.plot_feature_box
      ~Trainer.plot_feature_importance
      ~Trainer.plot_fill_rating
      ~Trainer.plot_hist
      ~Trainer.plot_hist_all
      ~Trainer.plot_kde
      ~Trainer.plot_kde_all
      ~Trainer.plot_loss
      ~Trainer.plot_on_one_axes
      ~Trainer.plot_pairplot
      ~Trainer.plot_partial_dependence
      ~Trainer.plot_partial_dependence_2way
      ~Trainer.plot_partial_dependence_2way_all
      ~Trainer.plot_partial_dependence_all
      ~Trainer.plot_partial_err
      ~Trainer.plot_partial_err_all
      ~Trainer.plot_pca_2d_visual
      ~Trainer.plot_pdf
      ~Trainer.plot_presence_ratio
      ~Trainer.plot_scatter
      ~Trainer.plot_subplots
      ~Trainer.plot_truth_pred
      ~Trainer.plot_truth_pred_all
      ~Trainer.set_device
      ~Trainer.set_path
      ~Trainer.set_status
      ~Trainer.summarize_device
      ~Trainer.summarize_setting
      ~Trainer.train
   
      ~Trainer._bootstrap_fit
      ~Trainer._cal_leaderboard
      ~Trainer._create_dir
      ~Trainer._generate_grid
      ~Trainer._metrics
      ~Trainer._plot_action_after_plot
      ~Trainer._plot_action_categorical_scatter
      ~Trainer._plot_action_category_unique_values
      ~Trainer._plot_action_generate_feature_types_legends
      ~Trainer._plot_action_generate_feature_types_palette
      ~Trainer._plot_action_get_df
      ~Trainer._plot_action_init_ax
      ~Trainer._plot_action_subplots
      ~Trainer._read_cv_leaderboards
   

   


   .. HACK -- the point here is that we don't want this to appear in the output, but the autosummary should still generate the pages.
      .. autosummary::
         :toctree:
      
         Trainer._bootstrap_fit
         Trainer._cal_leaderboard
         Trainer._create_dir
         Trainer._generate_grid
         Trainer._metrics
         Trainer._plot_action_after_plot
         Trainer._plot_action_categorical_scatter
         Trainer._plot_action_category_unique_values
         Trainer._plot_action_generate_feature_types_legends
         Trainer._plot_action_generate_feature_types_palette
         Trainer._plot_action_get_df
         Trainer._plot_action_init_ax
         Trainer._plot_action_subplots
         Trainer._read_cv_leaderboards
         Trainer.add_modelbases
         Trainer.cal_feature_importance
         Trainer.cal_partial_dependence
         Trainer.cal_partial_dependence_2way
         Trainer.cal_shap
         Trainer.clear_modelbase
         Trainer.copy
         Trainer.cross_validation
         Trainer.detach_model
         Trainer.detach_modelbase
         Trainer.get_approx_cv_leaderboard
         Trainer.get_best_model
         Trainer.get_leaderboard
         Trainer.get_modelbase
         Trainer.get_modelwise_cv_metrics
         Trainer.get_predict_leaderboard
         Trainer.load_config
         Trainer.load_data
         Trainer.load_state
         Trainer.plot_categorical_presence_ratio
         Trainer.plot_corr
         Trainer.plot_corr_with_label
         Trainer.plot_err_hist
         Trainer.plot_feature_box
         Trainer.plot_feature_importance
         Trainer.plot_fill_rating
         Trainer.plot_hist
         Trainer.plot_hist_all
         Trainer.plot_kde
         Trainer.plot_kde_all
         Trainer.plot_loss
         Trainer.plot_on_one_axes
         Trainer.plot_pairplot
         Trainer.plot_partial_dependence
         Trainer.plot_partial_dependence_2way
         Trainer.plot_partial_dependence_2way_all
         Trainer.plot_partial_dependence_all
         Trainer.plot_partial_err
         Trainer.plot_partial_err_all
         Trainer.plot_pca_2d_visual
         Trainer.plot_pdf
         Trainer.plot_presence_ratio
         Trainer.plot_scatter
         Trainer.plot_subplots
         Trainer.plot_truth_pred
         Trainer.plot_truth_pred_all
         Trainer.set_device
         Trainer.set_path
         Trainer.set_status
         Trainer.summarize_device
         Trainer.summarize_setting
         Trainer.train



   .. HACK -- the point here is that we don't want this to appear in the output, but the autosummary should still generate the pages.
      .. autosummary::
         :toctree:
      
         Trainer.SPACE
         Trainer.all_feature_names
         Trainer.cat_feature_mapping
         Trainer.cat_feature_names
         Trainer.chosen_params
         Trainer.cont_feature_names
         Trainer.derived_data
         Trainer.derived_stacked_features
         Trainer.df
         Trainer.feature_data
         Trainer.label_data
         Trainer.label_name
         Trainer.static_params
         Trainer.tensors
         Trainer.test_indices
         Trainer.train_indices
         Trainer.training
         Trainer.unscaled_feature_data
         Trainer.unscaled_label_data
         Trainer.val_indices
