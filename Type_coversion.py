#"When I take input, it will be returned as a string, but I can convert the user input to another data type using type conversion."

#Ex:

frist_num=input("Enetr 1st number:") #input return as a str
second_num=input("Enetr 2nd number:")#input return as a str
print(frist_num)
print(second_num)
result=frist_num+second_num
print(result)
#output
#frist_num=40
#second_num=6
#406  because concatenate two string(Ex: subhajit + roy= subhajitroy ,34+35=3435(as string))

#for number it is wrong because no addition in two number
#___________________________________________________________________________
#__________________________________________________________________________


#Thats why string(for number) convert in integer using type-conversin::--->>

# two types of type conversion-->>
#1.implicit type conversion.(not perfrom for string)
#2.Explicit type conversion.(not perfrom for string)

#1.implicit type conversion.
# =>Implicit type conversion, also known as automatic type conversion or type coercion, is when a programming language automatically converts one data type to another without explicit instruction from the programmer.

x = 5   # integer
y = 2.5 # float

result = x + y
print(result)  # Output: 7.5


x=5    #integer
y=2+3j #complex
result = x + y
print(result)  # Output: (7+3j)

x = 2.5 # float
y=2+3j #complex
result = x + y
print(result)  # Output: (4.5+3j)
#-----------------------------------------------------------------
#-----------------------------------------------------------------


#Explicit type conversion, also known as type casting, is when a programmer manually converts one data type into another. This is done using specific functions or methods provided by the programming language. Unlike implicit conversion, explicit conversion requires a clear instruction from the developer to ensure that the type change happens.

#In Python, you can use functions --> like int(), float(), str(), bool(),list(),complex(),tuple(), dict().

# for explicit type conversion. Here’s an example:
x = "10"    # string
y = int(x)  # explicitly converting string to integer

print(y)    # Output: 10


#-------------------------
x = 1    # int
y = float(x)  # explicitly converting integer to float

print(y)    # Output: 1.0
#-------------------------

x = 134    # int
y = str(x)  # explicitly converting integer to string

print(y)    # Output: '134'
#---------------------------
x = 1    # int
y = bool(x)  # explicitly converting integer to boolean

print(y)    # Output: True
#--------------------------------
x = 1    # int
y = complex(x)  # explicitly converting integer to complex

print(y)    # Output: 1+0j
#------------------------------
x = "subahjt"    # str
y = list(x)  # explicitly converting str to list

print(y)    # Output: ['s', 'u', 'b', 'a', 'h', 'j', 't']
#----------------------------------->> 
# ##This is wrong this type of string value are not convert in int-->.
# x = "subahjt"    # str
# y = int(x)  # explicitly converting str to list

# print(y) 
# #output will be error.

#------------------------------------------------------
#--------------------------------------------------------------------
#type convertion is not a parmanent operation(sloution):->
#Beacuse a=4  and i use str() function it will be convert in string but then i print = ptint(x)---> output will be print 4 . beacuse a=4 is her original value.

x = 3    # int
y = float(x)  # explicitly converting int to  str 

print(y) # Output: as a float 3.0
# but i will print print(a)-->
print(x)
# output 3

#--------------------------------------------------- #-------------------------------------------------------
#example of code::

frist_num=input("Enetr 1st number:") #input return as a str
second_num=input("Enetr 2nd number:")#input return as a str

result=int(frist_num)+int(second_num)
print(result)

##output
#Enetr 1st number:2
#Enetr 2nd number:3
#5
#---------------------------------------------------------

#example of code::
#It is best beacuse(For mathematical opertion) always input are genarate int -- Then after  not use this function--
frist_num=int(input("Enetr 1st number:") )#input return as a int
second_num=int(input("Enetr 2nd number:"))#input return as a int

result=(frist_num)+(second_num)
print(result)

##output
#Enetr 1st number:2
#Enetr 2nd number:3
#5

#---------------------------------------

number=input('Enter two number:') #12345

frist_num=number[0] #only access 1 
second_num=number[1] # only access 2

print(frist_num+ second_num)#by default frist and second num is string type -->
#output #12

#--------------

number=input("enter two number:")# enter 4157

frist_num=int(number[0])#4
second_num=int(number[1])#1

print(frist_num+ second_num)#4+1=5
#output
#5
#-------------------------





