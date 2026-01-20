import pandas as pd
import matplotlib.pyplot as plt

# Read CSV data
data = pd.read_csv("data.csv")

# Create plot
plt.plot(data.iloc[:, 0], data.iloc[:, 1])
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Simple Data Plot")
plt.grid(True)

# Save output
output_name = "output_plot.png"
plt.savefig(output_name)
plt.show()

print(f"Plot saved as {output_name}")
