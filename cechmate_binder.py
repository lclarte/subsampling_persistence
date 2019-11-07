# filtrations.py
# permet de calculer les filtrations ainsi que leurs diagrammes de persistence 
# contient les fonctions qui sont specifiques a cechmate

import cechmate as cm
import numpy    as np

def compute_filtration(x, method, **kwargs):
	"""
	utilise la librairie cechmate 
	"""
	if method == 'rips':
		r = cm.filtrations.Rips(**kwargs)
	elif method == 'cech':
		r = cm.filtrations.Cech(**kwargs)
	elif method == 'alpha':
		r = cm.filtrations.Alpha(**kwargs)
	else:
		print('Invalid method')
		return None
	return r

def compute_persistence(X, filtration):
	simplices = filtration.build(X)
	diagrams  = filtration.diagrams(simplices, show_inf=False)
	return simplices, diagrams
