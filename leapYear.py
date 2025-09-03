"""Home » Python Exercises » Python Basic Exercise for Beginners
Python Basic Exercise for Beginners
Updated on: April 30, 2025 | 519 Comments

This Python beginner’s exercise helps you quickly learn and practice basic skills by solving 23 coding questions and challenges, complete with solutions.

Immerse yourself in the practice of Python’s foundational concepts, such as loops, control flow, data types, operators, list, strings, input-output, and built-in functions. This beginner’s exercise is sure to elevate your understanding of Python.

Also, See:

Python Exercises: A set of 17 topic specific exercises
Python Quizzes: Solve quizzes to test your knowledge of fundamental concepts.
Python Basics: Learn the basics of Python to solve this exercise.
Beginner Python Interview Questions
What questions are included in this exercise?

This exercise contains 23 coding questions and challenges to solve, ranging from beginner to intermediate difficulty.
The hints and solutions are provided for each question.
Tips and essential learning resources accompany each question. These will assist you in solving the exercise and you’ll become more familiar with the basics of Python.
Use Online Code Editor to solve exercises.

This Python exercise covers questions on the following topics:

Python for loop and while loop
Python list, set, tuple, dictionary, input, and output
Also, try to solve the basic Python Quiz for beginners

+ Table of Content (23 Exercises)
Exercise 1: Calculate the multiplication and sum of two numbers
Given two integer numbers, write a Python program to return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.

Given 1:

number1 = 20
number2 = 30
Expected Output:

The result is 600
Given 2:

number1 = 40
number2 = 30
Expected Output:

The result is 70
Refer:

Accept user input in Python
Calculate an Average in Python
Show Hint
Show Solution
Exercise 2: Print the Sum of a Current Number and a Previous number
Write Python code to iterate through the first 10 numbers and, in each iteration, print the sum of the current and previous number.

Expected Output:

Printing current and previous number sum in a range(10)
Current Number 0 Previous Number  0  Sum:  0
Current Number 1 Previous Number  0  Sum:  1
Current Number 2 Previous Number  1  Sum:  3
Current Number 3 Previous Number  2  Sum:  5
Current Number 4 Previous Number  3  Sum:  7
Current Number 5 Previous Number  4  Sum:  9
Current Number 6 Previous Number  5  Sum:  11
Current Number 7 Previous Number  6  Sum:  13
Current Number 8 Previous Number  7  Sum:  15
Current Number 9 Previous Number  8  Sum:  17
Reference article for help:

Python range() function
Calculate sum and average in Python
Show Hint
Show Solution
Exercise 3: Print characters present at an even index number
Write a Python code to accept a string from the user and display characters present at an even index number.

For example, str = "PYnative". so your code should display ‘P’, ‘n’, ‘t’, ‘v’.

Expected Output:

Orginal String is  PYnative
Printing only even index chars
P
n
t
v
Reference article for help: Python Input and Output

Show Hint
Show Solution
Exercise 4: Remove first n characters from a string
Write a Python code to remove characters from a string from 0 to n and return a new string.

Given:

def remove_chars(word, n):
    # write your code

print("Removing characters from a string")
print(remove_chars("pynative", 4)) 
# output 'tive' first four characters are removed

print(remove_chars("pynative", 2)) 
# output 'native'
 Run
Note: n must be less than the length of the string.

Show Hint
Show Solution
Also, try to solve Python string exercises

Exercise 5: Check if the first and last numbers of a list are the same
Write a code to return True if the list’s first and last numbers are the same. If the numbers are different, return False.

Given:

numbers_x = [10, 20, 30, 40, 10]
# output True

numbers_y = [75, 65, 35, 75, 30]
# Output False
Show Hint
Show Solution
Exercise 6: Display numbers divisible by 5
Write a Python code to display numbers from a list divisible by 5

Expected Output:

Given list is  [10, 20, 33, 46, 55]
Divisible by 5
10
20
55
Show Hint
Show Solution
Also, try to solve Python list Exercise

Exercise 7: Find the number of occurrences of a substring in a string
Write a Python code to find how often the substring “Emma” appears in the given string.

Given:

str_x = "Emma is good developer. Emma is a writer"
Expected Output:

Emma appeared 2 times
Show Hint
Show Solution
Exercise 8: Print the following pattern
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5
Refer:

Print Pattern using for loop
Nested loops in Python
Show Hint
Show Solution
Exercise 9: Check Palindrome Number
Write a Python code to check if the given number is a palindrome. A palindrome number reads the same forwards and backward. For example, 545 is a palindrome number.

Expected Output:

original number 121
Yes. given number is palindrome number

original number 125
No. given number is not palindrome number
Refer: Python Programs to Check Palindrome Number

Show Hint
Show Solution

Solution 2:
Exercise 10: Merge two lists using the following condition
Given two lists of numbers, write Python code to create a new list containing odd numbers from the first list and even numbers from the second list.

Given:

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
Expected Output:

result list: [25, 35, 40, 60, 90]
Show Hint
Show Solution
Note: Try to solve the Python list exercises

Exercise 11: Get each digit from a number in the reverse order.
For example, If the given integer number is 7536, the output shall be “6 3 5 7“, with a space separating the digits.

Given:

number = 7536
# Output 6 3 5 7
Refer: Python Programs to Reverse an Integer Number

Show Hint
Show Solution
Exercise 12: Calculate income tax
Calculate income tax for the given income by adhering to the rules below

Taxable Income	Rate (in %)
First $10,000	0
Next $10,000	10
The remaining	20
Expected Output:

For example, suppose the income is 45000, and the income tax payable is

10000*0% + 10000*10%  + 25000*20% = $6000
Show Solution
Exercise 13: Print multiplication table from 1 to 10
The multiplication table from 1 to 10 is a table that shows the products of numbers from 1 to 10.

Write a code to generates a complete multiplication table for numbers 1 through 10.

Expected Output:

1  2 3 4 5 6 7 8 9 10 		
2  4 6 8 10 12 14 16 18 20 		
3  6 9 12 15 18 21 24 27 30 		
4  8 12 16 20 24 28 32 36 40 		
5  10 15 20 25 30 35 40 45 50 		
6  12 18 24 30 36 42 48 54 60 		
7  14 21 28 35 42 49 56 63 70 		
8  16 24 32 40 48 56 64 72 80 		
9  18 27 36 45 54 63 72 81 90 		
10 20 30 40 50 60 70 80 90 100
See:

Nested loops in Python
Create Multiplication Table in Python
Show Hint
Show Solution
Exercise 14: Print a downward half-pyramid pattern of stars
* * * * *  
* * * *  
* * *  
* *  
*
Refer:

Print Pattern using for loop
Nested loops in Python
Show Hint
Show Solution
Exercise 15: Get an int value of base raises to the power of exponent
Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.

Note here exp is a non-negative integer, and the base is an integer.

Expected output

Case 1:

base = 2
exponent = 5

2 raises to the power of 5: 32 i.e. (2 *2 * 2 *2 *2 = 32)
Case 2:

base = 5
exponent = 4


Exercise 18: Check if a given year is a leap year
A leap year is a year in the Gregorian calendar that contains an extra day, making it 366 days long instead of the usual 365. This extra day, February 29th, is added to keep the calendar synchronized with the Earth’s revolution around the Sun.

Rules for leap years: a year is a leap year if it’s divisible by 4, unless it’s also divisible by 100 but not by 400.
""" 

def leap(year):
  print(year %4 ==0 or year%100==0 and year%400 !=0 )

leap(2000)
