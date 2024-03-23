"""
022
Ask the user to enter their first name and surname in lower
case. Change the case to title case and join them together.
Display the finished result.
"""

firstname = input("Enter your first name in lowercase: ")
surname = input("Enter your surname in lowercase: ")
name = firstname.title() + " " + surname.capitalize()

print(name)



