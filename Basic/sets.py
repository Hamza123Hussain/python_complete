# Define two sets of numbers
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

# Display the two sets
print("Set A:", set_a)
print("Set B:", set_b)

# Add a new element to Set A
set_a.add(9)
print("Set A after adding 9:", set_a)

# Remove an element from Set B (will throw an error if the element doesn't exist)
set_b.remove(6)
print("Set B after removing 6:", set_b)

# Union of two sets (A ∪ B): Elements in either set
union_set = set_a.union(set_b)
print("Union of A and B:", union_set)

# Intersection of two sets (A ∩ B): Elements common to both sets
intersection_set = set_a.intersection(set_b)
print("Intersection of A and B:", intersection_set)

# Difference of two sets (A - B): Elements in A but not in B
difference_set = set_a.difference(set_b)
print("Difference of A and B (A - B):", difference_set)

# Symmetric Difference of two sets (A Δ B): Elements in either set, but not in both
symmetric_difference_set = set_a.symmetric_difference(set_b)
print("Symmetric Difference of A and B:", symmetric_difference_set)

# Check if an element is in a set
if 4 in set_a:
    print("4 is in Set A")
else:
    print("4 is not in Set A")

# Check if a set is a subset of another
subset_check = {1, 2}.issubset(set_a)
print("Is {1, 2} a subset of Set A?", subset_check)

# Check if a set is a superset of another
superset_check = set_a.issuperset({1, 2})
print("Is Set A a superset of {1, 2}?", superset_check)

# Clear all elements from Set B
set_b.clear()
print("Set B after clearing:", set_b)
