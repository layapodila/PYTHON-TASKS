'''1. Create a list of 10 elements of four different data types like int, string, complex and float.'''

list = [1,3.45,2+3j,"katie", 3, 4.5,4+3j,"Nancy",6,2.13]

print(list)

'''2. Create a list of size 5 and execute the slicing structure'''

list = [1,2,3,4,5]
print(len(list))
print(list[:])
print(list[::-1])
print(list[::2])
print(list[2:])

'''3. Write a program to get the sum and multiply of all the items in a given list.'''

list = [1,2,3,4,5]
print(sum(list))                  ##sum of the list
##multiplication of the list
list = [1,2,3,4,5]
count = 1
for i in list:
    count=count*i
print(count)

'''4. Find the largest and smallest number from a given list.'''

list = [5,4,8,19,20]             
print(max(list))                       ##largest number
print(min(list))                       ##smallest number

'''5. Create a new list which contains the specified numbers after removing the even numbers from a
predefined list.'''

list = [1,2,3,4,5,6,7,8]
list = [x for x in list if x%2 != 0]
print(list)

'''6. Create a list of elements such that it contains the squares of the first and last 5 elements between
1 and30 (both included).'''

list = []
for i in range (1,31):
    list.append(i**2)
print(list[:5])
print(list[-5:])
    
'''7. Write a program to replace the last element in a list with another list.'''

list1 = [1,3,5,7,9,10]
list2 = [2,4,6,8]
list1[-1:] = list2
print(list1)

'''8. Create a new dictionary by concatenating the following two dictionaries:'''

a={1:10,2:20}
b={3:30,4:40}
a.update(b)
print(a)

'''9. Create a dictionary that contain numbers in the form(x:x*x) where x takes all the values between 1
and n(both 1 and n included).'''

dict1 = {}
n = 5
for i in range(1, n+1):
    dict1[i] =i*i
print(dict1)

'''10. Write a program which accepts a sequence of comma-separated numbers from console and
generates a list and a tuple which contains every number in the form of string.'''

num = 34,67,55,33,12,98
list = num.split(" , ")
tuple = tuple(list)
print("list:", list)
print("Tuple:", tuple)
