# Lists (Array) and Tuples

# Making a list in python

shopping_list = ["eggs", "bacon", "bananas", "bread", "haggis"]

# print(type(shopping_list))
#
# # Access a specific item in the list
#
# print(shopping_list[2])
#
# # Change a specific element of the list
#
# shopping_list[4] = "orange juice"
# print(shopping_list)
#
# #list methods
#
# shopping_list.append("butter") # adds to the end of the list
# print(shopping_list[5])
#
# shopping_list.remove("butter") # removes the item
# print(shopping_list)
#
# shopping_list.pop() # removes the last item
# print(shopping_list)

# Mixed data type lists

mixture = [1, 2, 3, "one", "two", "three"]
print(mixture)

# list slicing

print(mixture[1:3]) # [2, 3]
print(mixture[::2]) # [1, 3, "two"]

# Tuples - immutable, they cant be changed.

essentials = ("bread", "eggs", "milk")
print(essentials)