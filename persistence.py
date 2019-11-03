# persistence.py
# Fichier pour calculer la persistence + lanscape des samples

from bisect_key import insort_left

def persistence_landscape(diag):
	"""
	Ref : https://hal.inria.fr/hal-01258875/file/PersistenceLandscapes_arxiv_v3.pdf
	Prend en argument un diagramme de persistence et retourne la liste 
	(critical points, critical values)
	Input format : liste de k elements. Pour chaque 0 <= l <= k-1, contient une liste de (b, d)
	"""
	# sort by increasing birth and decreasing death
	ordering_key = lambda x : (x[0], -x[1])
	# get number of dimensions in persistence diagram
	K = len(diag)
	# L[k] will store crit points and values for persistence of dimension k
	L = [[] for _ in range(K)]
	unpacked = []
	for d in diag:
		unpacked += d
	unpacked.sort(key = ordering_key)
	k = 0
	while len(unpacked) > 0:
		(b, d) = unpacked.pop(0)
		L[k] += [(float('-inf'), 0), (b, 0), (float(b+d)/2, float(d-b)/2)]
		# pointer on elements of unpacked
		p = 0
		# erreur dans l'article : (0, float('inf'))
		while L[k][-1] != (float('inf'), 0):
			# check if d maximal (not strict) among remaining terms
			if len(unpacked) == 0 or d == max(f for (e, f) in unpacked[p:]):
				L[k] += [(d, 0), (float('inf'), 0)]
			else:
				p, (b_1, d_1) = next(x for x in enumerate(unpacked) if x[1][1] > d)
				# pop current element, p points then to next element
				unpacked.pop(p)
				if b_1 > d:
					L[k].append( (d, 0) ) 
				if b_1 >= d:
					L[k].append( (b_1, 0) )
				else:
					L[k].append( (float(b_1 + d)/2.0, float(d - b_1)/2.0) )
					p = unpacked.insort_left(unpacked, (b_1, d), lo=p, key=ordering_key) + 1
				L[k] += (float(b_1 + d_1)/2.0, float(d_1 - b_1)/2.0)
				(b, d) = (b_1, d_1)
		k += 1
	return L

