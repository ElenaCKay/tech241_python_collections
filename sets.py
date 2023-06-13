# Sets and Frozen sets

# Lists but unordered {}

car_parts = {"wheels", "windows", "exhaust","steering wheel"}
print(car_parts)

# add to a set

car_parts.add("doors")
print(car_parts)

# remove form a set

car_parts.remove("doors")
print(car_parts)

# Frozen set - immutable set

x = frozenset([1, 2, 3, 4, 5, 6, 7])
print(x)

