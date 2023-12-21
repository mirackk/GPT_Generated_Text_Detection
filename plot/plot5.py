import matplotlib.pyplot as plt

models = ['GRU', 'LSTM']
inference_times = [5, 12]  # in milliseconds

plt.bar(models, inference_times, color=['blue', 'green'])

plt.title('Inference Time Comparison')
plt.xlabel('Model')
plt.ylabel('Inference Time (milliseconds per step)')

plt.show()
