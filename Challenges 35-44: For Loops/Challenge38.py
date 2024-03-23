"""
038
Change program 037 to also ask for a number. Display their name (one letter at a time on each line) and
repeat this for the number of times they entered.
"""

name = input("Enter your name: ")
num = int(input("Enter a number: "))

for i in range(0, num):
    for x in name:
        print(x)