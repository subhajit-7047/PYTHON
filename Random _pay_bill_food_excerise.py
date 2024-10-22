# write a progaram which is select random name from a list of names and a person will have to pay for everybody food bill:
import random

name=input("Enter everybody's name spareted by space:")#subhajit swadesh tarak suman
name_list=name.split(' ')
length=len(name_list)#calculate the length of the list
random_choice=random.randint(0,length-1)##The expression 0, length - 1 is used to define the range of valid indices for a list name_list


print(f'{name_list[random_choice]} will pay the bill')
# print(name_list[random_choice],'will pay the bill')





