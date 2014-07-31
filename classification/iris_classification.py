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

# plot charts
plt.subplot(231)
plt.scatter(sepal_length, petal_length, color=marker_color)
plt.xlabel("Sepal length")
plt.ylabel("Petal length")

plt.subplot(232)
plt.scatter(sepal_length, petal_width, color=marker_color)
plt.xlabel("Sepal length")
plt.ylabel("Petal width")

plt.subplot(233)
plt.scatter(sepal_width, petal_length, color=marker_color)
plt.xlabel("Sepal width")
plt.ylabel("Petal length")

plt.subplot(234)
plt.scatter(sepal_width, petal_width, color=marker_color)
plt.xlabel("Sepal width")
plt.ylabel("Petal width")

plt.subplot(235)
plt.scatter(petal_length, petal_width, color=marker_color)
plt.xlabel("Petal length")
plt.ylabel("Petal width")

plt.subplot(236)
plt.scatter(sepal_length, sepal_width, color=marker_color)
plt.xlabel("Sepal length")
plt.ylabel("Sepal width")

# print to screen
plt.autoscale(tight=True)
plt.show()

# We can separate Setosa based on petal length. 
# So get the petal length range for Setosa
max_setosa = max([iris[0] for iris in zip(petal_length, iris_type) if iris[1] == "Iris-setosa"])
min_non_setosa = min([iris[0] for iris in zip(petal_length, iris_type) if iris[1] != "Iris-setosa"])
print(max_setosa)
print(min_non_setosa)

# First classification model
# min_non_setosa (3.0) is greater than max_setosa (1.9), so if petal length
# is less than 2 it is from Setosa
for record in petal_length:
    if record < 2:
        print("Iris Setosa")
    else:
        print("Iris Virginica or Iris Versicolour")

