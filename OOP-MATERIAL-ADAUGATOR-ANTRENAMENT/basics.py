# PascalCaseClassName
# 1. Box (properties/methods())
# 2. Factory -> create -> objects

# declare a class

class Human:
    pass

# create objects of type Human 

h1 = Human()
h1.name = "John"
h1.age  = 30

h2 = Human()
h2.name = "Ana"
h2.age = 25

print(h1.name, h1.age)
print(h2.name, h2.age)




# 4 independent boxes 
# h1_name
# h1_age
# h2_name
# h2_age

# 2 independent boxes
# h1
#   .name
#   .age

# h2
#   .name
#   .age   
