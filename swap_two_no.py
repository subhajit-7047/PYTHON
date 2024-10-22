##Input function by defualt return string --->>.

a=input("Enter value of a:")
b=input("Enter value of b:")
temp=a 
a=b
b=temp
#This is not consider
#Example:
#print("a=" ,a) This not working because(data type is sting) no concatenate because when is data type-->(int) it is apply :
#print("a=" a) This not working because no concatenate:


#in case not "a" string and also by  default a is string:
print("a=" +a)
print("b=" +b)
###  input_function always by default return a string:::



#true
# ##in this case a nad b data type is int --->>
# #That's wht write this print("a=" ,a)--- --->> ...
# a=1
# b=2
# temp=a 
# a=b
# b=temp
# print("a=" ,a)
# print("b=" ,b)