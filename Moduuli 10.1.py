10.1

class elevator:
    def __init__(self):
        self.max_floor = 10
        self.min_floor = 0
        self.floor = self.min_floor


    def go_to(self, selected_floor):
        if selected_floor > self.floor:
            while selected_floor > self.floor:
                elevators[i].floor_up()
        elif selected_floor < self.floor:
            while selected_floor < self.floor:
                elevators[i].floor_down()
        else:
            print("Olet tässä kerroksessa.")

    def floor_up(self):
        self.floor = self.floor + 1
        print(f"{elevators[i].floor} kerros")

    def floor_down(self):
        self.floor = self.floor - 1
        print(f"{elevators[i].floor} kerros")

elevators = list()

for i in range(1):
    elevators.append(elevator())


elevators[i].go_to(6)

elevators[i].go_to(0)



