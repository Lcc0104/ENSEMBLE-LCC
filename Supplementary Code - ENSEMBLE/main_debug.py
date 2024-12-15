import faulthandler

faulthandler.enable()

import tabensemb
import numpy as np
import torch
from tabensemb.trainer import load_trainer, save_trainer
from src.trainer import FatigueTrainer
from tabensemb.trainer.utils import NoBayesOpt
from tabensemb.model import *

# from src.model.thiswork_as_input import ThisWorkAsInput
from src.model.thiswork_layup import ThisWorkLayup
from src.model import *
from tabensemb.utils import Logging, add_postfix
import os


import tabensemb

# tabensemb.setting["debug_mode"] = True

# trainer = load_trainer(
#     path="output/composite_database_07242023_5mat/2023-08-17-23-21-41-0_composite_5mat Cycle 316/trainer.pkl"
# )
# trainer.get_modelbase("ThisWork").plot_uncertain_dl_weight(
#     trainer.get_modelbase("ThisWork").inspect_weighted_predictions(
#         "WideDeep_TabResnet_NoWrap_1L_PCA_KMeans"
#     )
# )
# trainer.get_modelbase("ThisWork").plot_phy_weights(
#     "AutoGluon_Random Forest_NoWrap_1L_NoPCA_KMeans",
#     save_to=os.path.join(
#         trainer.get_modelbase("ThisWork").root,
#         "AutoGluon_Random Forest_NoWrap_1L_NoPCA_KMeans_phy_weights.jpg",
#     ),
# )
# df_cluster = trainer.get_modelbase("ThisWork").df_with_cluster(
#     "WideDeep_TabResnet_NoWrap_1L_PCA_KMeans",
#     save_to=os.path.join(trainer.project_root, "df_with_cluster.csv"),
# )
# improved_measure, ttest_res = trainer.get_modelbase("ThisWork").improvement(
#     trainer.leaderboard, cv_path=os.path.join(trainer.project_root, "cv")
# )
# improved_measure.to_csv(os.path.join(trainer.project_root, "improvement.csv"))
# method_ranking, detailed = trainer.get_modelbase("ThisWork").method_ranking(
#     improved_measure, trainer.leaderboard
# )
# method_ranking.to_csv(os.path.join(trainer.project_root, "method_ranking.csv"))
# trainer.get_modelbase("ThisWork").plot_method_ranking(
#     detailed, save_to=os.path.join(trainer.project_root, "method_ranking.jpg")
# )
# trainer.get_modelbase("ThisWork").plot_improvement(
#     trainer.leaderboard,
#     improved_measure,
#     ttest_res,
#     metric="Testing RMSE",
#     save_to=os.path.join(trainer.project_root, "improvement.jpg"),
# )
# trainer.plot_multiple_S_N(
#     m_codes=[
#         "MD-DD5P-UP2[0/±45/0]S",
#         "MD-P2B[±45/(90)4C]S",
#         "MD-QQ1-EP2-S[(±45)/(0)2]S",
#         "MD-QQ1-EP2-S[(±45)/(90)2]S",
#         "Triax-AA-UP2[(±45/0)3/(0/±45)2]",
#     ],
#     s_col="Maximum Stress",
#     n_col="log10(Cycles to Failure)",
#     r_col="R-value",
#     # avg_feature=["Width", "Length", "Maximum Strain", "Minimum Strain", "Frequency"],
#     # f_col="Frequency",
#     # freq=2,
#     n_bootstrap=1,
#     r_value=0.1,
#     load_dir="tension",
#     verbose=True,
#     program="ThisWork",
#     model_name="SNCatEmbedLR2LPCAKMeans",
#     refit=False,
#     resample=False,
# )
log = Logging()

device = "cuda" if torch.cuda.is_available() else "cpu"

