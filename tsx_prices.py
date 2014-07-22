import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

# get data from csv file
data = sp.genfromtxt("tsxclose.csv", delimiter=",")
x = np.array(range(1, data.shape[0]+1))
y = data[::-1, 1] # data is in reverse chronological order, so reverse again
plt.scatter(x, y)

# add labels
plt.title("TSX daily close from July 29, 1979 to July 21, 2014")
plt.xlabel("Day number")
plt.ylabel("Closing price")

# fit straight line
fp1, residuals, rank, sv, rcond = sp.polyfit(x, y, 1, full=True)
f1 = sp.poly1d(fp1)
fx = sp.linspace(0, x[-1], 1000)
plt.plot(fx, f1(fx), linewidth=4)

# print to screen
plt.autoscale(tight=True)
plt.grid()
plt.show()

