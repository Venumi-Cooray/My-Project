class Car:
    def __init__(self,brand,speed):
        self.brand=brand
        self.speed=speed

    def display_info(self):
        return f"This car is a {self.brand} with a top speed of {self.speed}."
