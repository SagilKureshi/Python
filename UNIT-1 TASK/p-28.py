# Program to find the year when the user will turn 60

name = input("Enter your name: ")
age = int(input("Enter your age: "))

current_year = 2026
year_to_60 = current_year + (60 - age)

print(name, "will turn 60 years old in the year", year_to_60)