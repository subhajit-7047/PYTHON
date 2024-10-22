#syntax: round(nimber,no. of bit ) number of bits= point after value.
# That should be int and float number are consider.


print(round(7)) # 7 is integer that's why return only 7

print(round(7,2))  # 7 This ia also int

print(round(7.41)) # 7

print(round(2.6666,2))
#2.67 =>.67 because n0. of bits are 2

print(round(2.6657,0))
# 3.0

print(round(7.5)) # This float and return(7 or 8) nearest even inerger is 8.
#o/p: 8

print(round(6.5))#return(6 or 7) nearest even integer is 6

print(round(674,2)) # 674

print(round(674,0))#674

print(round(674,-1))##check = 10^-(no, of digit)
#output: 670 [return (670 and 680)]
print(round(674,-2))
#700
#This case -2 means two zero and 6 is check 7 are greater than of 5 or not 
# in this case 7 is greater than of 5 that why 6 is become 7.

print(round(674,-3))
#1000
print(round(674,-4))
#0

print(round(665,-1))
#660 return even only

print(round(675,-1))
#680

print(round(-8/3) )
#-3

print(round(-1.5))
#-2(closest even number return)

print(round( -8/3,2))
#(-2.67) 

print(round(7.66666,2))
#7.67