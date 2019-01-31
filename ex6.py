# Learn Python 3 the Hard Way
# Exercise 6

#variable assignation
types_of_people = 10

#variable assignation
x = f"There are {types_of_people} types of people."

#another 3 variables assignation
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

#print variables x and y
print(x)
print(y)

#print 2 strings with variables in them
print(f"I said: {x}")
print(f"I also said '{y}'")

#variable assignation
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

#
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

#print the concation of the 2 strings declared above
print(w + e)
