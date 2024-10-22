#Operators in Python:


#1.Arithmetic: +, -, *, /, %, **, //
             #higher to lower precedence
# ----->     #1.()
             #2. **(exponent ^) (right to left)
             #3. *,/,///,% (left to right)when same is come then * operator work frist then other
             #4. +,-(left to right)
print(5+2*3-1+10/5)
#output: 12.0
#---------------
#2.Comparison: ==, !=, >, <, >=, <=
#3.Logical: and, or, not
#4.Bitwise: &, |, ^, ~, <<, >>
#5.Assignment: =, +=, -=, *=, /=, %=, **=, //=
#6.Identity: is, is not
#7.Membership: in, not in

#------------------------------------------------------


#Arithmetic Operators
x = 5
y = 2
print(x + y)
#o/p : 7
print(x - y)
#o/p :3
print(x * y)
#o/p :10
print(x / y)
#o/p :2.5
print(x % y)
#o/p :1
print( x ** y)
#o/p :25

#This operator-- This called integer division :
# 1st it will covert other  data-type to integer like-- float ---> int , etc.
 # also called flow division 
print(x // y)
#o/p : 2   (5/2=2.5 but it genarate in int value)

#----------------------------------------------------------------

#Comparison Operators
print(x > y)
#o/p :True
print(x < y)
#o/p :False
print(x >= y)
#o/p :True
print(x <= y)
#o/p :False
print(x == y)
#o/p :False
print(x != y)
#o/p :True

#-----------------------------------------------------------------

#Logical Operators
x = True
y = False
print( x or y)# while one condition is true then return true .
#o/p :True
a,b=4,5
print(a<5 or b<4)# In this case one condition is true output is return is true.
#---------------
print(x and y)
#o/p :False

a,b=4,5
print(a<5 and b>4)#While both are condition true then output are true and both are false then both are false.
#output: true
print(a>10 and b<10)# one condition are flase that why output return false.
#output; false
#----------------
print(not x)
#o/p :False
print(not y)
#o/p :True

#-----------------------------------------------------------------
#Bitwise Operators
# => bitwise means frist number convert in binary number (bit) Ex:5 -> 0101
a=5 # 0101 
b=4 # 0100
print(a &b) # 0101 & 0100 => 0100(00=0. 01=0, 11=1,10=0)while both are 11 then return 1;
# output= 4
x = 2 #0010
y = 3 #0011
print(x & y) # AND
#o/p :2
#------------
print(x | y) # OR # 0010 | 0011 => 0101(00=0. 01=1, 11=1,10=1)while both are 11 ,01,10 then return 1 for bitwise or;
#o/p :3
#------------
print(2 ^ 3) # XOR # # 0010 ^ 0011 => 0001(00=0. 01=1, 11=0,10=1)while both are difference 01 ,10,then return 1 for bitwise xor;
#o/p :1
#------------
print(x >> 2) # Right Shift # formula= x>>n = x/2^n=2/2^2=0 output
#o/p :0
#------------
print(y << 3) # Left Shift ### formula= x<<n = x*2^n= 3*2^3=24 output
#o/p :24
#------------
print(~ x) # NOT/ complement   -(2+1)=-3
#o/p :-3
a=10
print(~a)# -(10+1)=-11
#output = -11

#-------------------------------------------------
#Assignment Operators

a = 3
print(a)
#o/p :3
a += 3   # a = a + 3
print(a)
#o/p :6
a -= 3   # a = a - 3
print(a)
#o/p :3
a *= 3   # a = a * 3
print(a)
#o/p :9
a /= 3   # a = a / 3
print(a)
#o/p :3.0
#============
#it is not use in python
# a++
# ++a
#-----------------------------------------------

#Identity Operators

#It depend on memory location ==> when memory location are same  then it is true;
#check the id of boject (object means=a,b...)
# => print(id(a))
# a=4
# b=5
# print(id(a))  id=137491706736712
# print(id(b))  id=137491706736744
# print(a is b) false
a = 3
b = 3
print(a is b) # this case it is not compaire the value it check the id/memory locatin of a and b then it is return true/false(same id=true and other wise false.)
#o/p :True

a = "Hello"
b = "Hello"
print(a is b)
#o/p :True

a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)
#o/p :False

a = "Hello-World"
b = "Hello-World"
print(a is b)
#o/p :False

print(a is not b)
#o/p :True

a=4
b=5
print(id(a)) #id=137713801797704
print(id(b)) #id=137713801797736
print(a is not b) #True

a=4
b=4
print(id(a)) #id=133894261993544
print(id(b)) #id=133894261993544
print(a is not b) #False

#-----------------------------------------------------------------

#Membership Operators
#in & not in

x = "Delhi"
print("D" in x)
#o/p :True

print("D" not in x)
#o/p :False

x = [1, 2, 3]
print(1 in x)
#o/p :True

print(5 in x)
#o/p :False

x = (1, 2, 3)
print(1 in x)
#o/p :True

print(5 in x)
#o/p :False


#========================================================================
