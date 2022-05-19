# class vs object
# declare the class 

class Product:
    # constructor
    def __init__(self,name, price):
        self.name = name
        self.price = price

    def printIt(p):
        print("Product:" ,p.name, p.price)
# create some object
p1 = Product.init("OS", 100)

p2 = Product.init("Antivirus", 50)
 
p3 = Product.init("Game", 10)

Product.printIt(p1)
Product.printIt(p2)
Product.printIt(p3)


############### Code Split ##################
############### 1. Provider #################
class ClassName:
    # class ;structure
    pass


############### 2 Consumer ##################

obj1 = ClassName()
obj2 = ClassName()

#....

objN = ClassName()