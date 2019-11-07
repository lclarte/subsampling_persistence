# test_subsampling_persistence.py
# script pour tester la fonction subsampling_persistence_landscape : 
# on genere des points de données, on prend un echantillon et on calcule le diagramme de persistence 


from persistence import *

def main():
	import gudhi as gd
	import cechmate as cm
	import numpy as np
	import matplotlib.pyplot as plt

	import data

	X, Y = data.two_circles(250, 250)
	points = np.array([X, Y]).transpose()
	plt.scatter(X, Y) ; plt.title('data used : 10 points per class') ; plt.show()
	# uniform distribution
	mu = lambda x : 1
	# take all samples from X
	n = 20
	landscape = subsampling_persistence_landscape(points, mu, n, 'rips', maxdim=2)
	plot_persistence_landscape([landscape[0]])
	plt.show()

if __name__ == '__main__':
	main()