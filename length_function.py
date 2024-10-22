print(len("subhajit"))

print (len('subhajit roy'))
#output 12  (this 12 is integer not string)
#-----------------------------------------------

#length _function in only work for string not any int , flaot, complex--->>
#Example:

print(len(1364))#Error because data type is int -->
#TypeError: object of type 'int' has no len()

#--------------------------------------------------
length=len("subhajit roy")
print(length)
#---------------------------------------------------

length=len("subhajit roy")
print("hey you" + length+ "hello") #error
#becuse length data typr rrturn in integer type That's why-->
#we are know, string and integer are not concatenate ____>>(remember it)!

#-------------------------------------------------------
#It can  be solve using type conversation this function--> str().

length=len("subhajit roy")
print("hey you " + str(length)+ " hello")
#output: hey you 12 hello

#--------------------------------------------------