#what is list =>Collection in Python for sequences of diverse data types
#A mutable list is a type of data structure that allows you to modify its elements after the list has been created. This means you can add, remove, or change items within the list without creating a new list. 
# list will be Homogeneous and Heterogeneous( same and different data type in a one list)
##Dynamicly memory allocatin in list

    #1.Create
    #2.Access
    #3.Edit
    #4.Add
    #5.Delete
    #6.Operations
    #7.Functions
#-----------------------------
#Arrays vs. Lists in Memory:
#Arrays:

    #int arr[50]; ---> 50 contiguous memory blocks.
    #Elements stored in binary form at consecutive addresses.
#Lists:

    #list_example = [1, 2, 3] ---> Elements at different locations.
    #Stores references/pointers to elements, not the values.




#---------------------------------
##
##List Characteristics:

    #Ordered
    #Mutable
    #Heterogeneous
    #Duplicates allowed
    #Dynamic size
    #Nesting supported
    #Indexable
    #Any object type




#--------------------------------
# Array vs list


#                Array                      |               List            
#-------------------------------------------|--------------------------------------------------------
# 1.   Homogeneous => all data type are same| 1. Heterogeneous => can be different data
#     Ex: [1|2|3|4|5]=> all int data type   |    type. Ex: Homogenous list=[1,2,3,4] //same data type
#     Ex: [s|u|b|h|a]=> all char data type  |          Ex: Heterogeneous list= ["subha",4,5.7,True,1+3j]
#  -----------------------------------------|--------------------------------------------------------                  
#  2. Contiguous memory: computation fast   | 2.Non-contiguous memory:  
#     because all are items are homogenous. |
#     Data type same.                       |
#  -----------------------------------------|---------------------------------------------------------
#  3.  Fast:   computation fast             | 3.  computation slow because data type are different
#      because all are items are homogenous.|
#      Data type same                       |
#   ----------------------------------------|---------------------------------------------------------
#   4.  Numerical/Scientific use.           |4. Programmer-friendly; General-purpose.
#   ----------------------------------------|---------------------------------------------------------
#   5. Not flexible and difficult to modify |5.flexible and easy to modify
#   ----------------------------------------|----------------------------------------------------------
#   6. needs a loop to access the           |                                                                           
#      component of array                   | 6.no need a loop to access the components
#  -----------------------------------------|---------------------------------------------------------
#  7.less more memory consumption           |7. more memory consumption.
#  ----------------------------------------------------------------------------------------------------
#   
# 
# 
# ------------------------------------
# 1.CREATE LIST:

L=[]
print(L) #[] # empty list                                 

#Homogeneous => all data type are same:
L1=[1,2,3,4]
print(L1) #[1, 2, 3, 4]

#Heterogeneous => can be different data type:
L2=["subha",4,5.7,True,1+3j]
print(L2)# ['subha', 4, 5.7, True, (1+3j)]

### multi-diamensional list

#2D list:
L3=[1,2,3,[4,5]] # this Heterogeneous list because 1 2 3 is int and [4,5] is list
print(L3) #[1,2,3,[4,5]]

#3D
L4=[[[1,2],[3,4]],[[5,6],[7,8]]]
print(L4) #[[[1,2],[3,4]],[[5,6],[7,8]]]

#use type converstion:
L5=list("subhajit")
print(L5) #['s', 'u', 'b', 'h', 'a', 'j', 'i', 't']
#-------------------------------------------------------------
# positive index is start 0,1,2,3,.......
#Negative indx is start -1,-2,-2,-4,........ 
#print list--->
num=[1000,-29,69,3]
print(num)#[1000, -29, 69, 3]
print(num[-1])#3
print(num[1])#-29
print(num[-2])#69
#print(num[index:length])
print(num[0:4])#[1000, -29, 69, 3]
print(num[0:])#[1000, -29, 69, 3]#by default is it print upto list range
print(num[:])#[1000, -29, 69, 3] by start to end 
print(num[1:3])#[-29, 69]
#print(num[index:length:skip the step])
num=[1,2,3,4,5,6,7]
print(num[0:7:2])#[1, 3, 5, 7] 
print(num[0:7:3])#[1, 4, 7]
#--------------------------------------------------
# 2.how to Access:
#use positive index and negative index:

