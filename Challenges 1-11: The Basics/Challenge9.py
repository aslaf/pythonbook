"""
009
Write a program that will ask for a number of days and then will show how many
hours, minutes and seconds are in that number of days.
"""

days = int(input("Enter number of days: "))

hours = 24 * days
minute = hours * 60
seconds = minute * 60

print("There are", hours, "hours", minute, "minutes, and", seconds, "seconds in", days, "days!")
