#create

#empty tuple
T1=()

t2=(1,2,3,4,5,6,7,8,9,10)#homogeneous tuple

t3=(1,2,3,4,5,6,7,8,9,10.0,'Hello')#heterogeneous tuple
#2d tuple
t4=((1,2,3),(4,5,6),(7,8,9))#2d tuple
#3d tuple
t5=((1,2,3),(4,5,6),(7,8,9),(10,11,12))#3d tuple
#4d tuple
t6=((1,2,3),(4,5,6),(7,8,9),(10,11,12),(13,14,15))#4d tuple

#one item tuple
t7=(1)#single element tuple
print(type(t7))#<class 'int'>

#single element tuple
t8=(1,)#single element tuple
print(type(t8))#<class 'tuple'>

#create tuple using type converstion
t9=tuple('Hello')#convert string to tuple
print(t9)#('H', 'e', 'l', 'l', 'o')

#list to tuple
t10=tuple([1,2,3,4,5])#convert list to tuple
print(t10)#(1, 2, 3, 4, 5)  

#------------------

#ACCESS

T11=(1,2,3,3)
T11[0]#1st element of tuple
#output:1
T11[-1]#last element of tuple
#output:3
T11[0:3]#slice of tuple
#output:(1, 2, 3)
T11[0:3:2]#slice of tuple with step
#output:(1, 3)
T11[::-1]#reverse of tuple
#output:(3, 3, 2, 1)
#---------------------------
#EDIT
#tuple is immutable, so we cannot change the value of tuple
#T11[0]=10#TypeError: 'tuple' object does not support item assignment

#---------------------------
#delete tuple
T22=(6,54,5,6,4)
del T22[-1]
#TypeError: 'tuple' object doesn't support item deletion
#T22[-1]=10#TypeError: 'tuple' object does not support item assignment
#------------------------
#opertaion on tuple
T33=(1,2,3,4,5)
T44=(6,7,8,9,10)
T55=T33+T44#concatenate tuple
#output:(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

T66=T33*2#repeat tuple
#output:(1, 2, 3, 4, 5, 1, 2, 3, 4, 5)

T77=5 in T33#check element in tuple
#output:True

T88=5 not in T33#check element not in tuple
#output:False

for i in T33:#iterate tuple
    print(i)#1 2 3 4 5
#output:1 2 3 4 5


#-------------------------
#function on tuple

length=len(T33)#length of tuple
#output:5

T33.count(1)#count of element in tuple
#output:1

T33.index(1)#index of element in tuple

#output:0

min(T33)#minimum element in tuple
#output:1

max(T33)#maximum element in tuple
#output:5

sum(T33)#sum of element in tuple
#output:15

sorted(T33)#sort tuple
#output:[1, 2, 3, 4, 5]

#-------------------------