configfile = "composite"
trainer = FatigueTrainer(device=device, project="test")
trainer.load_config(
    configfile,
    manual_config={
        # "database": "composite_database_10082023",
        "data_splitter": "StressCycleSplitter",
        "split_ratio": [0.6, 0.2, 0.2],
        "bayes_opt": False,
        # "epoch": 1000,
        # "bayes_epoch": 10,
        # "bayes_calls": 12,
        # "batch_size": 128,
        # "patience": 10000,
    },
)
log.enter(os.path.join(trainer.project_root, "log.txt"))
trainer.summarize_setting()
trainer.load_data()

# pof50 = trainer.cal_theoretical_pof50(distribution="weibull")
# trainer.datamodule.set_feature_names(["Maximum Stress", "Relative Maximum Stress"])
# trainer.load_data()
# trainer.load_data()
# trainer.plot_data_split()
# trainer.set_data_splitter("RandomSplitter")
# trainer.load_data()
# trainer.plot_data_split()
# trainer.set_data_splitter("MaterialSplitter")
# trainer.load_data()
# trainer.plot_data_split()
# trainer.set_data_splitter("MaterialCycleSplitter")
# trainer.load_data()
# trainer.plot_data_split()
models = [
    PytorchTabular(trainer, model_subset=["Category Embedding"]),
    # AutoGluon(trainer),
    # CatEmbed(trainer),
    # WideDeep(trainer),
    # ThisWork(
    #     trainer,
    #     pca=False,
    #     clustering="KMeans",
    #     clustering_layer="3L",
    #     uncertainty="mcd",
    #     classifier_use_raw=True,
    # ),
    # ThisWorkLayup(trainer, model_subset=["TransformerLayup"])
    # ThisWork(
    #     trainer,
    #     clustering="KMeans",
    #     clustering_layer="2L",
    #     program="ThisWork_KMeans_2L",
    # ),
    # ThisWork(
    #     trainer, clustering="GMM", clustering_layer="1L", program="ThisWork_GMM_1L"
    # ),
    # ThisWork(
    #     trainer, clustering="BMM", clustering_layer="1L", program="ThisWork_BMM_1L"
    # ),
    # ThisWork(
    #     trainer,
    #     clustering="KMeans",
    #     clustering_layer="2L",
    #     program="ThisWork_KMeans_2L",
    # ),
    # ThisWork(
    #     trainer,
    #     clustering="KMeans",
    #     clustering_layer="3L",
    #     pca=False,
    #     program="ThisWork_KMeans_3L",
    #     uncertainty=None,
    # ),
    # ThisWork(
    #     trainer,
    #     clustering="KMeans",
    #     clustering_layer="3L",
    #     pca=False,
    #     program="ThisWork_KMeans_3L_mcd",
    #     uncertainty="mcd",
    # ),
    # ThisWork(
    #     trainer, clustering="GMM", clustering_layer="2L", program="ThisWork_GMM_2L"
    # ),
    # ThisWork(
    #     trainer, clustering="BMM", clustering_layer="2L", program="ThisWork_BMM_2L"
    # ),
    # ThisWork(
    #     trainer,
    #     clustering="KMeans",
    #     clustering_layer="1L",
    #     program="ThisWork_KMeans_1L_PCA",
    #     pca=True,
    # ),
    # ThisWork(
    #     trainer,
    #     clustering="GMM",
    #     clustering_layer="1L",
    #     program="ThisWork_GMM_1L_PCA",
    #     pca=True,
    # ),
    # ThisWork(
    #     trainer,
    #     clustering="BMM",
    #     clustering_layer="1L",
    #     program="ThisWork_BMM_1L_PCA",
    #     pca=True,
    # ),
    # ThisWork(
    #     trainer,
    #     clustering="KMeans",
    #     clustering_layer="2L",
    #     program="ThisWork_KMeans_2L_PCA",
    #     pca=True,
    # ),
    # ThisWork(
    #     trainer,
    #     clustering="GMM",
    #     clustering_layer="2L",
    #     program="ThisWork_GMM_2L_PCA",
    #     pca=True,
    # ),
    # ThisWork(
    #     trainer,
    #     clustering="BMM",
    #     clustering_layer="2L",
    #     program="ThisWork_BMM_2L_PCA",
    #     pca=True,
    # ),
]
# #
trainer.add_modelbases(models)
# trainer.bayes_opt = True
# trainer.plot_corr(fontsize=5, imputed=False)

