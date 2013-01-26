# Total number of cars available.
cars = 100
# Space available in a car
space_in_a_car = 4.0

# Total number of drivers available.
drivers = 30
# # of passengers available
passengers = 90

# Total number of cars not driven.
cars_not_driven = cars - drivers
# Total number of cars driven today
cars_driven = drivers

# Space in cars avilable today
car_pool_capacity = cars_driven * space_in_a_car
# Average passenger calculation for today
average_passenger_per_car = passengers / cars_driven


print "There are ", cars, " available."
print "There are only ", drivers, " available."
print "There will be ", cars_not_driven, " empty cars today."
print "We can transport ", car_pool_capacity, " people today."
print "We have", passengers, " to carpool today"
print "We need to put", average_passenger_per_car, " passengers per car"
