import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("data.csv")


plt.plot(data.iloc[:, 0], data.iloc[:, 1])
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Simple Data Plot")
plt.grid(True)


plt.savefig("plot.png")
plt.show()
