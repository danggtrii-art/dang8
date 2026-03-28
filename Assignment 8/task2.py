class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current_floor = bottom
    def floor_up(self):
        if self.current_floor < self.top:
            self.current_floor += 1
            print(f"Elevator at floor {self.current_floor}")
    def floor_down(self):
        if self.current_floor > self.bottom:
            self.current_floor -= 1
            print(f"Elevator at floor {self.current_floor}")
    def go_to_floor(self, target):
        while self.current_floor < target:
            self.floor_up()
        while self.current_floor > target:
            self.floor_down()
class Building:
    def __init__(self, bottom, top, num_elevators):
        self.elevators = []
        for i in range(num_elevators):
            self.elevators.append(Elevator(bottom, top))
    def run_elevator(self, elevator_number, destination):
        print(f"\nRunning elevator {elevator_number} to floor {destination}")
        self.elevators[elevator_number].go_to_floor(destination)
    def fire_alarm(self):
        print("\n🔥 FIRE ALARM!")
        for i, elevator in enumerate(self.elevators):
            print(f"Elevator {i} going to bottom floor")
            elevator.go_to_floor(elevator.bottom)
if __name__ == "__main__":
    building = Building(1, 10, 3)

    building.run_elevator(0, 7)
    building.run_elevator(1, 3)

    building.fire_alarm()