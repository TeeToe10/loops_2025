# while loops = execute some code while some condition remains true
# name = input("Enter your name: ") 


# if name == "":
#     print("You did not enter your name")
# else: 
#     print("Hello (name)") 
# while name == "":
#     print("You did not enter your name")
#     name = input("Enter your name") 
# print("Hello (name)")

# age = int(input("Enter your age: ")) 

# while age < 0:
#     print("Age cam't be negative") 
#     age = int(input("Enter your age: ")) 

# food = input("Enter a food you like (q to quit): ") 
# while not food == "q":
#     food_list = []
#     print(f"You like {food}")
#     food_list.append(food)
#     food = input("Enter another food you like (q to quit): ")

# print("Bye")

# num = int(input("Enter a # between 1 - 10: "))
# while num < 1 or num > 10:
#     print(f"(num) is not valid")
#     num = int(input("Enter a # between 1 - 10: "))

# print(f"Your number is {num}")

# Given:
colors = ["red", "blue", "green", "yellow", "purple"]

# Challenge:
# Use a while loop to print each color UNTIL you find "yellow".
# Do NOT print "yellow" — stop before it.
index = 0
while index < len(colors):
    if colors[index] == "yellow":
          break
    print(colors[index])
    index += 1 #increment the index to avoid infinite loop
    