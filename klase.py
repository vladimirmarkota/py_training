class Dog:
    species = "Canine" #class atribut, shared by all instances in this class
    def __init__(self, name, age):   #initiliazes the name and age attributes when new object is created
        self.name = name  #instance attribute
        self.age = age #inst atr

class auto:
    brand = "bmw"
    def __init__(self, series, colour):
        self.series = series
        self.colour = colour

class voce:
    vrsta = "agrum"
    def __init__(self, ime, boja):
        self.ime = ime
        self.boja = boja

voce1 = voce("limun", "zuta")
voce2 = voce("naranca", "narancasta")

print(voce1.ime, voce1.boja)
print(voce2.ime, voce2.boja)
print(voce1.ime, voce2.boja)


