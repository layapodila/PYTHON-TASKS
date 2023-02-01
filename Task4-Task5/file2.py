'''1. Write a program in Python to find out the character in a string which is uppercase using list
comprehension.'''

s1 = input("enter the string ")
lst =[i for i in s1 if i.isupper()]          ##list comprehension
print(lst)

'''2. Write a program to construct a dictionary from the two lists containing the names of students and
their corresponding subjects. The dictionary should map the students with their respective subjects.
Let’s see how to do this using for loops and dictionary comprehension.'''

##1st method
students = ['Smit', 'Jaya', 'Rayyan']                        
subjects = ['CSE', 'Networking', 'Operating System']
dict1 = {students[i]:subjects[i] for i in range(len(students))}   ##using dictionary
print("Result of the dictionary is", dict1)

##2nd method using zip function

students = ['Smit', 'Jaya', 'Rayyan'] 
subjects = ['CSE', 'Networking', 'Operating System']
dictionary = dict(zip(students,subjects))
print(dictionary)

#3rd method using for loop

students = ['Smit', 'Jaya', 'Rayyan'] 
subjects = ['CSE', 'Networking', 'Operating System']
dictionary = {}
for i in range(len(students)):
    key = students[i]
    value = subjects[i]
    dictionary[key] = value
    
print(dictionary)

'''3.'''


'''4. Write a program in Python using generators to reverse the string.'''

