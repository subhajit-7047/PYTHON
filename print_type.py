# #This the type of print::
# print("india", "pakistan","kolkata", "delhi")
# #out put
# #india pakistan kolkata delhi

# #any datatype with together
# print("india",5,True)
# #out put
# #india 5 True
# #

# #sep=' ' =>sepeter parameter as ex:space## by defualt exixts 
# print("india", "pakistan","kolkata", "delhi")#in this case output middle space genarate 
 
#  #i want /
# print("india", "pakistan","kolkata", "delhi",sep='/')
# #output
# #india/pakistan/kolkata/delhi

# print("india", "pakistan","kolkata", "delhi",sep='-')
# #output
# #india-pakistan-kolkata-delhi

# #####
# # in one line in help of end='' patameter => it exist end  by defualt end='\n' thats why automatically it print next line .
# print("hello")
# print("world")
# #output-->.
# #hello
# #world


# # in one line in help of end='' patameter => it exist end  by defualt end='\n' thats why automatically it print next line .
# print("hello",end=' ')
# print("world")
# #output
# #hello world



# print("i am beginner")
# print('print("i am cse student:")')
# print('Hello world')
# print("print('HI GUYS!')")

# # print('print('i am cse student')')// Error
# #  print("print("i am cse student:")")// Error

# ## STRING MANIPULATION:;

# print("hi" + "subhajit")# OUTPUT will bw : hisubhajit // no any space,
# print("hi" + " subhajit")#subhajit before sapace OUTPUT will be : hi subhajit
# print("hi " + "subhajit")#hi after sapace OUTPUT will be : hi subhajit.
# print("Hello" + " " + "subhajit")
# print("Hello world\nhello world\nHello world")

# #escape sequence characters:

# print("Hey I am a \"Good boy\" and this viwer is also good boy")
# #Hey I am a "Good boy" and this viwer is also good boy


# print("Hey I am a Good boy\nand this viwer is also good boy")
# #Hey I am a Good boy(next line)
# #and this viwer is also good boy


# #Seperate character

# print("Hey",  6,7 , sep='~')
# #Hey~6~7
# print("Hey",  6,7 , end='~')
# print('subhajit')
# #Hey 6 7~subhajit

# text="""Basic Syntax
# o Modules & PIP
# o Variables & Datatypes
# o Conditionals and Loops
# o Functions & Recursion
# o List, Tuple, Sets, Dictionaries
# o File I/O
# o If you prefer to l
# """
# print(text)

# ## using for we can print all character into the any text--.

# name="subhajit"
# for character in name:
#     print(character)

# # s
# # u
# # b
# # h
# # a
# # j
# # i
# # t


# ## strings slicing and operations on strings-->

# names="subhajit,Roy"
# print(names[0:5]) #slicing this string
# #subha


# names="subhajit,Roy"
# print(names[1:5]) #slicing this string
# #ubha

names="subhajit,Roy"
print(names[:6])
#subhaj

names="subhajit,Roy"
print(names[:]) 
#subhajit,Roy


names="subhajit,Roy"
print(len(names))
# print(names[0:len(names)-2])## it also valid syntax.
print(names[0:len(names)-2])
print(names[0:-2]) #12-2=10
#subhajit,R #have 10 no. of strings


names="subhajit,Roy"
print(names[-2:-1]) # len(names)-2:len(names)-1 => 12-2:12-1 =>10:11
print(names[10:11])
#o
