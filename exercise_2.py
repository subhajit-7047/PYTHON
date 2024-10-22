#Wap to find out how many year, days,months,weeks. we have left if we  live until90 year old.
 

age=int(input("Enter your age:")) #25
year_left= 90 - age
months_left=year_left*12
weeks_left=year_left*52
days_left=year_left*365
print(f"you have {year_left} years ,  {days_left} days,{weeks_left} weeks,{months_left} months left.")
#o/p:
#you have 65 years ,  23725 days,3380 weeks,780 months left.