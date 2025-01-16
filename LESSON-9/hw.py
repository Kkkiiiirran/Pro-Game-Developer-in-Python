import random
import time

class Car:
    def __init__(self, name, max_speed, fuel_capacity):
        """Initialize the car with a name, max speed, and fuel capacity."""
        self.name = name
        self.max_speed = max_speed
        self.fuel_capacity = fuel_capacity
        self.current_speed = 0
        self.fuel_level = fuel_capacity
        self.distance_covered = 0

    def accelerate(self):
        """Increase the speed of the car."""
        if self.fuel_level <= 0:
            print(f"{self.name} is out of fuel!")
            return False
        increase = random.randint(5, 15)
        self.current_speed = min(self.current_speed + increase, self.max_speed)
        self.fuel_level -= self.current_speed * 0.1  # Fuel consumption increases with speed
        self.distance_covered += self.current_speed * 0.1
        print(f"{self.name} accelerates to {self.current_speed} km/h. Fuel left: {self.fuel_level:.2f} L")
        return True

    def brake(self):
        """Reduce the speed of the car."""
        decrease = random.randint(5, 10)
        self.current_speed = max(self.current_speed - decrease, 0)
        print(f"{self.name} slows down to {self.current_speed} km/h.")

    def refuel(self):
        """Refill the car's fuel tank."""
        self.fuel_level = self.fuel_capacity
        print(f"{self.name} refueled to {self.fuel_capacity} L.")

    def status(self):
        """Display the current status of the car."""
        print(f"--- {self.name} Status ---")
        print(f"Speed: {self.current_speed} km/h")
        print(f"Fuel: {self.fuel_level:.2f} L")
        print(f"Distance covered: {self.distance_covered:.2f} km\n")


def car_race():
    """Simulate a car race."""
    print("Welcome to the Car Racing Simulation!\n")
    car1 = Car(name="Speedster", max_speed=200, fuel_capacity=50)
    car2 = Car(name="Lightning", max_speed=220, fuel_capacity=60)

    cars = [car1, car2]
    race_distance = 100  # Distance to finish the race
    turns = 0

    while all(car.distance_covered < race_distance for car in cars):
        print(f"Turn {turns + 1}\n")
        for car in cars:
            action = random.choice(["accelerate", "brake", "refuel"])
            if action == "accelerate":
                car.accelerate()
            elif action == "brake":
                car.brake()
            elif action == "refuel":
                car.refuel()
            car.status()

        turns += 1
        time.sleep(1)  # Simulate time passing in the race

    # Determine the winner
    print("\n--- Race Over ---")
    winner = max(cars, key=lambda c: c.distance_covered)
    print(f"The winner is {winner.name} with a distance of {winner.distance_covered:.2f} km!")
    print(f"Race completed in {turns} turns.\n")

    # Display final scores
    for car in cars:
        print(f"{car.name} Final Score:")
        print(f"Distance covered: {car.distance_covered:.2f} km")
        print(f"Fuel left: {car.fuel_level:.2f} L\n")


# Run the race simulation
car_race()
