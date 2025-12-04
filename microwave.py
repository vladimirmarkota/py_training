class Microwave:
    def __init__(self, brand: str, power_rating: str)->None:
        self.brand = brand
        self.power_rating = power_rating
        self.turned_on: bool = False

    def turn_on(self) -> None:
        if self.turned_on:
            print(f"Microwave {self.brand} is allready turned on")
        else:
            self.turned_on = True
            print(f"Microwave {self.brand} is now turned on")

    def turn_off(self) -> None:
        if self.turned_on:
           self.turned_on = False
           print(f"Microwave ({self.brand}) is now turned off")
        else:
            print(f"Microwave {self.brand} is already off")

    def run(self, seconds: int) -> None:
        if self.turned_on:
            print(f"Microwave {self.brand} running for {seconds} seconds")
        else:
            print(f"Turn on {self.brand}")



smeg: Microwave = Microwave("Smeg", "B")
print(smeg.brand, smeg.power_rating)

bosch: Microwave = Microwave("Bosch", "C")
print(bosch.brand, bosch.power_rating)

'''
smeg.turn_on()
smeg.turn_on()

smeg.turn_off()
smeg.turn_off()

smeg.run(5)
smeg.turn_on()
smeg.run(5)
'''

