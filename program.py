from car import Car

car1 = Car('Toyota',180,6.5)
car2 = Car('Tesla',250,0) 

cars = [car1, car2]

for car in cars:
    print(car.display_info())
    print(car.check_speed(50))
    print(car.check_speed(90))
    print(car.check_speed(120))
    print(car.check_speed(160))
    print(car.fuel_efficiency())
    print()

    
    

