import matplotlib.pyplot as plt

models = ['GRU', 'LSTM']

accuracy = [93.5, 94.5]

plt.bar(models, accuracy, color=['blue', 'green'])

plt.title('Accuracy Comparison')
plt.xlabel('Model')
plt.ylabel('Accuracy (%)')
plt.legend(['Accuracy'])

plt.show()
