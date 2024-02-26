from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score
import numpy as np
from matplotlib import pyplot as plt

fig, axs = plt.subplots(3,3, squeeze=True)

langs = ['english', 'tagalog', 'xhosa', 'middle-english', 'hiligaynon', 'plautdietsch']

for lang in langs:
    auc = []
    for i in range(1,10):
        english_scores = np.loadtxt(f'path/string_length_tests/test_scores_english_{i}.txt')
        scores = np.loadtxt(f'C:/path/string_length_tests/test_scores_{lang}_{i}.txt')
        labels = np.append(np.zeros(len(english_scores)), np.ones(len(scores)))
        data = np.append(english_scores, scores)

        auc += [roc_auc_score(labels, data)]
        if lang == 'tagalog':
            fpr, tpr, thresholds = roc_curve(labels, data)
            axs.flatten()[i-1].plot(fpr, tpr, c='k')
            axs.flatten()[i-1].plot([0,1],[0,1], 'k--')
            axs.flatten()[i-1].set_title(f'Min substring length = {i}')
    print(max(auc))
plt.show()
