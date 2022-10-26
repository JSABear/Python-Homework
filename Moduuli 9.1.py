#9.1

class car:
    def __init__(self, plate, topspeed):

        self.plate = plate
        self.topspeed = topspeed
        self.speed = 0
        self.distance = 0

car1 = car ("ABC-123", "142 km/h")


print(f"Plate: {car1.plate}, Top speed: {car1.topspeed}, Current Speed: {car1.speed} km/h,Distance traveled: {car1.distance} km")
