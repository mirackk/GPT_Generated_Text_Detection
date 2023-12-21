import matplotlib.pyplot as plt

models = ['GRU', 'LSTM']
training_times = [82.47, 123.34]

plt.bar(models, training_times, color=['blue', 'green'])

plt.title('Training Time Comparison')
plt.xlabel('Model')
plt.ylabel('Training Time (seconds per epoch)')

plt.show()
