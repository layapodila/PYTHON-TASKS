'''1. Write a program to reverse a string.'''

string = "1234abcd"
reverse_string = string[::-1]
print(reverse_string)

'''2. Write a function that accepts a string and prints the number of uppercase letters and lowercase
letters.'''

def count_upper_lower(string1):
    upper_count = 0
    lower_count = 0
    for char in string1:
        if char.isupper():
            upper_count +=1
        elif char.islower():
            lower_count +=1
        else:
            pass
    print("No. of uppercase count is", upper_count)
    print("No.of lowercase count is", lower_count)
temp = input("Enter a string ")
print(count_upper_lower(temp))

'''3. Create a function that takes a list and returns a new list with unique elements of the first list.'''

def unique_list(numbers):
    x = []
    for item in numbers :
        if item not in x:
            x.append(item)
    return x

print(unique_list([1, 2, 3, 1, 4]))

'''4. Write a program that accepts a hyphen-separated sequence of words as input and prints the words
in a hyphen-separated sequence after sorting them alphabetically.'''

items=[n for n in input().split('-')]
items.sort()
print('-'.join(items))

'''5. Write a program that accepts a sequence of lines as input and prints the lines after making all
characters in the sentence capitalized.'''

lines = []
while True:
    l = input()
    if l:
        lines.append(l.upper())
    else:
        break
for l in lines:
    print(l)

'''6 Define a function that can receive two integral numbers in string form and compute their sum and
print it in the console.'''

def calculateSum(a,b):
    s = int(a)+int(b)
    return s
num1 = "10"
num2 = "20"
sum = calculateSum(num1,num2)
print('Sum =', sum)

'''7.Define a function that can accept two strings as input and print the string with the maximum length
in the console. If two strings have the same length, then the function should print both the strings line
by line.'''

def max_len(s1,s2):
	len1 = len(s1)
	len2 = len(s2)
	if len1>len2:
		print(s1)
	elif len2>len1:
		print(s2)
	else:
		print(s1)
		print(s2)
print(max_len("two","three"))


'''8.Define a function which can generate and print a tuple where the values are square of numbers
between 1 and 20 (both 1 and 20 included).'''

def printTuple():
	li=list()
	for i in range(1,21):                  # range b/w the 1 and 21
		li.append(i**2)                    # adding the square of numbers to the list
	print(tuple(li))                       # converting list into tuple
printTuple()


'''9.Write a function called showNumbers that takes a parameter called limit. It should print all the
numbers between 0 and limit with a label to identify the even and odd numbers'''

def showNumbers(limit):
    for i in range(0, limit):
        if i == 0:
            print(i,end=" ")
            print("EVEN")
        elif i%2 == 0:
            print(i, end=" ")
            print("EVEN")
        else:
            print(i, end=" ")
            print("ODD")
print(showNumbers(4))


'''10. Write a program which uses filter() to make a list whose elements are even numbers between 1
and 20 (both included)'''

x =(lambda i: i%2 == 0)                    #even numbers
list1 = list(filter(x, range(1,21)))       ## listing the even numbers using filter method  
print(list1) 


'''11.Write a program which uses map() and filter() to make a list whose elements are squares of even
numbers in [1,2,3,4,5,6,7,8,9,10].'''

li = [1,2,3,4,5,6,7,8,9,10]
even_num=list(map(lambda i : i**2 , filter(lambda i: i%2 == 0 , li)))
print(even_num)

'''12.Write a function to compute 5/0 and use try/except to catch the exceptions'''

def foo():
    try:
        numerator = 5
        denominator = 0

        result = numerator/denominator

        print(result)
    except:
        print("Error: Denominator cannot be 0.")
    
    finally:
        print("This is finally block.")
foo()

'''13.Flatten the list [1,2,3,4,5,6,7] into 1234567 using reduce().'''

list1 = [1,2,3,4,5,6,7]

from functools import reduce

list2 = reduce(lambda x,y: 10*x+y, list1)

print(list2)


'''14.'''

'''15. Write a program in Python to multiply the elements of a list by itself using a traditional function
and pass the function to map() to complete the operation.'''

def multiply(n):
    return n*n
my_list = [1,2,3,4,5]
updated_list = list(map(multiply,my_list))
print(updated_list)


'''16. What is the output of the following codes:'''

def foo():
    try:
        return 1
    finally:
        return 2
k = foo()
print(k)
##answer is 2


def a():
    try:
        f(x,4)
    finally:
        print('after f')
        print('after f?')
a()
## NameError: name 'f' is not defined