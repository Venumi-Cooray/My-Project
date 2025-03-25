class Car:
    def __init__(self,brand,speed,fuel_usage):
        self.brand=brand
        self.speed=speed
        self.fuel_usage=fuel_usage

    def display_info(self):
        return f"This car is a {self.brand} with a top speed of {self.speed}."

    def check_speed(self, current_speed):
        if current_speed <= 60:
            return f"✅ The {self.brand} is moving at a **safe speed**: {current_speed} km/h."
        elif 61 <= current_speed <= 100:
            return f"✅ The {self.brand} is running at a **normal speed**: {current_speed} km/h."
        elif 101 <= current_speed <= 140:
            return f"⚠️ Warning! The {self.brand} is moving **too fast**: {current_speed} km/h!"
        else:  # Speed > 140 km/h
            return f"🚨 **Danger! The {self.brand} is over-speeding at {current_speed} km/h! Slow down!**"
    def fuel_efficiency(self):
        return f"The {self.brand} consumes {self.fuel_usage} liters per 100 km"

   
