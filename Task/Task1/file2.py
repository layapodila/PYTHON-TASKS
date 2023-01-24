##1. Write a program in Python to perform the following operation:

number = int(input("Enter the number "))
if number%3 == 0 and number%5 ==0:
   print("cosultadd-python training")
elif number % 5 == 0:
     print("python training")
else:
      print("consultadd")



##3. Write a program in Python to implement the given flowchart:

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


##4. Write a program in Python to break and continue if the following cases occurs:

while True:
    num = int(input("Enter the number: "))
    if num<0:
        print("it's over")
        break
    if num>0:
        print("keep going")
        continue

##5. Write a program in Python which will find all such numbers which are divisible by 7 but are not a
##multiple of 5, between 2000 and 3200.

for i in range(2000, 3200):
    if (i%7==0) and (i%5!=0):
        print(i)

##6. What is the output of the following code examples?

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

##7. Write a program that prints all the numbers from 0 to 6 except 3 and 6.

for i in range(6):
    if i == 3 or i==6:
        continue
    print(i, end = ' ')
print("\n")

##8. Write a program that accepts a string as an input from the user and calculate the number of digits
##and letters.

string = "Hello 123"
count1 = 0
count2 = 1
for i in string:
    if i.isdigit():
        count1 += 1
    count2 += 1
print("no.of digits ", count1)
print("no.of letters ", count2)
    