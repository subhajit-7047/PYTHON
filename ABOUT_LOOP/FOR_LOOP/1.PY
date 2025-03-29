name="subhajit"

for i in name:
    print(i)
# #output:------->
# s
# u
# b
# h
# a
# j
# i
# t

#-----------------------

name="swadesh"

for i in name:
    print(i)
    if i=="w":
        print("This is somthing special!")
#output
# s
# w
# This is somthing special!
# a
# d
# e
# s
# h
#-----------------------------

#for list

colors=["RED", "GREEN","YELLOE","BLUE","BLACK"]

for x in colors:
    print(x)
# RED
# GREEN
# YELLOE
# BLUE
# BLACK

#--------------------------
colors=["RED", "GREEN","YELLOE","BLUE","BLACK"]

for x in colors:
    print(x, end=" ")
#ouput   
#RED GREEN YELLOE BLUE BLACK