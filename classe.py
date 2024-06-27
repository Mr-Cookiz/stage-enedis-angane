class Animal :
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print(f"Cet animal s'appelle {name} et il a {age} ans .")
    def faireUnBruit (self):
        print()

class Chien(Animal):
    def faireUnBruit (self):
        print("Ouaf")

class Chat(Animal):
    def faireUnBruit (self):
        print("miaou")

maTortue = Animal("Caroline",50)
monChien = Chien("bill",5)
monChat = Chat("Garfield",12)

maTortue.faireUnBruit()
monChien.faireUnBruit()
monChat.faireUnBruit()
