# data.py
# script pour générer les différents exemples 

import numpy as np
import matplotlib.pyplot as plt

def two_circles(m, n):
	"""
	Retourne des points repartis autour de deux cercles de diametre et centre differents 
	m et n sont les nombres de points respectifs des deux cercles 
	"""
	radius1, radius2 = 1.0, 0.5
	theta1, theta2 = np.random.uniform(low=0.0, high=2*np.pi, size=m), np.random.uniform(low=0.0, high=2*np.pi, size=n)
	# let's say that the two centers are on X axis 
	center1, center2 = 0.0, 1.6
	X1, Y1 = center1 + radius1*np.cos(theta1), radius1*np.sin(theta1)
	X2, Y2 = center2 + radius2*np.cos(theta2), radius2*np.sin(theta2)
	return np.concatenate((X1, X2)), np.concatenate((Y1, Y2))