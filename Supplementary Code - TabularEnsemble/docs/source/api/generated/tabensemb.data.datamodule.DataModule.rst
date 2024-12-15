tabensemb.data.datamodule.DataModule
====================================

.. currentmodule:: tabensemb.data.datamodule

.. autoclass:: DataModule
   :show-inheritance:
   
   .. rubric:: Methods
   .. automethod:: __init__

   
   .. autosummary::
   
      ~DataModule.cal_corr
      ~DataModule.categories_inverse_transform
      ~DataModule.categories_transform
      ~DataModule.data_transform
      ~DataModule.dataset_dict
      ~DataModule.derive
      ~DataModule.derive_stacked
      ~DataModule.derive_unstacked
      ~DataModule.describe
      ~DataModule.divide_from_tabular_dataset
      ~DataModule.extract_derived_stacked_feature_names
      ~DataModule.extract_original_cat_feature_names
      ~DataModule.extract_original_cont_feature_names
      ~DataModule.feature_types_with_derived
      ~DataModule.generate_subset
      ~DataModule.generate_tensors
      ~DataModule.get_additional_tensors_slice
      ~DataModule.get_all_derived_stacked_feature_names
      ~DataModule.get_all_derived_unstacked_feature_names
      ~DataModule.get_base_predictor
      ~DataModule.get_categorical_ordinal_encoder
      ~DataModule.get_derived_data_sizes
      ~DataModule.get_derived_data_slice
      ~DataModule.get_df
      ~DataModule.get_feature_idx_by_type
      ~DataModule.get_feature_names_by_type
      ~DataModule.get_feature_types
      ~DataModule.get_feature_types_idx
      ~DataModule.get_first_tensor_slice
      ~DataModule.get_not_imputed_df
      ~DataModule.get_tabular_dataset
      ~DataModule.get_var_change
      ~DataModule.get_zero_slip
      ~DataModule.label_categories_inverse_transform
      ~DataModule.label_categories_transform
      ~DataModule.load_data
      ~DataModule.pca
      ~DataModule.prepare_new_data
      ~DataModule.save_data
      ~DataModule.select_by_value
      ~DataModule.set_data
      ~DataModule.set_data_derivers
      ~DataModule.set_data_imputer
      ~DataModule.set_data_processors
      ~DataModule.set_data_splitter
      ~DataModule.set_feature_names
      ~DataModule.set_status
      ~DataModule.sort_derived_data
      ~DataModule.unique_feature_types_with_derived
      ~DataModule.update_dataset
   
      ~DataModule._data_preprocess
      ~DataModule._data_process
      ~DataModule._get_gini
      ~DataModule._get_indices
      ~DataModule._get_kurtosis
      ~DataModule._get_mode
      ~DataModule._infer_loss
      ~DataModule._infer_task
   

   


   .. HACK -- the point here is that we don't want this to appear in the output, but the autosummary should still generate the pages.
      .. autosummary::
         :toctree:
      
         DataModule._data_preprocess
         DataModule._data_process
         DataModule._get_gini
         DataModule._get_indices
         DataModule._get_kurtosis
         DataModule._get_mode
         DataModule._infer_loss
         DataModule._infer_task
         DataModule.cal_corr
         DataModule.categories_inverse_transform
         DataModule.categories_transform
         DataModule.data_transform
         DataModule.dataset_dict
         DataModule.derive
         DataModule.derive_stacked
         DataModule.derive_unstacked
         DataModule.describe
         DataModule.divide_from_tabular_dataset
         DataModule.extract_derived_stacked_feature_names
         DataModule.extract_original_cat_feature_names
         DataModule.extract_original_cont_feature_names
         DataModule.feature_types_with_derived
         DataModule.generate_subset
         DataModule.generate_tensors
         DataModule.get_additional_tensors_slice
         DataModule.get_all_derived_stacked_feature_names
         DataModule.get_all_derived_unstacked_feature_names
         DataModule.get_base_predictor
         DataModule.get_categorical_ordinal_encoder
         DataModule.get_derived_data_sizes
         DataModule.get_derived_data_slice
         DataModule.get_df
         DataModule.get_feature_idx_by_type
         DataModule.get_feature_names_by_type
         DataModule.get_feature_types
         DataModule.get_feature_types_idx
         DataModule.get_first_tensor_slice
         DataModule.get_not_imputed_df
         DataModule.get_tabular_dataset
         DataModule.get_var_change
         DataModule.get_zero_slip
         DataModule.label_categories_inverse_transform
         DataModule.label_categories_transform
         DataModule.load_data
         DataModule.pca
         DataModule.prepare_new_data
         DataModule.save_data
         DataModule.select_by_value
         DataModule.set_data
         DataModule.set_data_derivers
         DataModule.set_data_imputer
         DataModule.set_data_processors
         DataModule.set_data_splitter
         DataModule.set_feature_names
         DataModule.set_status
         DataModule.sort_derived_data
         DataModule.unique_feature_types_with_derived
         DataModule.update_dataset



   .. HACK -- the point here is that we don't want this to appear in the output, but the autosummary should still generate the pages.
      .. autosummary::
         :toctree:
      
         DataModule.D_test
         DataModule.D_train
         DataModule.D_val
         DataModule.X_test
         DataModule.X_train
         DataModule.X_val
         DataModule.all_feature_names
         DataModule.cat_imputed_mask
         DataModule.cat_num_unique
         DataModule.categorical_data
         DataModule.cont_imputed_mask
         DataModule.derived_stacked_cat_features
         DataModule.derived_stacked_cont_features
         DataModule.derived_stacked_features
         DataModule.feature_data
         DataModule.label_data
         DataModule.unscaled_feature_data
         DataModule.unscaled_label_data
         DataModule.y_test
         DataModule.y_train
         DataModule.y_val
