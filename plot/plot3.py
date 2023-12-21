import matplotlib.pyplot as plt

models = ['GRU', 'LSTM']
f1_scores = [0.9395, 0.94]

plt.bar(models, f1_scores, color=['blue', 'green'])

plt.title('F1 Score Comparison')
plt.xlabel('Model')
plt.ylabel('F1 Score')

plt.show()
