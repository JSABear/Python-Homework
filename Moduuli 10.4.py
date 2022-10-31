#10.4

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

    def get_info(self):
        print(f"Plate: {self.plate}, Top speed: {self.top_speed} km/h, Current Speed: {self.speed} km/h, Distance traveled: {self.distance} km")


class race:
    def __init__(self, race_name, race_length, car_list):
        self.race_name = race_name
        self.race_length = race_length
        self.car_list = car_list

    def hour_passes(self):
        for i in range(10):
            self.car_list[i].accelerate(random.randint(-10, 15))
            self.car_list[i].travel(1)

    def print_info(self):
        for car in self.car_list:
            car.get_info()


    def race_over(self):

        for i in range(len(self.car_list)):
            if self.car_list[i].distance >= self.race_length:
                race1.print_info()
                print(self.car_list[i].plate, "Voitti!")
                return True
        return False

cars = list()

for i in range(10):
    hp = random.randint(100, 200)
    cars.append(car(f"ABC-{i+1}", hp))

race1 = race("Suuri romuralli", 8000, cars)

game_over = False
hours_passed = 0

while game_over == False:
    race1.hour_passes()
    hours_passed += 1
    if hours_passed == 10:
        hours_passed = 0
        race1.print_info()
        print("")
    game_over = race1.race_over()

