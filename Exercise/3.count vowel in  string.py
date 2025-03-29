check_vowel=input("Enter a string:")

count=0

vowels="AEIOUaeiou"

for i in check_vowel:
    if i in vowels:
        count+=1

print(count)