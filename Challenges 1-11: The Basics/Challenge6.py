"""
006
Ask how many slices of pizza the user started with and ask how many slices they have eaten.
Work out how many slices they have left and display the answer in a userfriendly format.
"""

total_pizza_slices = int(input("Enter total num of pizza slices: "))
slices_eaten = int(input("Enter num of slices you ate: "))

slices_remaining = total_pizza_slices - slices_eaten

print("You have", slices_remaining, "slices remaining")