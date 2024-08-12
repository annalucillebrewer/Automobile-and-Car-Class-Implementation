#The automobile class holds general data about an automobile in inventory.

class Automobile:
    #The __init__ method accepts arguments for make, model, year, mile, and price
    #intiiliazes the dara attributes with these values

    def __init__(self, make, model, mileage, price):
        self.__make = make
        self.__model = model
        self.__mileage = mileage
        self.__price = price

    #the following methods are mutators for the class data attributes

    def set_make(self, make):
        self.__make = make

    def set_model (self, model):
        self.__model = model

    def set_mileage(self, mileage):
        self.__mileage = mileage

    def set_price (self, price):
        self.__price = price

    #the following methods are the accessors for the class data attributes
    def get_make(self):
        return self.__make
    
    def get_model(self):
        return self.__model

    def get_mileage(self):
        return self.__mileage

    def get_price(self):
        return self.__price

#the Car class represents a car. It is a subclass of Automobile class
class Car(Automobile):
    #the __init__ method accepts arguments for car's
    #make, model, mileage, price, AND, doors

    def __init__(self, make, model, mileage, price, doors):

        #that was a call to the superclass' __init__ method to pass arguments
        Automobile.__init__(self, make, model, mileage, price)

        #intiialize __doors attribute
        self.__doors = doors

    #the set_doors method is a mutator for doors attribute
    def set_doors(self, doors):
        self.__doors = doors

    #the get_doors method is the accesor for the doors attribute
    def get_doors(self):
        return self.__doors
    
    
        
        
    
        
