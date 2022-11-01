class Car:
    def __init__(self, plate, top_speed):

        self.plate = plate
        self.top_speed = top_speed
        self.speed = 0
        self.distance = 0

    def accelerate(self, acceleration):

        if acceleration > 0:
            self.speed = self.speed + acceleration
            if self.speed > self.top_speed:
                self.speed = self.top_speed
            else:
                return
        elif acceleration < 0:
            self.speed = self.speed + acceleration
            if self.speed < 0:
                self.speed = 0
            else:
                return

    def travel(self, hours):
        self.distance = self.speed * hours + self.distance

    def get_info(self):
        print(f"Plate: {self.plate}, Top speed: {self.top_speed} km/h, Current Speed: {self.speed}/ "
              f"km/h, Distance traveled: {self.distance} km, ", end="", flush=True)


class Electric(Car):
    def __init__(self, plate, top_speed, battery_size):
        self.battery_size = battery_size
        super().__init__(plate, top_speed)

    def get_info(self):
        super().get_info(), print(f"Battery capacity: {self.battery_size} kWh")


class Fuel(Car):
    def __init__(self, plate, top_speed, fuel_tank):
        self.fuel_tank = fuel_tank
        super().__init__(plate, top_speed)

    def get_info(self):
        super().get_info(), print(f"Fuel tank: {self.fuel_tank} l")


car1 = Fuel("ACD-123", 165, 32.3)
car1.accelerate(car1.top_speed)
car1.get_info()

car2 = Electric("ABC-15", 180, 52.5)
car2.accelerate(car2.top_speed)
car2.get_info()

car1.travel(3)
car2.travel(3)

print(f"Odometer {car1.distance} km")
print(f"Odometer {car2.distance} km")