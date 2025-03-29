def calculateGmean(a,b): # define the function
    mean=(a*b)/(a+b)
    print(mean)

def isGreater(a,b): # define the function
    if a>b:
        print("a is greater.")
    elif a==b:
        print("a and b is equal.")
    else:
        print("b is Graeter.")

a=int(input("Enter the value of a :"))
b=int(input("Enter the value of b :"))
calculateGmean(a,b) #call the function 
isGreater(a,b)  #call the function 
 