'''1. Write a program in Python to perform the following operation:'''

number = int(input("Enter the number "))
if number%3 == 0 and number%5 ==0:
   print("cosultadd-python training")
elif number % 5 == 0:
     print("python training")
else:
      print("consultadd")

'''2. Write a program in Python to perform the following operator based task:'''     

n1 = int(input("enter number1 "))
n2 = int(input("enter number2 "))
print("Enter 1 - Addition")
print("Enter 2 - subtraction")
print("Enter 3 - division")
print("Enter 4 - multiplication")
print("Enter 5 - average")

choice = int(input("enter the number"))

if choice == 1:
    addition = n1+n2
    print("addition of two numbers is", addition)
elif choice == 2 :
    subtraction = n1-n2
    print("subtraction of two numbers is", subtraction)
elif choice == 3:
    division= n1/n2
    print("division of two numbers is", division)
elif choice == 4:
    multiplication = n1*n2
    print("multiplication of two numbers is", multiplication)
elif choice == 5:
    avg = (n1+n2)/2
    print("avg of two numbers is", avg)
else:
    print("NEGATIVE")


'''3. Write a program in Python to implement the given flowchart:'''

a=10
b=20
c=30
avg = (a+b+c)/3
print(avg)
if avg>a and avg>b and avg>c:
    print("avg is higher than a, b,c")
elif avg>a and avg>b:
    print("avg is higher than a, b,c")
elif avg>a and avg>c:
    print("avg is higher than a,c")
elif avg>b and avg>c:
    print("avg is higher than b,c")
elif avg>a:
    print("avg is just higher than a")
elif avg>b:
    print("avg is just higher than b")
else:
    print("avg is just higher than c")


'''4. Write a program in Python to break and continue if the following cases occurs:'''

while True:
    num = int(input("Enter the number: "))
    if num<0:
        print("it's over")
        break
    if num>0:
        print("keep going")
        continue

'''5. Write a program in Python which will find all such numbers which are divisible by 7 but are not a
multiple of 5, between 2000 and 3200.'''

for i in range(2000, 3200):
    if (i%7==0) and (i%5!=0):
        print(i)
    else:
        print("entered number is not divisible by 7 and multiple of 5")

'''6. What is the output of the following code examples?'''

x = 123
for i in x:     
    print(i)
# ans is int object is not iterable

i = 0
while i < 5:
    print(i)
    i +=1 
    if i ==3:
        break 
    else:
        print("error")
# 0
#error
#1
#error
#2

'''7. Write a program that prints all the numbers from 0 to 6 except 3 and 6.'''

for i in range(6):
    if i == 3 or i==6:
        continue
    print(i, end = ' ')
print("\n")

'''8. Write a program that accepts a string as an input from the user and calculate the number of digits
and letters.'''

string = "Hello 123"
count1 = 0
count2 = 1
for i in string:
    if i.isdigit():
        count1 += 1
    count2 += 1
print("no.of digits ", count1)
print("no.of letters ", count2)

'''9. Read the two parts of the question below:
Write a program such that it asks users to “guess the lucky number”. If the correct number is
guessed the program stops, otherwise it continues forever.'''


import random
rn = random.randint(1,10)
while True:
    gn = int(input('Guess a number between 1 and 10 '))
    if rn==gn:
        print("well guessed!")
        break
    else:
        print("incorrect")
    
'''10. Write a program that asks five times to guess the lucky number. Use a while loop and a counter,
such as'''

counter = 1
while counter <= 5:
   number = input("Type in the " + str(counter) + " number ")
   if number != 5:
       print("Try again.")
   else:
       print("Good guess!")
   counter = counter +1
else:
   print("Game over")

'''11. In the previous question, insert break after the “Good guess!” print statement. break will terminate
the while loop so that users do not have to continue guessing after they found the number. If the user
does not guess the number at all, print “Sorry but that was not very successful”.'''


counter = 1
while counter <= 5:
   number = input("Type in the " + str(counter) + " number ")
   if number != 5:
       print("Try again.")
   else:
       print("Good guess!")
       break
   counter = counter +1 
else:
   print("Sorry but that was not very successful.")