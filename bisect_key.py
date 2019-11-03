# bisect_key.py 

# Overload de la fonction insort_left de bisect pour 
def insort_left(a, x, lo=0, hi=None, key= lambda x : x):
    """Insert item x in list a, and keep it sorted assuming a is sorted.
	Return the index at which it is inserted

    If x is already in a, insert it to the left of the leftmost x.

    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.
    """
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        # comparison of the two keys
        if key(a[mid]) < key(x): lo = mid+1
        else: hi = mid
    a.insert(lo, x)
    return lo
