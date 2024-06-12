class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("I am a dog")

class Cat(Animal):
    def speak(self):
        print("I am a cat")

def make_noise(animal:Animal):
    animal.speak()

dog=Dog()
cat=Cat()

make_noise(dog)
make_noise(cat)