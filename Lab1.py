# Chris Smith
# Chapter 14 - Lab 1
# 07/14/2025

class Vehicle:
    def __init__(self):
        self.__speed = 0

    def accelerate(self):
        self.__speed += 1

    def decelerate(self):
        if self.__speed > 0:
            self.__speed -= 1

    def display_speed(self):
        print(f"Current speed: {self.__speed}")

def main():
    car = Vehicle()

    # Accelerate twice
    print("Accelerating...")
    car.accelerate()
    car.display_speed()

    print("Accelerating...")
    car.accelerate()
    car.display_speed()

    # Decelerate twice
    print("Decelerating...")
    car.decelerate()
    car.display_speed()

    print("Decelerating...")
    car.decelerate()
    car.display_speed()

# Call main
main()

