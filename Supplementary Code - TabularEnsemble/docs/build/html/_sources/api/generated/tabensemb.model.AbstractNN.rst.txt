tabensemb.model.AbstractNN
==========================

.. currentmodule:: tabensemb.model

.. autoclass:: AbstractNN
   :show-inheritance:
   
   .. rubric:: Methods
   .. automethod:: __init__

   
   .. autosummary::
   
      ~AbstractNN.before_loss_fn
      ~AbstractNN.cal_backward_step
      ~AbstractNN.cal_zero_grad
      ~AbstractNN.call_required_model
      ~AbstractNN.configure_optimizers
      ~AbstractNN.forward
      ~AbstractNN.get_hidden_state
      ~AbstractNN.get_loss_fn
      ~AbstractNN.get_output_norm
      ~AbstractNN.loss_fn
      ~AbstractNN.output_norm
      ~AbstractNN.set_requires_grad
      ~AbstractNN.test_epoch
      ~AbstractNN.training_step
      ~AbstractNN.validation_step
   
      ~AbstractNN._early_stopping_eval
      ~AbstractNN._forward
      ~AbstractNN._test_required_model
   

   


   .. HACK -- the point here is that we don't want this to appear in the output, but the autosummary should still generate the pages.
      .. autosummary::
         :toctree:
      
         AbstractNN._DeviceDtypeModuleMixin__update_properties
         AbstractNN.__call__
         AbstractNN._apply
         AbstractNN._apply_batch_transfer_handler
         AbstractNN._call_batch_hook
         AbstractNN._call_impl
         AbstractNN._early_stopping_eval
         AbstractNN._forward
         AbstractNN._get_backward_hooks
         AbstractNN._get_name
         AbstractNN._load_from_state_dict
         AbstractNN._log_dict_through_fabric
         AbstractNN._maybe_warn_non_full_backward_hook
         AbstractNN._named_members
         AbstractNN._on_before_batch_transfer
         AbstractNN._prevent_trainer_and_dataloaders_deepcopy
         AbstractNN._register_load_state_dict_pre_hook
         AbstractNN._register_sharded_tensor_state_dict_hooks_if_available
         AbstractNN._register_state_dict_hook
         AbstractNN._replicate_for_data_parallel
         AbstractNN._save_to_state_dict
         AbstractNN._set_hparams
         AbstractNN._slow_forward
         AbstractNN._test_required_model
         AbstractNN._to_hparams_dict
         AbstractNN._verify_is_manual_optimization
         AbstractNN.add_module
         AbstractNN.all_gather
         AbstractNN.apply
         AbstractNN.backward
         AbstractNN.before_loss_fn
         AbstractNN.bfloat16
         AbstractNN.buffers
         AbstractNN.cal_backward_step
         AbstractNN.cal_zero_grad
         AbstractNN.call_required_model
         AbstractNN.children
         AbstractNN.clip_gradients
         AbstractNN.configure_callbacks
         AbstractNN.configure_gradient_clipping
         AbstractNN.configure_optimizers
         AbstractNN.configure_sharded_model
         AbstractNN.cpu
         AbstractNN.cuda
         AbstractNN.double
         AbstractNN.eval
         AbstractNN.extra_repr
         AbstractNN.float
         AbstractNN.forward
         AbstractNN.freeze
         AbstractNN.from_compiled
         AbstractNN.get_buffer
         AbstractNN.get_extra_state
         AbstractNN.get_hidden_state
         AbstractNN.get_loss_fn
         AbstractNN.get_output_norm
         AbstractNN.get_parameter
         AbstractNN.get_submodule
         AbstractNN.half
         AbstractNN.ipu
         AbstractNN.load_from_checkpoint
         AbstractNN.load_state_dict
         AbstractNN.log
         AbstractNN.log_dict
         AbstractNN.log_grad_norm
         AbstractNN.loss_fn
         AbstractNN.lr_scheduler_step
         AbstractNN.lr_schedulers
         AbstractNN.manual_backward
         AbstractNN.modules
         AbstractNN.named_buffers
         AbstractNN.named_children
         AbstractNN.named_modules
         AbstractNN.named_parameters
         AbstractNN.on_after_backward
         AbstractNN.on_after_batch_transfer
         AbstractNN.on_before_backward
         AbstractNN.on_before_batch_transfer
         AbstractNN.on_before_optimizer_step
         AbstractNN.on_before_zero_grad
         AbstractNN.on_fit_end
         AbstractNN.on_fit_start
         AbstractNN.on_load_checkpoint
         AbstractNN.on_predict_batch_end
         AbstractNN.on_predict_batch_start
         AbstractNN.on_predict_end
         AbstractNN.on_predict_epoch_end
         AbstractNN.on_predict_epoch_start
         AbstractNN.on_predict_model_eval
         AbstractNN.on_predict_start
         AbstractNN.on_save_checkpoint
         AbstractNN.on_test_batch_end
         AbstractNN.on_test_batch_start
         AbstractNN.on_test_end
         AbstractNN.on_test_epoch_end
         AbstractNN.on_test_epoch_start
         AbstractNN.on_test_model_eval
         AbstractNN.on_test_model_train
         AbstractNN.on_test_start
         AbstractNN.on_train_batch_end
         AbstractNN.on_train_batch_start
         AbstractNN.on_train_end
         AbstractNN.on_train_epoch_end
         AbstractNN.on_train_epoch_start
         AbstractNN.on_train_start
         AbstractNN.on_validation_batch_end
         AbstractNN.on_validation_batch_start
         AbstractNN.on_validation_end
         AbstractNN.on_validation_epoch_end
         AbstractNN.on_validation_epoch_start
         AbstractNN.on_validation_model_eval
         AbstractNN.on_validation_model_train
         AbstractNN.on_validation_start
         AbstractNN.optimizer_step
         AbstractNN.optimizer_zero_grad
         AbstractNN.optimizers
         AbstractNN.output_norm
         AbstractNN.parameters
         AbstractNN.predict_dataloader
         AbstractNN.predict_step
         AbstractNN.prepare_data
         AbstractNN.print
         AbstractNN.register_backward_hook
         AbstractNN.register_buffer
         AbstractNN.register_forward_hook
         AbstractNN.register_forward_pre_hook
         AbstractNN.register_full_backward_hook
         AbstractNN.register_load_state_dict_post_hook
         AbstractNN.register_module
         AbstractNN.register_parameter
         AbstractNN.requires_grad_
         AbstractNN.save_hyperparameters
         AbstractNN.set_extra_state
         AbstractNN.set_requires_grad
         AbstractNN.setup
         AbstractNN.share_memory
         AbstractNN.state_dict
         AbstractNN.tbptt_split_batch
         AbstractNN.teardown
         AbstractNN.test_dataloader
         AbstractNN.test_epoch
         AbstractNN.test_epoch_end
         AbstractNN.test_step
         AbstractNN.test_step_end
         AbstractNN.to
         AbstractNN.to_empty
         AbstractNN.to_onnx
         AbstractNN.to_torchscript
         AbstractNN.to_uncompiled
         AbstractNN.toggle_optimizer
         AbstractNN.train
         AbstractNN.train_dataloader
         AbstractNN.training_epoch_end
         AbstractNN.training_step
         AbstractNN.training_step_end
         AbstractNN.transfer_batch_to_device
         AbstractNN.type
         AbstractNN.unfreeze
         AbstractNN.untoggle_optimizer
         AbstractNN.val_dataloader
         AbstractNN.validation_epoch_end
         AbstractNN.validation_step
         AbstractNN.validation_step_end
         AbstractNN.xpu
         AbstractNN.zero_grad



   .. HACK -- the point here is that we don't want this to appear in the output, but the autosummary should still generate the pages.
      .. autosummary::
         :toctree:
      
         AbstractNN.CHECKPOINT_HYPER_PARAMS_KEY
         AbstractNN.CHECKPOINT_HYPER_PARAMS_NAME
         AbstractNN.CHECKPOINT_HYPER_PARAMS_TYPE
         AbstractNN.T_destination
         AbstractNN._jit_is_scripting
         AbstractNN._version
         AbstractNN.automatic_optimization
         AbstractNN.current_epoch
         AbstractNN.device
         AbstractNN.dump_patches
         AbstractNN.example_input_array
         AbstractNN.fabric
         AbstractNN.global_rank
         AbstractNN.global_step
         AbstractNN.hparams
         AbstractNN.hparams_initial
         AbstractNN.local_rank
         AbstractNN.logger
         AbstractNN.loggers
         AbstractNN.on_gpu
         AbstractNN.truncated_bptt_steps
         AbstractNN.training
         AbstractNN._parameters
         AbstractNN._buffers
         AbstractNN._non_persistent_buffers_set
         AbstractNN._backward_hooks
         AbstractNN._is_full_backward_hook
         AbstractNN._forward_hooks
         AbstractNN._forward_pre_hooks
         AbstractNN._state_dict_hooks
         AbstractNN._load_state_dict_pre_hooks
         AbstractNN._load_state_dict_post_hooks
         AbstractNN._modules
