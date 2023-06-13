# Dictionaries

# Making a dictionary

student_1 = {
    "name": "luke",
    "stream": "DevOps",
    "completed_lessons": 4,
    "completed_lesson_names": ["variables", "git", "data types", "collections"]
}

print(student_1)

# How to access parts of a dictionary

print(student_1["stream"])
print(student_1["completed_lesson_names"][0])

# Changing a value

student_1["completed_lessons"] = 3

student_1["completed_lesson_names"].remove("data types")

# Dictionary methods

print(student_1.keys())
print(student_1.values())