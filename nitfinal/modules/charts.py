import matplotlib.pyplot as plt
import os
def generate_chart(data,labels):
    os.makedirs("assets/charts",exist_ok=True)
    path="assets/charts/chart.png"
    plt.figure()
    plt.bar(labels, data)
    plt.title("Generated Chart")
    plt.savefig(path)
    plt.close()
    return path
