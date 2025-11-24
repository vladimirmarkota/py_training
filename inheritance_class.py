class animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return ("...")

class dog(animal):
    def bark(self):
        return "woof"

    def speak(self):
        return "woof"

pas = dog("maro")
print(pas.name)
print(pas.speak())
print(pas.bark())




