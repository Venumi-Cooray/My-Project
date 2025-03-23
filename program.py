from car import Car

car1 = Car('Toyota',180)
car2 = Car('Tesla',250)

cars = [car1, car2]

for car in cars:
    print(car.display_info())