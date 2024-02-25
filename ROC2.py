from sklearn.metrics import roc_curve, roc_auc_score
import numpy as np
from matplotlib import pyplot as plt


r_values = range(2, 7)

# subplot grid of 3x2 for the ROC curves
fig, axs = plt.subplots(2, 3, figsize=(15, 10)) 
axs = axs.flatten()  


for idx, r in enumerate(r_values):
    # load the scores for the current r
    score_0 = np.loadtxt(f'C:/Users/31613/OneDrive/Documenten/Artificial Intelligence/Semester 2/Natural Computing/Assignment 3/results_r2to6/average_results_0_r{r}.txt')
    score_1 = np.loadtxt(f'C:/Users/31613/OneDrive/Documenten/Artificial Intelligence/Semester 2/Natural Computing/Assignment 3/results_r2to6/average_results_1_r{r}.txt')
    
    # labling the scores
    labels = np.append(np.zeros(len(score_0)), np.ones(len(score_1)))
    
    data = np.append(score_0, score_1)
    
    auc = roc_auc_score(labels, data)
    print(f'AUC for r={r}: {auc}')
    
    # roc curve
    fpr, tpr, thresholds = roc_curve(labels, data)
    
    axs[idx].plot(fpr, tpr, label=f'ROC Curve (AUC = {auc:.2f})')
    axs[idx].plot([0, 1], [0, 1], 'k--')
    axs[idx].set_title(f'ROC Curve for r = {r}')
    axs[idx].set_xlabel('False Positive Rate')
    axs[idx].set_ylabel('True Positive Rate')
    axs[idx].legend(loc='lower right')

# remove the last subplot, since we only have 5 r values
if len(r_values) < 6:
    fig.delaxes(axs[-1])

plt.tight_layout()
plt.show()



