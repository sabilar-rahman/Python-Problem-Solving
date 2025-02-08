class Car:
    def __init__(self,userBrand, userModel):
        self.brand = userBrand
        self.model = userModel

    def full_name(self):
        return f"{self.brand} {self.model}"
    

class ElectricCar(Car):
    def __init__(self,brand, model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size


my_car = ElectricCar("Tesla","Model S","85kwH")
print(my_car.full_name())


