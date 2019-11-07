def clean_diag(diag):
	return [x for x in diag if not float('inf') in x[1]]

def main():
	import persistence
	import matplotlib.pyplot as plt
	try:
		import gudhi
	except:
		print('gudhi package not installed')
		return

	# definir la filtration : on a un triangle vide et un triangle plein qui partagent une arete
	st = gudhi.SimplexTree()
	n_pts = 5
	time  = 0.0
	for n in range(n_pts):
		st.insert([n], time)
		time += 1.0
	for n in range(n_pts - 1, 0, -1):
		st.insert([0, n], time)
		time += 1.0
	diag = st.persistence(persistence_dim_max=True)
	gudhi.plot_persistence_diagram(diag)
	plt.show()
	diag2 = clean_diag(diag)
	landscape = persistence.persistence_landscape(diag2)
	persistence.plot_persistence_landscape(landscape)
	plt.show()

if __name__ == '__main__':
	main()