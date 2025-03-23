from car import Car

car1 = Car('Toyota')
car2 = Car('Tesla')

cars = [car1, car2]

for car in cars:
    print(car.display_info())