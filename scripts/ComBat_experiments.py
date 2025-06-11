import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from joblib import Parallel, delayed
from sklearn.dummy import DummyClassifier
from sklearn.metrics import classification_report
from sklearn.metrics.pairwise import pairwise_kernels
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, KernelCenterer
from sklearn.svm import SVC

from .evaluation_classifier import Evaluater
from .pycombat import Combat


def plot_ComBat_experiment_results(y_label, dummy_results, svm_results, svm_combat_results, metric_labels, save_dir,
                                   y_chance=0.5, multiclass=False):
    if multiclass:
        metrics_of_interest = ['accuracy', 'weigh_avg_precision', 'weigh_avg_recall', 'weigh_avg_f1_score']
        y_min, y_max = 0.0, 1.0
    else:
        metrics_of_interest = ['AUC', 'balanced_accuracy', 'sensitivity', 'specificity']
        y_min, y_max = 0.3, 1.0

    aggr_results_df = pd.DataFrame([], columns=metric_labels)
    for label, result in [('Dummy', dummy_results),
                        ('SVM', svm_results),
                        ('SVM+ComBat', svm_combat_results)]:
        tmp_df = pd.DataFrame(index=[label], columns=metric_labels, data=[result.mean(axis=0)])
        aggr_results_df = pd.concat([aggr_results_df, tmp_df])

        # Plot results
    plt.style.use('seaborn-dark')

    ax = aggr_results_df.loc[:, metrics_of_interest].plot(kind='bar')
    fig = ax.get_figure()
    fig.set_size_inches(6, 3.5)

    ax.axhline(y=y_chance, color='r', linestyle='--', alpha=0.5)

    ax.set_ylim(y_min, y_max)
    ax.set_title(y_label)
    plt.xticks(rotation=0)

    # Save figure
    save_path = os.path.join(save_dir, 'results_' + y_label + '_clf.png')
    plt.savefig(save_path, dpi=300)
    plt.close()
