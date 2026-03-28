import random
class Car:
    def __init__(self, reg_number, max_speed):
        self.reg_number = reg_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.distance = 0
    def drive(self, hours):
        self.distance += self.current_speed * hours
class Race:
    def __init__(self, name, km, cars):
        self.name = name
        self.distance = km
        self.cars = cars
    def hour_passes(self):
        for car in self.cars:
            change = random.randint(-10, 15)
            car.current_speed = max(0, min(car.max_speed, car.current_speed + change))
            car.drive(1)
    def print_status(self):
        print("\n--- Race Status ---")
        print(f"{'Car':10} {'Speed':10} {'Distance':10}")
        for car in self.cars:
            print(f"{car.reg_number:10} {car.current_speed:10} {car.distance:10}")
    def race_finished(self):
        for car in self.cars:
            if car.distance >= self.distance:
                return True
        return False
if __name__ == "__main__":
    cars = []
    for i in range(10):
        car = Car(f"ABC-{i+1}", random.randint(100, 200))
        cars.append(car)
    race = Race("Grand Demolition Derby", 8000, cars)
    hours = 0
    while not race.race_finished():
        race.hour_passes()
        hours += 1
        if hours % 10 == 0:
            race.print_status()
    print("\n🏁 Race finished!")
    race.print_status()