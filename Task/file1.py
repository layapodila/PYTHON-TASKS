 #1. Create a list of given structure and get the Access list as provided below:
#x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]

x = [100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]
print(x)

print(x[5][:4])
print(x[-3:-1])
print(x[::2])
print(x[::-1])
print(x[5][5][:1])
print(x[:0])


#2Create a list of thousand numbers using range and xrange and see the difference between each
#other.
r = range(1, 1000,1)
print(type(r))
len(r)

xr = xrange(1,1000,1)
type(xr)


##3. How Tuple is beneficial as compared to the list?

1. Tuples are immutable 2. The implication of iterations is comparatively Faster
3. Tuple data type is appropriate for accessing the elements 4.Tuple consumes less memory as compared to the list
5. Tuple does not have many built-in methods 6. In tuple, it is hard to take place.

#4.Write a program in Python to iterate through the list of numbers in the range of 1,100 and print
#the number which is divisible by 3 and is a multiple of 2.

for i in range(1, 100):
    if (i % 3 == 0) and (i % 2 == 0):
        print(i)
    

#5.5. Write a program in Python to reverse a string and print only the vowel alphabet if it exists in the
#string with their index.

string = "Hello World"
reverse_string = string[::-1]
for i in reverse_string:
    if i in "aeiouAEIOU":
        print(list(i), end = ' , ')


##6. Write a program in Python to iterate through the string “hello my name is abcde” and print the
##string which is having an even length.

string = "hello my name is abcde"
for word in string:
    if (len(word)%2==0):
        print(word)


##8.Create two lists such as even_list and odd_list
even_list = []
odd_list = []
# ask user to enter the number in between 1and50
number = int(input("Enter the number b/w 1 and 50: "))
for number in range(1,50):
    if number%2 == 0:
        even_list.append(number)
    else:
        odd_list.append(number)
print("even list are ", even_list)
print("odd lists are ", odd_list)


##9. Write a program to find out the occurrence of a specific character from an alphanumeric string.

s1 = '12abcbacbaba44'
print(s1.count('a'))       # occurrences of a
print(s1.count('b'))       # occurrences of b
print(s1.count('c'))       # occurrences of c


##10. Generate and print another tuple whose values are even numbers in the given tuple

tup = (1,2,3,4,5,6,7,8,9,10)
li = list()
tp2 = tuple(li)
for i in tup:
    if tup[i-1] % 2 == 0 :
        li.append(tup[i-1])
print(tp2)


