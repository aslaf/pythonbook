"""
021
Ask the user to enter their first name and then ask them to
enter their surname. Join them together with a space between
and display the name and the length of whole name.
"""

firstname = input("Enter your first name: ")
surname = input("Enter your surname: ")
name = firstname + " " + surname
print(name)
print(len(name))