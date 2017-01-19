# PrimeNumbers
Contains a python project with a function for determining the number of prime numbers between zero and a given number.

# Files
1. generate_prime_numbers.py - Contains the main function generate_prime_numbers() which generates a list of prime numbers from 0 to a given number  
2. test_prime_numbers.py - Contains the test cases to test the function generate_prime_numbers(). 

# Asymptotic analysis of the function
The function scales very poorly as the size of the input increases. This is because given an input N, it loops through all numbers from 0 to N, 
and for each number loops through zero to half its value within the main loop.
The time taken for the function to complete increases exponentially as the size of the input increases. 
It also takes up much more memory to build a list containing numbers from zero to half the value of each of the input numbers  from 0 to the input number.
A larger input number would require more memory.

# Python version
Python 2.6.6