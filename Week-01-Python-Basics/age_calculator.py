from datetime import date

name = input("Enter your name: ")
birth_year = int(input("Enter birth year: "))

age = date.today().year - birth_year

print("Hello!", name)
print("You are", age, "years old")