from matplotlib import pyplot as plt
import numpy as np

a = np.array([1,4,9,16,25,36,49,64,81,100])

fig, ax = plt.subplots(figsize=(10, 7))
ax.hist(a, bins = [0, 25, 50, 75, 100], edgecolor='black')

plt.show()