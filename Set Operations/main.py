# Set Union
print("Set Union")
set1 = {1, 2, 3, 4, 5}
set2 = {8, 9, 10}
print(f"{set1} and {set2}")
union = set1.union(set2)
print(union)
print("")

# Set Intersection
print("Set Intersection")
set1 = {1, 2, 3, 4, 5}
set2 = {2,3,5}
print(f"{set1} and {set2}")
intersection = set1.intersection(set2)
print(intersection)
print("")

# Set Difference
print("Set Difference")
set1 = {1, 2, 3, 4, 5}
set2 = {2,3,5}
print(f"{set1} and {set2}")
difference = set1.difference(set2)
print(difference)
print("")

# Set Symmetric Difference
print("Set Symmetric Difference")
set1 = {1, 2, 3, 4, 5}
set2 = {2,3,5}
print(f"{set1} and {set2}")
sym_difference = set1.symmetric_difference(set2)
print(sym_difference)
print("")



