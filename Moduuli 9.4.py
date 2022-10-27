import random
class car:
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


cars = list()
for i in range(10):
    hp = random.randint(100, 200)
    cars.append(car(f"ABC-{i+1}", hp))
while cars[i].distance <= 10000:
    for i in range(10):
        cars[i].accelerate(random.randint(-10, 15))
        cars[i].travel(1)
        if cars[i].distance >= 10000:
            print(cars[i].plate, "Voitti!")
            break

