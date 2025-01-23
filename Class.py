class Car:
    nameOfCar="default"
    kindOfCar="default"
    colorOfCar="default"
    valueOfCar=100.00
    def desc(self):
        descString="%s is a %s in %s with cost of %f" %(self.nameOfCar,self.kindOfCar,self.colorOfCar,self.valueOfCar)
        return descString

carObj=Car()
print(f"Name of the Car is : {carObj.nameOfCar} \t Kind of the car is : {carObj.kindOfCar} \t color of the car is : {carObj.colorOfCar} \t cost of the car is : {carObj.valueOfCar}")

#Exercise
# We have a class defined for vehicles. Create two new vehicles called car1 and car2. Set car1 to be a red convertible worth $60,000.00 with a name of Fer, and car2 to be a blue van named Jump worth $10,000.00.
car1=Car()
car1.nameOfCar="Fer"
car1.kindOfCar="convertible"
car1.colorOfCar="red"
car1.valueOfCar=60000.00

car2=Car()
car2.nameOfCar="Jump"
car2.kindOfCar="van"
car2.colorOfCar="blue"
car2.valueOfCar=10000.00

print(car1.desc())
print(car2.desc())

#__init__ method allows you to customize the initialization of your objects. It helps you:

#    Set default values for instance variables.
#   Ensure that each instance of the class is initialized with the necessary data.
#    Encapsulate initialization logic, such as validating input or processing data when the object is created.

class NumberHolder:

   def __init__(self, number):
       self.number = number

   def returnNumber(self):
       return self.number

var = NumberHolder(7)
print(var.returnNumber()) #Prints '7'

print("--------------This is from Class.py ----------------")