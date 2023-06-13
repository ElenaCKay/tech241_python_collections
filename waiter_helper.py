# Task 2

menu = {
    "starters": ["soup", "olives", "chicken strips", "nachos"],
    "mains": ["pizza", "burger", "sushi", "ramen", "hot dog"],
    "desserts": ["cheesecake", "ice-cream", "milkshake", "tiramisu"]
}

guest_list = []


print("Hello, here is the menu")
print(menu)

guest_starter = input("What would you like for your starter? ")
guest_list.append(guest_starter)

guest_main = input("What would you like for your main? ")
guest_list.append(guest_main)

guest_dessert = input("What would you like for dessert? ")
guest_list.append(guest_dessert)

print(f"You have ordered the {guest_list[0]}, the {guest_list[1]} and the {guest_list[2]}.")