L1=[1,2,3,4]
print(L1[0]) #1
print(L1[-1]) #4 # return last item.
# Slicing
print(L1[1:3]) #[2, 3]
print(L1[::-1]) #[4, 3, 2, 1]# reverse the list.

L3=[1,2,3,[4,5]] # i want access item 4 how -->
print(L3[-1]) #[4, 5] return last item.
x=L3[-1]
print(x) #[4, 5]
print(x[0]) #4


#Easy to access item 4
print(L3[-1][0]) #4
print(L3[-1][-1]) #5


#find the item 7 ->
L4=[[[1,2],[3,4]],[[5,6],[7,8]]]
print(L4[-1][-1][0]) #7

print(L4[0][-1][-1]) #4

#use positive index->
print(L4[1][1][0]) #7
print(L4[0][1][1]) #4
#---------------------------------------

###3. How to edit item: ->

#A mutable list is a type of data structure that allows you to modify its elements after the list has been created. This means you can add, remove, or change items within the list without creating a new list. 

#list is mutable -> that why change the item/replace the item, add, remove


#Editing with index:

L1=[1, 2, 3, 4, 5]
L1[0]=100
print(L1) #[100, 2, 3, 4, 5]
# List in Python are Mutable:

L1[-1] = 500
print(L1) #[100, 2, 3, 4, 500]

## Editing With Slicing:->
L1[1:4] = [200, 300, 400]
print(L1) #[100, 200, 300, 400, 500]

#-----------------------------------------

#
# 4. Add-->

    #append()
    #extend()
    #insert()


  #append() ->  item add in last position in list. and list.append() takes exactly one argument
L1=[1, 2, 3, 4, 5]
L1.append(10000)
print(L1)#[1, 2, 3, 4, 5, 10000] 

L1=[1, 2, 3, 4, 5]
L1.append("subha")
print(L1)#[1, 2, 3, 4, 5, 'subha'] 

L1=[1, 2, 3, 4, 5]
L1.append([1000,'subha'])
print(L1)#[1, 2, 3, 4, 5, [1000, 'subha']]  #[1000, 'subha'] this treat as list and only cosider one item

#--------------------

   #extend() ->  item add in last position in list. and list.append() takes exactly multiple argument.
L2=[1, 2, 3, 4, 5]
L2.extend([1000,'subha','roy',50000])
print(L2)#[1, 2, 3, 4, 5, 1000, 'subha', 'roy', 50000]

L2=[1, 2, 3, 4, 5]
L2.extend("subha")
print(L2)#[1, 2, 3, 4, 5, 's', 'u', 'b', 'h', 'a']
#---------------------

  #insert() # item insert any places.and only one item
  #insert expected 2 arguments
L3=[1, 2, 3, 4, 5]
L3.insert(1,"subha")
print(L3)#[1, 'subha', 2, 3, 4, 5]# other shift in the right side.

L3=[1, 2, 3, 4, 5]
# L3.insert(1,2,"subha",'roy') # only cosider 2 argument
L3.insert(3,'kousik')
print(L3)#[1, 2, 3, 'kousik', 4, 5]
#----------------------------------
#mutable:->

L=[1,-9,4,2]
L[1]=20
print(L)#[1, 20, 4, 2] in list secific position it will replace the item.
#That's why list is mutable.

#more Example:
L1=[1,3,2,-3,-8445,73454]
#L1[index;length]-->
L1[1:4]=['subhajit','kumar','Roy']
print(L1)#[1, 'subhajit', 'kumar', 'Roy', -8445, 73454] #Mutable

#-----------------------------------------------------------------------

#5.DELETE:

    #  del
    # .remove()
    # .pop()
    # .clear()

  # del
L3=[1, 2, 3, 4, 5]
del L3[0] #frist item will be delete
print(L3) #[2, 3, 4, 5]

L5=[1,2,3,4,'subha',2,3,'s','u','m','a','n']
del L5[-3] # only delete 'm"
print(L5) #[1, 2, 3, 4, 'subha', 2, 3, 's', 'u', 'a', 'n']

