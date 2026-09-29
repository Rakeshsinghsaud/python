#frozenset is an immutable version of a set.
#syntax:frozenset()
a=frozenset({2,3,4,5,6})
b=frozenset({6,7,9,9,23})
print(a)
print(b)
print(a.difference(b))
print(a.intersection(b))