# tabensemb._stream_filters = ["DeprecationWarning"]
trainer.train()
# trainer.get_leaderboard()
# trainer.get_leaderboard(cross_validation=1, split_type="random")
# trainer.datamodule.get_not_imputed_df()

# trainer.plot_loss(
#     program="PytorchTabular",
#     model_name="Category Embedding",
#     restored_epoch_mark_if_last=True,
# )
# trainer.plot_loss(
#     program="CatEmbed",
#     model_name="Category Embedding",
#     restored_epoch_mark_if_last=False,
# )
# trainer.plot_loss(
#     program="WideDeep", model_name="TabResnet", restored_epoch_mark_if_last=False
# )

# trainer.plot_fill_rating()
# trainer.plot_pca_2d_visual(category="Resin Type")
# from tabensemb.utils.utils import global_palette
#
# ax = trainer.plot_on_one_axes(
#     meth_name="plot_scatter",
#     meth_kwargs_ls=[
#         dict(
#             select_by_value_kwargs={
#                 "selection": {"Material_Code": "MD-P2B[±45/(90)4C]S"}
#             },
#             scatter_kwargs={
#                 "color": global_palette[0],
#                 "s": 5,
#                 "marker": "s",
#                 "label": "MD-P2B[±45/(90)4C]S",
#             },
#         ),
#         dict(
#             select_by_value_kwargs={
#                 "selection": {"Material_Code": "MD-DD5P-UP2[0/±45/0]S"}
#             },
#             scatter_kwargs={
#                 "color": global_palette[1],
#                 "s": 5,
#                 "marker": "v",
#                 "label": "MD-DD5P-UP2[0/±45/0]S",
#             },
#         ),
#         dict(
#             select_by_value_kwargs={
#                 "selection": {"Material_Code": "MD-QQ1-EP2-S[(±45)/(90)2]S"}
#             },
#             scatter_kwargs={
#                 "color": global_palette[2],
#                 "s": 5,
#                 "marker": "^",
#                 "label": "MD-QQ1-EP2-S[(±45)/(90)2]S",
#             },
#         ),
#         dict(
#             select_by_value_kwargs={
#                 "selection": {"Material_Code": "MD-QQ1-EP2-S[(±45)/(0)2]S"}
#             },
#             scatter_kwargs={
#                 "color": global_palette[3],
#                 "s": 5,
#                 "marker": "<",
#                 "label": "MD-QQ1-EP2-S[(±45)/(0)2]S",
#             },
#         ),
#         dict(
#             select_by_value_kwargs={
#                 "selection": {"Material_Code": "Triax-AA-UP2[(±45/0)3/(0/±45)2]"}
#             },
#             scatter_kwargs={
#                 "color": global_palette[4],
#                 "s": 5,
#                 "marker": ">",
#                 "label": "Triax-AA-UP2[(±45/0)3/(0/±45)2]",
#             },
#         ),
#     ],
#     meth_fix_kwargs=dict(
#         x_col="log10(Cycles to Failure)",
#         y_col="Maximum Stress",
#         imputed=False,
#     ),
#     save_show_close=False,
#     xlabel="log10(Cycles to Failure)",
#     ylabel="Maximum Stress",
# )
#
# import matplotlib.pyplot as plt
#
# ax.legend()
#
# plt.sca(ax)
# plt.savefig(os.path.join(trainer.project_root, "SN_5mat.pdf"))
# plt.close()
#
# trainer.plot_on_one_axes(
#     meth_name=["plot_hist", "plot_pdf", "plot_kde"],
#     meth_kwargs_ls=[
#         dict(
#             feature="Maximum Stress",
#             select_by_value_kwargs={
#                 "selection": {"Material_Code": "MD-P2B[±45/(90)4C]S"}
#             },
#             hist_kwargs={"color": "k", "alpha": 0.2, "label": "hist"},
#             imputed=False,
#         ),
#         dict(
#             feature="Maximum Stress",
#             imputed=False,
#             select_by_value_kwargs={
#                 "selection": {"Material_Code": "MD-P2B[±45/(90)4C]S"}
#             },
#             plot_kwargs={"color": global_palette[0], "label": "pdf"},
#         ),
#         dict(
#             feature="Maximum Stress",
#             imputed=False,
#             select_by_value_kwargs={
#                 "selection": {"Material_Code": "MD-P2B[±45/(90)4C]S"}
#             },
#             kdeplot_kwargs={"color": global_palette[1], "label": "kde"},
#         ),
#     ],
#     legend=True,
# )
# trainer.plot_pdf(
#     feature="Maximum Stress",
#     select_by_value_kwargs={"selection": {"Material_Code": "MD-P2B[±45/(90)4C]S"}},
#     imputed=False,
# )
# trainer.plot_hist(feature="Maximum Stress")
# trainer.plot_corr(imputed=False)
# trainer.plot_corr(imputed=True)
# trainer.plot_truth_pred_all(program="PytorchTabular")
# trainer.plot_truth_pred(program="PytorchTabular", model_name="Category Embedding")
# trainer.plot_presence_ratio(order="type")
# trainer.plot_partial_dependence_all(
#     program="PytorchTabular", model_name="Category Embedding", refit=False, grid_size=5
# )
# trainer.plot_partial_dependence(
#     program="PytorchTabular",
#     model_name="Category Embedding",
#     feature="Maximum Stress",
#     refit=False,
#     grid_size=5,
# )
# trainer.plot_feature_importance(
#     program="PytorchTabular", model_name="Category Embedding", method="permutation"
# )
# trainer.plot_feature_importance(
#     program="PytorchTabular", model_name="Category Embedding", method="shap"
# )
# trainer.plot_feature_importance(
#     program="CatEmbed", model_name="Category Embedding", method="permutation"
# )
# trainer.plot_feature_importance(
#     program="CatEmbed", model_name="Category Embedding", method="shap"
# )
# trainer.plot_partial_err_all(program="PytorchTabular", model_name="Category Embedding")
# trainer.plot_partial_err(
#     program="PytorchTabular", model_name="Category Embedding", feature="Maximum Stress"
# )
# trainer.plot_pairplot()
# trainer.plot_feature_box(imputed=True)
# trainer.plot_feature_box(imputed=False)
# trainer.plot_hist_all(imputed=False)
# trainer.plot_hist_all(imputed=True)
# trainer.plot_hist(feature="Maximum Stress", imputed=True)
#

