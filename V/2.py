import matplotlib.pyplot as plt 

x1 = [5, 10, 15, 60, 40, 21, 43, 110, 225]

y1 = [8, 54, 32, 43, 124, 981, 221, 543, 222]

#

x2 = [2, 4, 8, 16, 32, 64, 128, 256, 512]

y2 = [5, 134, 512, 564, 642, 667, 812, 4665, 10050]

plt.scatter(x1, y1, c="green", marker="s", linewidths=2, label="Dataset 1", edgecolor="black", s=100)

plt.scatter(x2, y2, c="red", marker="o", linewidths=2, edgecolor="black", label="Dataset 2", s=200)

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Scatter Plot with Multiple Datasets")

plt.show()