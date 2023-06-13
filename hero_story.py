# Task 3 Hero story

story1 = {
    "start": "In a world where zombies rule, an unlikely hero emerged. His name was Dave. ",
    "middle": "Dave had the ability to snap his fingers and the zombie heads would explode into pink glitter. ",
    "end": "He did this to all of the zombies in the land and saved man-kind! Now we just need a hero that can deal with glitter..."
}

# print(story1)
# print(type(story1))
# print(story1.keys())
# print(story1.values())
# print(story1["start"])
# print(story1["middle"])
# print(story1["end"])
#
# story1["hero"] = "Dave"
#
# print(story1)

story = story1.values()
print(story)

for value in story:
    print(value)