# trainer.plot_partial_dependence(
#     program="PytorchTabular", model_name="Category Embedding", refit=False, grid_size=5
# )
# res = models[0].predict(trainer.df, model_name="SNCatEmbedLRPCAKMeans")
# trainer.get_leaderboard(cross_validation=10, split_type="random")
# mean, std = trainer.get_approx_cv_leaderboard(trainer.leaderboard)
# tmp_trainer = trainer.detach_modelbase(program="ThisWork")

# trainer.plot_S_N(
#     m_code="Carbon prepreg[0]2",
#     s_col="Maximum Stress",
#     n_col="log10(Cycles to Failure)",
#     r_col="R-value",
#     # avg_feature=["Width", "Length", "Maximum Strain", "Minimum Strain", "Frequency"],
#     f_col="Frequency",
#     freq=10,
#     n_bootstrap=1,
#     r_value=0.1,
#     load_dir="tension",
#     verbose=True,
#     program="PytorchTabular",
#     model_name="Category Embedding",
#     refit=False,
#     resample=False,
#     log_stress=True,
# )

# trainer.plot_multiple_S_N(
#     m_codes=[
#         "MD-DD5P-UP2[0/±45/0]S",
#         "MD-P2B[±45/(90)4C]S",
#         "MD-QQ1-EP2-S[(±45)/(0)2]S",
#         "MD-QQ1-EP2-S[(±45)/(90)2]S",
#         "Triax-AA-UP2[(±45/0)3/(0/±45)2]",
#     ],
#     s_col="Maximum Stress",
#     n_col="log10(Cycles to Failure)",
#     r_col="R-value",
#     # avg_feature=["Width", "Length", "Maximum Strain", "Minimum Strain", "Frequency"],
#     # f_col="Frequency",
#     # freq=2,
#     n_bootstrap=1,
#     r_value=0.1,
#     load_dir="tension",
#     verbose=True,
#     program="ThisWork",
#     model_name="SNCategoryEmbedLR2LPCAKMeans",
#     refit=False,
#     resample=False,
# )

