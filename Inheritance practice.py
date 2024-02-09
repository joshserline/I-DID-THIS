class Animal:

    alive = True

    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")

class Rabbit(Animal):
    def run(self):
        print("This rabbit is running")
class Fish(Animal):
    def swimming(self):
        print("This fish is swimming")
class Hawk(Animal):
    def flying(self):
        print("This hawk is flying")
Rabbit = Rabbit()
Fish = Fish()
Hawk = Hawk()

#print(Rabbit.alive)
#Fish.eat()
#Hawk.sleep()

Rabbit.run()
Fish.swimming()
Hawk.flying()
