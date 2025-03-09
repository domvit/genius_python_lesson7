class Vehicle:
    """Base class for all vehicles"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_attributes(self):
        for attribute in self.__dict__:
            print(f"{attribute}: {self.__dict__[attribute]}")

    def display_info(self):
        print(f"Це {self.make} {self.model} {self.year} року виробництва.")

class Car(Vehicle):
    """Car class"""
    def __init__(self, make, model, year, fuel):
        super().__init__(make, model, year)
        self.fuel = fuel

    def start_engine(self):
        print(f"Car engine started. Fuel: {self.fuel}")

    def display_info(self):
        print(f"Це автомобіль {self.make} {self.model} {self.year} року виробництва. Працює на {self.fuel}.")

class Motorcycle(Vehicle):
    """Motorcycle class"""
    def __init__(self, make, model, year, count_of_cylinder):
        super().__init__(make, model, year)
        self.count_of_cylinder = count_of_cylinder

    def get_sound(self):
        print(f"Motorcycle engine on. Count of cylinder: {self.count_of_cylinder}")

    def display_info(self):
        print(f"Це мотоцикл {self.make} {self.model} {self.year} року виробництва. В нього {self.count_of_cylinder} циліндри.")

class Bicycle(Vehicle):
    """Bicycle class"""
    def __init__(self, make, model, year, weight):
        super().__init__(make, model, year)
        self.weight = weight

    def get_weight(self):
        print(f"Bicycle weight is {self.weight}.")

    def display_info(self):
        print(f"Це лісапєд {self.make} {self.model} {self.year} року виробництва. Його вага {self.weight} кг.")


# task_1
print("Task 1")

car = Car('Ford', 'Mustang', 1999, "gas")
car.get_attributes()
car.start_engine()
print("----------------------------")

motorcycle = Motorcycle('Dnipro', 'Torpeda', 2022, 2)
motorcycle.get_attributes()
motorcycle.get_sound()
print("----------------------------")

bicycle = Bicycle('HTZ', 'T-40', 2015, 3)
bicycle.get_attributes()
bicycle.get_weight()
print("----------------------------")
print("END Task 1", end="\n\n")
# end task_1


# task_2
print("Task 2")
for vehicle in (car, motorcycle, bicycle):
    vehicle.display_info()

print("END Task 2", end="\n\n")
# end task_2
