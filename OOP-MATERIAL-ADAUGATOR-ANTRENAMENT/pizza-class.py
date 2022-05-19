# PizzaRestaurant() -> class
# pizza - > object
# pizza prep -> __init()__



# WHEN PizzaRestaurant() -> class
# 1. new [object]
# 2. PizzaRestaurant() [object]
# 3. [object] ---> self ---> __init()__
# 4. custom initialization 

class PizzaRestaurant:
    def __init__(self):
        self.salt = 10
        self.cheese = "Parmesan"
        self.tomatos = 100
        
# 3 var       3 objects
pizza_mike  = PizzaRestaurant()
pizza_ana   = PizzaRestaurant()
pizza_marry = PizzaRestaurant()