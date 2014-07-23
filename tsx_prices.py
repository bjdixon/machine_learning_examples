import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

def error(f, x, y):
    return sp.sum((f(x)-y)**2)

# get data from csv file
data = sp.genfromtxt("tsxclose.csv", delimiter=",")
x = np.array(range(1, data.shape[0]+1))
y = data[::-1, 1] # data is in reverse chronological order, so reverse again
plt.scatter(x, y)

# add labels
plt.title("TSX daily close from July 29, 1979 to July 21, 2014")
plt.xlabel("Day number")
plt.ylabel("Closing price")

# x values for plotting
fx = sp.linspace(0, x[-1], 1000)

# fit straight line - first trained model
fp1, residuals, rank, sv, rcond = sp.polyfit(x, y, 1, full=True)
f1 = sp.poly1d(fp1)
plt.plot(fx, f1(fx), linewidth=4)
# print out error value - difference from the model to the actual values
print("Model 1 error: %d" % error(f1, x, y))

# fit another model - polynomial of degree 2
fp2 = sp.polyfit(x, y, 2)
f2 = sp.poly1d(fp2)
plt.plot(fx, f2(fx), linewidth=4)
print("Model 2 error: %d" % error(f2, x, y))

# model 3 - degree 3
fp3 = sp.polyfit(x, y, 3)
f3 = sp.poly1d(fp3)
plt.plot(fx, f3(fx), linewidth=4)
print("Model 3 error: %d" % error(f3, x, y))

# model 10 - degree 10 (overfitting)
fp10 = sp.polyfit(x, y, 10)
f10 = sp.poly1d(fp10)
plt.plot(fx, f10(fx), linewidth=4)
print("Model 10 error: %d" % error(f10, x, y))

# model 30 - degree 30 (overfitting)
fp30 = sp.polyfit(x, y, 30)
f30 = sp.poly1d(fp30)
plt.plot(fx, f30(fx), linewidth=4)
print("Model 30 error: %d" % error(f30, x, y))

# print to screen
plt.autoscale(tight=True)
plt.grid()
plt.show()


