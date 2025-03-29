"""
*
**
***
****
*****
"""
rows= int(input("Enter thr number of rows:"))

# for i in rows:[Error:'int' object is not iterable]
for i in range(1,rows+1):
    for x in range(0,i):
        print("*",end=" ")
    print("")
   
