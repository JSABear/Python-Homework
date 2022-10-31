# 10.3

class building:
    def __init__(self, num_of_elevators):
        self.min_floor = 0
        self.max_floor = 10
        self.num_of_elevators = num_of_elevators
        self.elevators = []
        for i in range (self.num_of_elevators):
            self.elevators.append(elevator())

    def ride_elevator(self, target_elevator, target_floor):
        self.target_elevator = target_elevator-1
        self.elevators[self.target_elevator].go_to(target_floor)

    def firealarm(self):
        for i in range(self.num_of_elevators):
            building1.ride_elevator(i, 0)
class elevator:
    def __init__(self,):
        self.max_floor = 10
        self.min_floor = 0
        self.floor = self.min_floor


    def go_to(self, selected_floor):
        if selected_floor > self.floor:
            while selected_floor > self.floor:
                building1.elevators[building1.target_elevator].floor_up()
        elif selected_floor < self.floor:
            while selected_floor < self.floor:
                building1.elevators[building1.target_elevator].floor_down()

    def floor_up(self):
        self.floor = self.floor + 1
        print(f"{building1.elevators[building1.target_elevator].floor} kerros")

    def floor_down(self):
        self.floor = self.floor - 1
        print(f"{building1.elevators[building1.target_elevator].floor} kerros")



building1 = building(4)

building1.ride_elevator(1, 1)

building1.ride_elevator(2, 2)

building1.ride_elevator(3, 3)

building1.ride_elevator(4, 4)

building1.firealarm()