import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

def string_to_float(data):
    return [float(value) for value in data]

# import data from csv file 
data = sp.genfromtxt("iris.csv", delimiter=",", dtype="|S15")
# Column 1: Sepal length
# Column 2: Sepal width
# Column 3: Petal length
# Column 4: Petal width
# Column 5: Iris type
sepal_length = string_to_float(data[:,0])
sepal_width = string_to_float(data[:,1])
petal_length = string_to_float(data[:,2])
petal_width = string_to_float(data[:,3])
iris_type = data[:,4]
marker_color = []
for variety in iris_type:
    if variety == "Iris-virginica":
        marker_color.append('r')
    if variety == "Iris-versicolor":
        marker_color.append('g')
    if variety == "Iris-setosa":
        marker_color.append('b')

plt.scatter(sepal_width, sepal_length, color=marker_color)

plt.title("Iris classification")
plt.xlabel("Sepal Width")
plt.ylabel("Sepal Length")

# print to screen
plt.autoscale(tight=True)
plt.grid()
plt.show()
