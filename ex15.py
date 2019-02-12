# Learn Python 3 the Hard Way
# Exercise 15

from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())
txt.close()

print("Type the file again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
txt_again.close()
