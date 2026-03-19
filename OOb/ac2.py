print("This is a vehicle class")    

class vehicle:

    
    def __init__(self, max_speed, model, mileage):
        self.max_speed = max_speed
        self.model = model
        self.mileage = mileage

car = vehicle(240, "BMW", 18)
print("Car model:", car.model)
print("Car max speed:", car.max_speed)
print("Car mileage:", car.mileage)  
