import os

clear = lambda: os.system('cls')

class vehicle:

    def __init__(self, model,rok_vyroby):
        self.model = model
        self.rok_vyroby = rok_vyroby

    def __str__(self):
        return f"model vozidla {self.model} was made {self.rok_vyroby} "
    
    def blinkr(self, svetlo="//"):
        return f"vozidlo {self.model} má blinkr {svetlo}."

class car(vehicle):

    def blinkr(self, svetlo="//-//"):
        return vehicle.blinkr(self, svetlo) + f" car {self.model} má blinkr {svetlo}."

class motorbike(vehicle):

    def blinkr(self, svetlo="// // -// // "):
        return vehicle.blinkr(self, svetlo) + f" motorbike {self.model} má blinkr {svetlo}."
    
class truck(vehicle):

    def blinkr(self, svetlo=" //-//// "):
        return vehicle.blinkr(self, svetlo) + f" truck {self.model} má blinkr {svetlo}."


clear()

print("-"*69, "eeeeeeee", "-"*69)
wvgolf = car("golf",2006 )
print(wvgolf)
print(wvgolf.blinkr())
print(wvgolf.blinkr("bleeeh"))

print("-"*69, "qwdqdqdqdd", "-"*69)
babeta = motorbike("babeta", 1952)
print(babeta)
print(babeta.blinkr())
print(babeta.blinkr("///"))

print("-"*69, "wwwwwwwwww", "-"*69)
tatra = truck("tatra",1948)
print(tatra)
print(tatra.blinkr())
print(tatra.blinkr("///-////-"))

print("-"*69, "fdfdfcfc", "-"*69)
if isinstance(babeta, vehicle): print(f"{babeta.model} is a vehicle.")
if isinstance(babeta, car): print(f"{babeta.model} is a car.")
if isinstance(babeta, tatra): print(f"{babeta.model} is tatra.")
if isinstance(tatra, vehicle): print(f"{tatra.model} is a vehicle.")
if isinstance(tatra, motorbike): print(f"{tatra.model} is motorbike.")
if isinstance(tatra, wvgolf): print(f"{tatra.model} is wv golf.")
if isinstance(wvgolf, vehicle): print(f"{wvgolf.model} is a vehicle.")
if isinstance(wvgolf, truck): print(f"{wvgolf.model} is  a truck.")
if isinstance(wvgolf, wvgolf): print(f"{wvgolf.model} is wv golf.")