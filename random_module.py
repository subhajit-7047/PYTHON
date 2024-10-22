#-----------------> RANDOM MOUDLE <------------------
# => The random module in Python is a built-in module that provides a suite of functions to generate pseudo-random numbers and perform random operations. Here are some key features and functions of the random module:

#1.Generating Random Numbers:
    # random.random(): Generates a random float number between 0.0 and 1.0.
    # random.randint(a, b): Returns a random integer between a and b (inclusive).
    # random.uniform(a, b): Returns a random float number between a and b.
    # ramdom.range(a,b)

#2.Random Choices and Sampling:
    # random.choice(seq): Returns a random element from a non-empty sequence.
    # random.choices(population, weights=None, k=1): Returns a list with k random elements from the population, with optional weights.
    # random.sample(population, k): Returns a list of k unique elements chosen from the population.

#3.Shuffling Data:
    #random.shuffle(seq): Shuffles the sequence in place.

#4.Seeding:
    # random.seed(a=None): Initializes the random number generator. If a is omitted or None, the current system time is used.

#5. Distributions:
    # random.gauss(mu, sigma): Generates a random float number based on the Gaussian distribution with mean mu and standard deviation sigma.
    # random.expovariate(lambd): Generates a random float number based on the exponential distribution with rate lambd

#-------------------------------------------------------------------

#1.Generating Random Numbers:-->

#(i)  # random.randint(a, b): Returns a random integer between a and b (inclusive)
    # in value return a<=x<=b 
    #Return random integer in range [a, b], including both end points.

import random #define frist and then use include functions:

a=random.randint(1,4)
print(a)
#output will be any number 1 to 4 no any sequence randomly
#4
#2
#1
#3
#----------------
L = ['subha', 'Arup', 'kartik']
# Generate a random index within the range of the list indices
random_index = random.randint(0, len(L) - 1) #len(L)-1 means => The expression 0, len(L) - 1 is used to define the range of valid indices for a list L
# Use the random index to get an element from the list
name=random_index
print(name) #### this return index
name = L[random_index] # that means access the in the  name/items.
print(name) #### this is return random name(string/item).
#-------------
name=input("Enter everybody's name spareted by space:")#subhajit swadesh tarak suman
name_list=name.split(' ')
length=len(name_list)
random_choice=random.randint(0,length-1)#The expression 0, length - 1 is used to define the range of valid indices for a list name_list.
print(f'{name_list[random_choice]} will pay the bill')
#output:will be
#tarak will pay the bill
#subhajit will pay the bill
#tarak will pay the bill  #repeat  are allow
#tarak will pay the bill
#suman will pay the bill
#--------------

L = ['subha', 'Arup', 'kartik']
random_index = random.randint(0, len(L) - 1)
print(L[random_index])



random_int = random.randint(1, 10)
print("Random integer between 1 and 10:", random_int)
#Random integer between 1 and 10: 1
#Random integer between 1 and 10: 3
#Random integer between 1 and 10: 4
#Random integer between 1 and 10: 6 .................

# 1 এবং 10 এর মধ্যে একটি র্যান্ডম পূর্ণসংখ্যা তৈরি করুন
random_int = random.randint(1, 10)
print("1 এবং 10 এর মধ্যে র্যান্ডম পূর্ণসংখ্যা:", random_int)
#----------------------------
#(ii) ramdom.range(a,b)  # a<=x<b

a=random.randrange(1,3)
print(a)
#output will be 1 to 2 (1<=a<b)
#2
#1

#-------------------------------
#(iii)  random.random(): Generates a random float number between 0.0 and 1.0.
a=random.random()
print(a)
#0.6648252479638302 any floating number between 0.0 to 1.0
#0.6675419392081925
#0.5178696852107485
#0.7910005779027423
#0.40402961116599
#0.8883780121440245
#...................
random_float = random.random()
print("Random float between 0.0 and 1.0:", random_float)
#Random float between 0.0 and 1.0: 0.9053077175546831

# 0.0 এবং 1.0 এর মধ্যে একটি র্যান্ডম ফ্লোট সংখ্যা তৈরি করুন
random_float = random.random()
print("0.0 এবং 1.0 এর মধ্যে র্যান্ডম ফ্লোট সংখ্যা:", random_float)
#----------------------------------
#(iv) random.uniform(a, b): Returns a random float number between a and b.

a=random.uniform(1,3)
print(a)
#1.312682816175396
#1.7722719008270786
#.................
random_uniform = random.uniform(5.0, 10.0)
print("Random float between 5.0 and 10.0:", random_uniform)
#Random float between 5.0 and 10.0: 9.567041218450141 ..........

# 5.0 এবং 10.0 এর মধ্যে একটি র্যান্ডম ফ্লোট সংখ্যা তৈরি করুন
random_uniform = random.uniform(5.0, 10.0)
print("5.0 এবং 10.0 এর মধ্যে র্যান্ডম ফ্লোট সংখ্যা:", random_uniform)
#--------------------------------------------------------------------------------------

#2.Random Choices and Sampling:------------>>

#random.choice(seq): 

# Choose a random element from a list
random_choice = random.choice(['apple', 'banana', 'cherry'])
print("Random choice from list:", random_choice)
#cherry
#banana
#banana # repeate are allow
#apple

L=[1,2,8,-4777,'subha']
a=random.choice(L)
print(a)
#1
#8
#2
#-4777
#-4777
#8
#subha
#1...........................

# একটি তালিকা থেকে একটি র্যান্ডম উপাদান নির্বাচন করুন
random_choice = random.choice(['apple', 'banana', 'cherry'])
print("তালিকা থেকে র্যান্ডম নির্বাচন:", random_choice)
#-------------------------------------------------------


#3.Shuffling Data:
    #random.shuffle(seq): Shuffles the sequence in place.

L=[1,2,8,-4777,'subha']
random.shuffle(L)
print(L)
#[-4777, 2, 1, 'subha', 8]
#[2, 1, -4777, 8, 'subha']
#[-4777, 8, 1, 2, 'subha']
#[-4777, 8, 'subha', 2, 1]...................

# একটি তালিকা এলোমেলো করুন
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print("এলোমেলো তালিকা:", my_list)
#এলোমেলো তালিকা: [1, 4, 3, 5, 2]
#এলোমেলো তালিকা: [5, 2, 3, 1, 4]
#এলোমেলো তালিকা: [3, 2, 1, 4, 5]....................

#------------------------------------------------------------------------------

#5. Distributions:
    # random.gauss(mu, sigma): Generates a random float number based on the Gaussian distribution with mean mu and standard deviation sigma.
    # random.expovariate(lambd): Generates a random float number based on the exponential distribution with rate lambd


random_gauss = random.gauss(0, 1)
print(random_gauss)
#0.16182560126736728
#-0.9798673431686564 
#-1.4285609538144892
#0.993473045481878
#------------------------------------------------------------------------------------

