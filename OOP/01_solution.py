class Car:
    def __init__(self,userBrand, userModel):
        self.brand = userBrand
        self.model = userModel

my_Car= Car("Toyota", "Camry")
print(my_Car.brand)

my_new_car = Car("Honda", "Civic")
print(my_new_car.model)