L5=[1,2,3,4,'subha',2,3,'s','u','m','a','n']
del L5[-3:] #  but in this case delete 'm' 'a' 'n'
print(L5) #[1, 2, 3, 4, 'subha', 2, 3, 's', 'u'] 

#--------------
  # .remove()

L5=[1,2,3,4,'subha',2,3,'s','u','m','a','n']
L5.remove('subha') #In the bracket will pass the value/item.
print(L5) #[1, 2, 3, 4, 2, 3, 's', 'u', 'm', 'a', 'n']
#========->
L2=[1,2,3,4,5,60,2]# while multiple value/item are same in list 
L2.remove(2)# It will remove only start to frist pass item
print(L2)#[1, 3, 4, 5, 60, 2] 
#--------------
 # .pop()-> always only delete last item in the list.

L5=[1,2,3,4]
L5.pop()# delete item=4
print(L5)#[1, 2, 3]
#suppose i want to remove secific item in the list then pass the index
L5=[1,2,3,4]
L5.pop(1)#pass index=1
print(L5)#[1, 3, 4]

print(L5.pop(0)) #1 pop item print
print(L5)#[3, 4]

#-----------------

# .clear()--> it will delete all item in the entire list.

L5=[1,2,3,4,'subha',2,3,'s','u','m','a','n']
L5.clear() # all item are delete
print(L5) #[] 
#-------------------------------------------------------------------------
 #6.Operations

 
    # Arithmetic
    # Membership
    # Loop

L = [1, 2, 3, 4]
L1 = [5, 6, 7, 8]
# Concatenation/Merge
print(L + L1)#[1, 2, 3, 4, 5, 6, 7, 8] #It will be create a new list
#  no change the main list
print(L)#[1, 2, 3, 4]

print(L1)#[5, 6, 7, 8]

#----------------
L = [1, 2, 3, 4]
print(L * 3)#[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]

#-------------
# Loops:
L = [1, 2, 3, 4]
for i in L:
    print(i)
#output:
# 1
# 2
# 3
# 4

L3 = [1, 2, 3, [4, 5]]
for i in L3:
    print(i)

#output:
# 1
# 2
# 3
# [4, 5]
L3 = [1, 2, 3, [4, 5]]
print(4 in L3)#False # because 4 is not item in  main list
print([4, 5] in L3) #True # this case [4,5] this are as a item

#-------------------------------------------------------------------------

    #7.Functions
    
    # len()
    # min()
    # max()
    # sorted()
    #.index()


    # len()
L=[1,2,3,4,5]
print(len(L))#5

L3 = [1, 2, 3, [4, 5]]
print(len(L3))#4 because [4,5] as a one item

#---------------------
 # min()
L=[1,2,3,4,5]
print(min(L))#1

L=[1,2,0,4,5]
print(min(L))#0 return minimum value of entire list

#-------------------
# max()

L=[1,2,3,4,5]
print(max(L))#5

L=[1,2,2000,4,5]
print(max(L))#2000 # return max value of entire list
#-------------------

#sorted()

L=[1,4,5,3,6,2] # sort the all item
print(sorted(L))#[1, 2, 3, 4, 5, 6] # it is new list not parmanently change
print(L)#[1, 4, 5, 3, 6, 2] #no change   

print(sorted(L, reverse = True))#[6, 5, 4, 3, 2, 1] reverse the list
#--------------
# .sort()
L=[2,4,1,5,2,6,7]
L.sort()
print(L)#[1, 2, 2, 4, 5, 6, 7] 
#print(L.sort())#None because it is change original list that why return none


#mix-list are not allow -------->...
# L=[1,'subhajit',1.2,True]
# L.sort()
# print(L)#Error
#because on sorting time not compaire the str,int, flaot, bool , that why it return error.
#--------------------------------------------
# .reverse()
L.reverse()
print(L)#[7, 6, 5, 4, 2, 2, 1] 
#-------------------------
   #.index()
L=[1,4,5,3,6,2]  #return index of item
print(L.index(6)) # 4
#--------------------------------------------

