# Nested List
print("Nested List")
list1 = [["banana", "strawberry"], [18.5, True]]
print(list1)
print(f"Nested list: {list1}")
print("")

# Length
print("Length")
list1 = [["hi"], ["hello"], ["world"]]
print(list1)
print(len(list1))
print("")

# Concatenation
print("Concantation")
list1 = ["hello"]
list2 = ["hi"]
print(f"{list1} and {list2}")
print(list1 + list2)
print("")

# Membership
print("Membership")
list1 = [1, 2, 3, 4, 5]
list2 = [1, 3, 5]
print(f"{list1} and {list2}")
for item in list1:
    if item in list2:
        print("Overlapping")
    else:
        print("Not overlapping")
print("")

# Iteration
print("Iteration")
list1 = [1, 3, 5, 7, 9, 10]
print(list1)
for item in list1:
    print(item)
print("")

# Indexing
print("Indexing")
list1 = [1, 2, 3, 4, 6, 7, 8, 9]
print(list1)
print(list1[0])
print(list1[3])
print(list1[7])
print("")

# Slicing
print("Slicing")
list1 = [1, 3, 4, 5, 6, 7, 8, 9]
print(list1[:5])
print(list1[3:7])
print("")
