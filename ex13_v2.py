# Learn Python 3 the Hard Way
# Exercise 13 - 6 arguments instead of 4

from sys import argv
#read the WYSS section for how to run this
script, first, second, third, fourth, fifth = argv

print("The script is called: ", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
print("Your fourth variable is:", fourth)
print("Your fith variable is:", fifth)
