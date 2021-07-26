# Eg to define a class in python
# Eg to represent each employees as a list
kirk = ["James kirk",34,"Captain",2265]
spock = ["Spock" ,35,"Science Officer",2254]
mccoy = ["Leonard Mccoy","Chief Medical Officer",2254]

#Eg to define a class
# Eg of a Dog class:
class Dog:
    pass
#update of dog class with__init__()method
class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

# Following Dog class has a class attribute called species with the value "Canis familiaris":
class Dog:
    def __init__ (self,name,age):
        self.name = name
        self.age  = age
        
# instantiate an object in python
>>> class Dog:
...     pass
# instanciating a new Dog object
>>> Dog()
<__main__.Dog object at 0x106702d30>

# now instantiate second Dog object
>>> Dog()
<__main__.Dog object at 0x0004ccc90>
#create two new Dog objects
>>> a = Dog()
>>> b = Dog()
>>> a == b
False
# Class & instance attributes
>>> class Dog:
...     species = "Canis familiaris"
...     def __init__(self, name, age):
...         self.name = name
...         self.age = age
# To pass arguments to the name and age parameters, put values into the parentheses after the class name
>>> buddy = Dog("Buddy", 9)
>>> miles = Dog("Miles", 4)
#  accessing class attributes the samilar way
>>> buddy.species
'Canis familiaris'
# changing values of attributes
>>> buddy.age = 10
>>> buddy.age
10

>>> miles.species = "Felis silvestris"
>>> miles.species
'Felis silvestris'
#Instance methods
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

# enter this dog class
>>> miles = Dog("Miles", 4)

>>> miles.description()
'Miles is 4 years old'

>>> miles.speak("Woof Woof")
'Miles says Woof Woof'

>>> miles.speak("Bow Wow")
'Miles says Bow Wow'
# create a list object
>>> names = ["Fletcher", "David", "Dan"]
>>> print(names)
['Fletcher', 'David', 'Dan']
# while print() miles object
>>> print(miles)
<__main__.Dog object at 0x00aeff70>

# change the name of the dog class
class Dog:
    # Leave other parts of Dog class as-is

    # Replace .description() with __str__()
    def __str__(self):
        return f"{self.name} is {self.age} years old"
# Dog Park Example
# modify Dog park in editor
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

#  Model the dog park by instantiating a bunch of different dogs
>>> miles = Dog("Miles", 4, "Jack Russell Terrier")
>>> buddy = Dog("Buddy", 9, "Dachshund")
>>> jack = Dog("Jack", 3, "Bulldog")
>>> jim = Dog("Jim", 5, "Bulldog")
# Supply a string for the sound argument
>>> buddy.speak("Yap")
'Buddy says Yap'

>>> jim.speak("Woof")
'Jim says Woof'

>>> jack.speak("Woof")
'Jack says Woof'
# Parent Classes vs Child Classes
#create a child class
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"
#create three new child classes of the Dog class
class JackRussellTerrier(Dog):
    pass

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass
#instantiate some dogs of specific breeds
>>> miles = JackRussellTerrier("Miles", 4)
>>> buddy = Dachshund("Buddy", 9)
>>> jack = Bulldog("Jack", 3)
>>> jim = Bulldog("Jim", 5)
# inherit all of the attributes and methods of the parent class
>>> miles.species
'Canis familiaris'

>>> buddy.name
'Buddy'

>>> print(jack)
Jack is 3 years old

>>> jim.speak("Woof")
'Jim says Woof'

# To determine which class a given object belongs to
>>> type(miles)
<class '__main__.JackRussellTerrier'>

# to determine if miles is also an instance of the Dog class
>>> isinstance(miles, Dog)
True
# The miles, buddy, jack, and jim objects are all Dog instances
>>> isinstance(miles, Bulldog)
False

>>> isinstance(jack, Dachshund)
False
#Extend the Functionality of a Parent Class
class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return f"{self.name} says {sound}"
#instance without passing an argument to sound
>>> miles = JackRussellTerrier("Miles", 4)
>>> miles.speak()
'Miles says Arf'
# dog with different sound
>>> miles.speak("Grrr")
'Miles says Grrr'
#change the string returned by .speak() in the Dog class
class Dog:
    # Leave other attributes and methods as they are

    # Change the string returned by .speak()
    def speak(self, sound):
        return f"{self.name} barks: {sound}"

# create a new Bulldog instance
>>> jim = Bulldog("Jim", 5)
>>> jim.speak("Woof")
'Jim barks: Woof'
# instance won’t show the new style of output
>>> miles = JackRussellTerrier("Miles", 4)
>>> miles.speak()
'Miles says Arf'
#accessing the parent class from inside a method of a child class by using super():

class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return super().speak(sound)
#output reflecting the new formatting in the Dog class.
>>> miles = JackRussellTerrier("Miles", 4)
>>> miles.speak()
'Miles barks: Arf'
#Create a GoldenRetriever class that inherits from the Dog class.
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"
#Create a class called GoldenRetriever that inherits from the Dog class
class GoldenRetriever(Dog):
    def speak(self, sound="Bark"):
        return super().speak(sound)






        
