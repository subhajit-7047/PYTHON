#true love calculation-->

name_1=input('Enter is your name:')
name_2=input('Enter is his/her name:')

combine_string=name_1+name_2
lower_case_string=combine_string.lower()

t=lower_case_string.count('t')
r=lower_case_string.count('r')
u=lower_case_string.count('u')
e=lower_case_string.count('e')
true=t+r+u+e

l=lower_case_string.count('l')
o=lower_case_string.count('o')
v=lower_case_string.count('v')
e=lower_case_string.count('e')
love=l+o+v+e

love_score=int(str(true) + str(love)) #ans is int because in if statement love_score must be in integer then it is compair with 10.string is not compair with the int that's why it is covert in int,

if love_score <10 or love_score >90:
    print(f'your score is {love_score} and you go together like coke and mentos.')
elif love_score >= 40 and love_score<=50:
    print(f'your score is {love_score} and you are alright together.')
else:
    print(f'your score:{love_score}')