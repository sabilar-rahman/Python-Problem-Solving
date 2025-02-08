class Car:
    def __init__(self,userBrand, userModel):
        self.brand = userBrand
        self.model = userModel

    def full_name(self):
        return f"{self.brand} {self.model}"

my_Car= Car("Toyota", "Camry")
# print(my_Car.brand)
print(my_Car.full_name())

# my_new_car = Car("Honda", "Civic")
# print(my_new_car.model)