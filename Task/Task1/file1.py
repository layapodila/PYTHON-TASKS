##1. Create three variables in a single line and assign values to them in such a manner that each one of
#them belongs to a different data type.

a,b,c = 1,2.01,'string'
print(a)
print(b)
print(c)

##2. Create a variable of type complex and swap it with another variable of type integer.

complex = 2+3j        #complex number
num = 1               #integer
complex,num = num,complex
print(num)
print(complex)

##3. Swap two numbers using a third variable and do the same task without using any third variable.
#1st method
n1 = 2
n2 = 3
print('before swapping:', n1)
print('before swapping:', n2)
t = n1
n1 = n2
n2 = t
print('after swapping:',n1)
print('after swapping:',n2)

#2nd method
n1 = 2
n2 = 3
print('before swapping:', n1)
print('before swapping:', n2)
n1,n2 = n2,n1
print('after swapping:',n1)
print('after swapping:',n2)


#5. Write a program to complete the task given below:
#Ask users to enter any 2 numbers in between 1-10 , add the two numbers and keep the sum in
#another variable called z. Add 30 to z and store the output in variable result and print result as the
#final output.

n1 = int(input("Enter the first number b/w 1 and 10: "))
n2 = int(input("Enter the second number b/w 1 and 10: "))
z = (n1+n2)
result = z+30
print(result)

#6. Write a program to check the data type of the entered values.

n1 = 3                          ## integer type
n2 = 3.45                       ## float
n3 = "hello"                    ## string
n4 = 3+3j                       ## complex
n5 = [1,2,3,4]                  ## list
n6 = {n1:1,n2:2}                ## dict
n7 = (1,2,3,4)                  ## tuple
n8 = {"lisa", "katie", "kathy"} ## sets
print(type(n1))              
print(type(n2))
print(type(n3))
print(type(n4))
print(type(n5))
print(type(n6))
print(type(n7))
print(type(n8))

##7.Create Variables using formats such as Upper CamelCase, Lower CamelCase, SnakeCase and
#UPPERCASE. 

my_var = 15           ## snake_case
MyVar = 10            ## UpperCamel
myVar = 12            ## lowerCamel
MYVAR = 14            ## UPPERCASE

##8.8. If one data type value is assigned to ‘a’ variable and then a different data type value is assigned to ‘a’
#again. Will it change the value? If Yes then Why?

answer-yes it will change the value because python is dynamically typed programming language
