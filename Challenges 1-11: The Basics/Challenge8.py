"""
008
Ask for the total price of the bill, then ask how
many diners there are. Divide the total bill by the
number of diners and show how much each
person must pay.
"""

total = int(input("Enter total amount of bill: "))
diners = int(input("Enter number of diners: "))

per_person = total / diners
# print(type(per_person))
print("Each person should pay", per_person)