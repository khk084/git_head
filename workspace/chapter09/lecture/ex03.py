import os

import pandas as pd
import matplotlib.pyplot as plt

print(os.getcwd())
iris = pd.read_csv('chapter09/data/iris.csv')
print(iris.info())
print(iris.head())

plt.scatter(iris['Sepal.Length'], iris['Petal.Length'])