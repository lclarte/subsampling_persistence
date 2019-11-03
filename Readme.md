#### Résumé 

Ceci est un repository contenant des expérimentations autour de l'article suivant : http://proceedings.mlr.press/v37/chazal15.pdf . 
Article pour le calcul du persistence landscape : https://hal.inria.fr/hal-01258875/file/PersistenceLandscapes_arxiv_v3.pdf

#### EXPERIMENTATIONS

Remarque   : experimentations faites sans calculer la persistence de tout l'ensemble de point (on peut faire ça sur des exemples pas trop compliqués)

Remarque 2 : Essayer de faire les expériences avec d'autres types de filtrations (lower star filtration par exemple)
	+ à faire : trouver le bon dataset (ex : relief de régions par exemple )

#### TODO 

1 ) Module pour subsampler un ensemble de points par rapport à une distribution
   i.e : (X, mu, N) -> (x_1, ... , x_N) qui suit la distribution mu 
   1.1 ) Fonction qui convertit une distribution de proba sur un espace (R^d) en une distribution sur 
   		 l'ensemble de points X c R^d : tel que la proba de x \in X soit proportionnelle à la proba de sa position dans R^d
   1.2 ) Fonction qui prend en argument un ensemble fini, une distrib. sur cet ensemble et renvoie 

2 ) Fonctions pour calculer la distance de Gromov-Hausdorff entre deux ensembles

3 ) Fonction pour calculer la distance de Wasserstein entre deux distributions

