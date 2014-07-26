import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

def error(f, x, y):
    return sp.sum((f(x)-y)**2)

def add_model_to_chart(x, y, degree):
    # x values for plotting
    fx = sp.linspace(0, x[-1], 1000)
    # model (polynomial of degree...)
    fp = sp.polyfit(x, y, degree)
    f = sp.poly1d(fp)
    plt.plot(fx, f(fx), linewidth=3, label="d=%d" % degree)
    return f

# take data from csv file and add it to the chart
data = sp.genfromtxt("tsxclose.csv", delimiter=",")
x = np.array(range(1, data.shape[0]+1))
y = data[::-1, 1] # data is in reverse chronological order, so reverse again
plt.scatter(x, y)

# create models
inflection = 5500
xa = x[:inflection] # data before the inflection point
ya = y[:inflection]
xb = x[inflection:] # data after the inflection point
yb = y[inflection:]
add_model_to_chart(x, y, 1)
add_model_to_chart(xa, ya, 1)
add_model_to_chart(xb, yb, 1)

# make the chart pretty with labels, title and a legend
plt.title("TSX daily close from July 29, 1979 to July 21, 2014")
plt.xlabel("Day number")
plt.ylabel("Closing price")
plt.legend(loc="upper left")

# print to screen
plt.autoscale(tight=True)
plt.grid()
plt.show()
