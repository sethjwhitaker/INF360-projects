# INF360 - Programming in Python
# Seth Whitaker
# Assignment 1

# Greet user
print("Welcome! What is your name?") 

# Get input from user
name = input()
birthYear = input("What year were you born?\n") 

# Calculate age and decades
age = 2020 - int(birthYear) - 1
decades = int((age - age % 10) / 10)

# Output result to user
print("Hello " + name + "!")
print("You are at least " + str(age) + " years old,")
print("meaning that you have been alive for over " + str(decades) + " decades.")


