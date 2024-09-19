# Union:

set1 = {1,2,3}
set2 = {4,5,6,2}

my_set = set1.union(set2)
print(my_set)

set3 = {1,2,3,4,5}
set4 = {5,2,6,7,8,9}
my_ssat = set4.intersection(set3)
print(my_ssat)

my_set1=set1.difference(set2)
my_set2=set2.difference(set1)
print(f"my_set1 {my_set1}")
print(f"my_set2 {my_set2}")

set5 = {1,2,3,4,5,6}
set6 = {2,3,8}
subset = set6.issubset(set5)
print(subset)
