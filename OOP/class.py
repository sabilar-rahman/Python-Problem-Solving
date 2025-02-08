class Dog:  # ক্লাস
    def __init__(self, name, age):  # কনস্ট্রাক্টর
        self.name = name  # attribute (ডাটা)
        self.age = age    # attribute (ডাটা)

    def bark(self):  # method (বিহেভিয়ার)
        print(f"{self.name} is barking!")

# অবজেক্ট তৈরি
my_dog = Dog("Tommy", 3)
my_dog.bark()  # Output: Tommy is barking!