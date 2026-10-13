set1 = {"Roger", "Sid"}
set2 = {"Roger"}

# Set operations
print(set1 & set2)     #intersection
print(set1 | set2)     # Union
print(set1 - set2)     #difference
print(set1 > set2)     # Superset check- True
print(set1 < set2)     # Subset check- False

# Duplicates automatically discarded
unique_names = set(["Roger", "Sid", "Roger"])
print(unique_names)    # {'Roger', 'Sid'}