# Collections

A collection is a store of multiple pieces of data.

## Lists and tuples

Lists are the same as arrays in JavaScript. It uses square brackets and is separated by commas [].
You can use indexes to pick out items within an array. For example: shopping_list[3] .
You can also change an item in the list. For example: shopping_list[3] = "Oranges"

List can be have a mix of data types.

### List methods

- .append("butter") -> adds to the end of the list
- .remove("butter") -> removes the item
- .pop() -> removes the last item

### List slicing 

example: mixture[1:3]
mixture[::2]

### Tuples

Tuples are immutable, they cant be changed, very similar to lists. They use ().
Example:

("eggs", "cheese", "bread")

## Dictionaries

Are like objects. Use {}. They have keys and values.
You can have mixed data types. Keys can be accessed by square bracket notation.

Example of a dictionary:
```python
student_1 = {
    "name": "luke",
    "stream": "DevOps",
    "completed_lessons": 4,
    "completed_lesson_names": ["variables", "git", "data types", "collections"]
}
```

How to change values:
```python
student_1["completed_lessons"] = 3
student_1["completed_lesson_names"].remove("data types")
```
### Dictionary methods

- print(student_1.keys()) -> Will print all the keys
- print(student_1.values()) -> Will print all the values

## Sets

Sets are very similar to lists but they are unordered. They use curley brackets {}.

Example of a set:

```python
car_parts = {"wheels", "windows", "exhaust","steering wheel"}
```

### Set methods

- car_parts.add("doors") -> will add to the set
- car_parts.remove("doors") -> will remove from the set

### Frozen sets

These are immutable sets. Here is an example:

```python
x = frozenset([1, 2, 3, 4, 5, 6, 7])
print(x)
```