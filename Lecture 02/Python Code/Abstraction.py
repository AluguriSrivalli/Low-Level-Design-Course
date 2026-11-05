from abc import ABC, abstractmethod

"""
Car Interface --> Act as an interface for Outside world to operate the car. 
This interface tells 'WHAT' all it can do rather than 'HOW' it does that.
Since this is an interface we cannot directly create Objects of this. We
need to implement it first and then that child class will have the responsibility to 
provide implementation details of all the methods in the interface.

In our real world example of Car, imagine you sitting in the car and able to operate
the car (startEngine, accelerate, brake, turn) just by pressing or moving some
pedals/buttons/steering wheel etc. You dont need to know how these things work, and
also they are hidden under the hood.
This Interface 'Car' denotes that (pedals/buttons/steering wheel etc). 
"""
class Car(ABC):
    
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def shift_gear(self, gear: int):
        pass

    @abstractmethod
    def accelerate(self):
        pass

    @abstractmethod
    def brake(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass


"""
This is a Concrete class (A class that provide implementation details of an interface/abstract class).
Now anyone can make an Object of 'SportsCar' and can assign it to 'Car' reference. 
(See main block for this)

In our real world example of Car, as you cannot have a real car by just having its body only
(all these buttons or pedals). You need to have the actual implementation of 'What' happens
when we press these buttons. 'SportsCar' class denotes that actual implementation. 

Hence we can conclude, to denote a real world car in programming we created 2 classes.
One to denote all the user-interface like pedals, buttons, steering wheels etc ('Car' interface).
And another one to denote the actual car with all the implementations of these buttons ('SportsCar' class).
"""
class SportsCar(Car):

    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model
        self.is_engine_on = False
        self.current_speed = 0
        self.current_gear = 0

    def start_engine(self):
        self.is_engine_on = True
        print(f"{self.brand} {self.model} : Engine starts with a roar!")

    def shift_gear(self, gear: int):
        if not self.is_engine_on:
            print(f"{self.brand} {self.model} : Engine is off! Cannot Shift Gear.")
            return
        self.current_gear = gear
        print(f"{self.brand} {self.model} : Shifted to gear {self.current_gear}")

    def accelerate(self):
        if not self.is_engine_on:
            print(f"{self.brand} {self.model} : Engine is off! Cannot accelerate.")
            return
        self.current_speed += 20
        print(f"{self.brand} {self.model} : Accelerating to {self.current_speed} km/h")
    
    def brake(self):
        self.current_speed -= 20
        if self.current_speed < 0:
            self.current_speed = 0
        print(f"{self.brand} {self.model} : Braking! Speed is now {self.current_speed} km/h")

    def stop_engine(self):
        self.is_engine_on = False
        self.current_gear = 0
        self.current_speed = 0
        print(f"{self.brand} {self.model} : Engine turned off.")


# Main Method Execution
if __name__ == "__main__":

    my_car: Car = SportsCar("Ford", "Mustang")

    my_car.start_engine()
    my_car.shift_gear(1)
    my_car.accelerate()
    my_car.shift_gear(2)
    my_car.accelerate()
    my_car.brake()
    my_car.stop_engine()
