
#There are 100 cars
cars = 100

#A car can fit 4 people
space_in_a_car = 4

#Number of drivers
drivers = 30

#Number of passangers
passengers = 90

#Cars not driven are the cars without drivers
cars_not_driven = cars - drivers

#Cars that are driven are the cars that do have drivers
cars_driven = drivers

#The total number of people that can be transported is:
#the number of cars multiplied by the number of passengers a car can carry
carpool_capacity = cars_driven * space_in_a_car

#Avarage passengers per car:
avarage_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers are available.")
print("There will be", cars_not_driven,"empty cars today.")
print("We can transport", carpool_capacity,"people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", avarage_passengers_per_car, "in each car.")
