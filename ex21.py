# Learn Python 3 the Hard Way
# Exercise 21

def add(a, b):
    print(f"Adding {a} + {b}")
    return a + b

def substract(a, b):
    print(f"Substracting {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"Multiplying {a} * {b}")
    return a * b

def divide (a, b):
    print(f"Diving {a} by {b}")
    return a / b

print("Let's do some math with just functions:")

age = add(30, 5)
height = substract(78, 4)
weight = multiply(90, 2)
iq = divide(100,2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ:{iq}")

#A puzzle for the extracredit, type it in anyway:
print ("Here is a puzzle:")

what = add(age, substract(height, multiply(weight, divide(iq, 2))))

print("That becomes:", what, "Can you do that by hand?")
