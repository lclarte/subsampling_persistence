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
	st.insert([0], 0.0)
	st.insert([1], 1.0)
	st.insert([2], 2.0)
	st.insert([0, 1], 3.0)
	st.insert([0, 2], 4.0)
	st.insert([1, 2], 5.0)
	st.insert([3], 6.0)
	st.insert([1, 3], 7.0)
	st.insert([2, 3], 8.0)
	st.insert([1, 2, 3], 9.0)
	# 2 ) calculer son diagramme de persistence avec gudhi
	diag = st.persistence()
	gudhi.display_persistence_diagram(diag)
	# 3 ) calculer son landscape avec persistence.py
	landscape = persistence.persistence_landscape(diag)

if __name__ == '__main__':
	main()