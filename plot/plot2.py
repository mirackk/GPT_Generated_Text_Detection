import matplotlib.pyplot as plt

models = ['GRU', 'LSTM']
auc = [0.9840, 0.48705]

plt.bar(models, auc, color=['blue', 'green'])

plt.title('AUC Comparison')
plt.xlabel('Model')
plt.ylabel('AUC')

plt.show()
