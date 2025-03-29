string="how are you?"
L=[]
for i in string.split():
    print(i.capitalize()) #capitalize() method is used to convert the first character of the string to uppercase and the rest to lowercase.
    L.append(i.capitalize())
    
print(L)
print(" ".join(L)) #join() method is used to join the elements of the list into a single string, with a space as the separator.
#
# Output:How Are You?