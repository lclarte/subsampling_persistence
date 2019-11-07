# sampling.py 

import numpy as np

def uniform_density(n):
	return np.array([1./n]*n)


def get_samples_from_vector(X, mu, n):
	"""
	Prend en argument un ensemble X, une distribution et renvoie un nombre n de samples
	"""
	indexes = list(range(len(X)))
	sampling = np.random.choice(indexes, p=mu, size=n, replace=False)
	return X[sampling]

def get_samples_from_density(X, mu, n):
	"""
	Prend en argument X, une fonction de densite mu et n samples
	"""
	probas = np.array([ mu(x) for x in X ], dtype=float)
	if np.amax(probas) == 0:
		return None 
	probas /= np.linalg.norm(probas, ord=1)
	return get_samples(X, probas, n)

def get_samples(X, mu, n):
	"""
	permet d'echantilloner indifferemnt de la distribution mu
	"""
	if callable(mu):
		return get_samples_from_density(X, mu, n)
	# case 2 : mu is discrete proba vector
	elif type(mu) in [list, np.ndarray]:
		return get_samples_from_vector(X, mu, n)
	else:
		print('Invalid probability')
		return None 