log.exit()
# trainer.cal_shap(program="AutoGluon", model_name="Random Forest")
# trainer.train(verbose=True)
# trainer.plot_feature_importance(
#     program="MLP", method="shap"
# )
# trainer.plot_feature_importance(program="MLP", model_name="MLP", method="permutation")
# trainer.plot_feature_importance(program="MLP", model_name="MLP", method="shap")
# trainer.plot_feature_importance(
#     program="TabNet", model_name="TabNet", method="permutation"
# )
# trainer.plot_feature_importance(program="TabNet", model_name="TabNet", method="shap")
# trainer.plot_partial_err(program="TabNet", model_name="TabNet")
# trainer.plot_partial_err(program="MLP", model_name="MLP")
# trainer.plot_partial_dependence(
#     program="MLP",
#     model_name="MLP",
#     n_bootstrap=1,
#     refit=False,
#     upper_lim=6,
#     lower_lim=3,
# )
# trainer.plot_partial_dependence(
#     program="TabNet",
#     model_name="TabNet",
#     n_bootstrap=2,
#     refit=False,
#     upper_lim=6,
#     lower_lim=3,
# )
# models[0].trainer.plot_corr(fontsize=10, imputed=False)
# trainer.cal_feature_importance(program="MLP", model_name="MLP", method="shap")
# trainer.cal_feature_importance(program="TabNet", model_name="TabNet", method="shap")
# leaderboard = trainer.get_leaderboard(test_data_only=False, cross_validation=0)

# importance = trainer.cal_feature_importance(
#     program="MLP", model_name="MLP", method="shap"
# )
# importance = trainer.cal_feature_importance(
#     program="MLP", model_name="MLP", method="permutation"
# )
# trainer.plot_partial_err(program="MLP", model_name="MLP")
# trainer.plot_feature_importance(program="MLP", model_name="MLP")

# trainer.plot_feature_importance(program="MLP", fig_size=(6, 6))
# trainer.plot_partial_dependence(
#     program="MLP",
#     model_name="MLP",
#     n_bootstrap=2,
#     refit=False,
#     upper_lim=6,
#     lower_lim=3,
# )
# leaderboard = trainer.get_leaderboard(
#     test_data_only=True, cross_validation=1, verbose=True
# )
# print(leaderboard)

# trainer.plot_S_N(
#     m_code=m_code,
#     s_col="Maximum Stress",
#     n_col="log10(Cycles to Failure)",
#     r_col="R-value",
#     n_bootstrap=10,
#     r_value=0.1,
#     load_dir="tension",
#     verbose=False,
#     program="MLP",
#     model_name="MLP",
#     refit=False,
# )
# trainer.plot_S_N(
#     m_code=m_code,
#     s_col="Maximum Stress",
#     n_col="log10(Cycles to Failure)",
#     r_col="R-value",
#     n_bootstrap=10,
#     r_value=0.1,
#     load_dir="tension",
#     verbose=False,
#     program=leaderboard["Program"][0]
#     if leaderboard["Program"][0] != "MLP"
#     else leaderboard["Program"][1],
#     refit=False,
# )
