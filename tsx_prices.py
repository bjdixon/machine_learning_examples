import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

data = sp.genfromtxt("tsxclose.csv", delimiter=",")
x = np.array(range(1, data.shape[0]+1))
y = data[::-1, 1]
plt.scatter(x, y)
plt.title("TSX daily close from July 29, 1979 to July 21, 2014")
plt.xlabel("Day number")
plt.ylabel("Closing price")
plt.autoscale(tight=True)
plt.grid()
plt.show()

