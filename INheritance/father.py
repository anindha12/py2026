class Vehicle:

    def __init__(self, name, maxspeed, mileage):
        self.name = name
        self.maxspeed = maxspeed
        self.mileage = mileage

class Bus(Vehicle):
    pass 
school_bus = Bus("School Volvo"," 180m/ph", "12km")
print("Vehicle Name:", school_bus.name, "   Speed:",school_bus.maxspeed, "    Mileage:", school_bus.mileage)