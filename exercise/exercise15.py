#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 25 17:28:25 2019

@author: francesco
"""

"""
### Exercise 15

Given the 2-dimensional points in "pca_data.csv", apply PCA and project the points in 1 dimension according to the eigenvector with largest eigenvalue. Plot the projected points in 1 dimension (to plot them, set the second dimension equal to 0), project them back to 2 dimensions using the orthogonal eigenvectors found the first time through PCA and plot such projected points again.

Then repeat the same process from the original points, but projecting the points according to the eigenvectors but without changing number of dimensions. Plot the projected points, project them back using the same orthogonal eigenvectors and plot the projected points.

Which differences do you see in the plots?

TIP:
* when projecting back from 1 dimension to 2 dimensions, you should obtain a plot similar to the following:

![image.png](attachment:image.png)

ADDITIONAL MATERIAL:
* For a refresh on linear algebra: http://vmls-book.stanford.edu/vmls.pdf
* For a geometrical interpretation of the covariance matrix: http://www.visiondummy.com/2014/04/geometric-interpretation-covariance-matrix/
* About other types of linear projections: https://en.wikipedia.org/wiki/Linear_map#Examples_of_linear_transformation_matrices
"""



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# read data
path = "pca_data.csv"
df = pd.read_csv(path)

# extract only input dimensions from data
A = df.iloc[:,0:2].values

# standardize data (subtract mean and divide by standard deviation of columns)
M = np.mean(A.T, axis=1)
S = np.std(A.T, axis=1) 
N = (A - M)/S

# compute covariance matrix of data (must be dXd, where d = original dimension)
V = np.cov(N.T)

# compute eigendecomposition of covariance matrix (must obtain d eigenvectors)
eig_vals, eig_vecs = np.linalg.eig(V)

# sort eigenvalues and eigenvectors according to eigenvalues
idx = np.argsort(eig_vals)[::-1] # find the indexes which sort the array (reverse)
eig_vecs = eig_vecs[:,idx]
eig_vals = eig_vals[idx]

# extract first two eigenvectors (transpose because eigenvectors are columns here)
projection_vectors = np.array([eig_vecs.T[0]])

# project standardized data (must obtain nX2, where n = number of data points)
P = np.dot(N, projection_vectors.T)

# plot projected data
for i,j in enumerate(P):    
    plt.plot(j, 1, 'o')
plt.title("pca k = 1")
plt.grid()
plt.show()

# plot 2
projection_vectors = np.array([eig_vecs.T[0], eig_vecs[1]])
P = np.dot(N, projection_vectors.T)
plt.title("pca k = 2")
plt.scatter(P[:,0], P[:,1])
plt.grid()
plt.show()

# plot 3
plt.scatter(A[:,0], A[:,1])
plt.title("original data")
plt.grid()
plt.show()
