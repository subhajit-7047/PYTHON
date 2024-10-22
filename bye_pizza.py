size=input("What size pizza you want(s/m/l)? ")
bill=0
if size== "s" or size== 'S':
    bill+=100
    print(f"small pizza is {bill} Rs.")
elif size=='m' or size=='M':
    bill+=200
    print(f"medium pizza is {bill} Rs.")
else:
    bill+=300
    print(f"large piza is {bill} Rs.")

add_peperoni= input('Do you want peperoni(y/n)? ')
if add_peperoni=='y' or add_peperoni=='Y':
    if size=='s' or size=='S':
        bill+=30
    else:
        bill+=50

extra_cheese=input("Do you want extra cheese(y/n)? ")
if extra_cheese=='y' or extra_cheese=='Y':
    bill+=20
print(f"your final bill is {bill}.")


#output:
#What size pizza you want(s/m/l)? l
# large piza is 300 Rs.
# Do you want peperoni(y/n)? y
# Do you want extra cheese(y/n)? y
# your final bill is 370.
