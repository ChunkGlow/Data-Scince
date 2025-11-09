import matplotlib.pyplot as plt

x = [5, 6, 7, 43, 117, 435, 6314, 2783, 1121]
y = [8, 54, 32, 43, 124, 981, 221, 543, 222]

plt.scatter(x, y, c="blue", marker="x")
plt.title(" Scatter Plot ")
plt.xlabel(" X-axis ")
plt.ylabel(" Y-axis ")

plt.show()

