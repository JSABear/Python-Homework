#9.3

class car:
    def __init__(self, plate, top_speed):

        self.plate = plate
        self.topspeed = top_speed
        self.speed = 0
        self.distance = 0

    def accelerate(self, acceleration):

        if acceleration > 0:
            self.speed = self.speed + acceleration
            if self.speed > self.topspeed:
                self.speed = self.topspeed
            else:
                return
        elif acceleration < 0:
            self.speed = self.speed + acceleration
            if self.speed < 0:
                self.speed = 0
            else:
                return

    def travel(self,hours):
        self.distance = self.speed * hours + self.distance


car1 = car ("ABC-123", 142)

print(f"Plate: {car1.plate}, Top speed: {car1.topspeed} km/h, Current Speed: {car1.speed} km/h,Distance traveled: {car1.distance} km")

car1.accelerate(30)

car1.accelerate(70)

car1.accelerate(50)
print(f"{car1.speed} km/h")

car1.accelerate(-200)
print(f"{car1.speed} km/h")
