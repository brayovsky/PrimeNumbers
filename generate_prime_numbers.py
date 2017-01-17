#function to generate prime numbers between 0 and a given number

#ALGORITHM
"""
1. Iterate through 0 to number n, call each number between 0 and n, y
2. Iterate from 2 to (y/2)-1 and check the modulus of each number with y
3. If modulus = 0, break. If modulus is always above 0, add the number y to a return list
"""
# class  NegativeNumberError(Exception):
# 	def __init__(self, expression , message):
# 		self.message = message
# 		self.expression = expression
		

def generate_prime_numbers(last_number):
	if(type(last_number) != int):
		raise TypeError("Please pass an integer as a parameter")
	if(last_number<0):
		raise Exception("Please pass a positive integer")

	list_of_prime_numbers = []
	number = 0
	while (number<last_number):
		if(number==2 or number ==3):
			list_of_prime_numbers.append(number)
		elif(number==1 or number == 0):
			pass
		else:
			half_number = int(number/2)+1
			for divisor in range(2,half_number):
				#if any modulus is equal to zero break, not prime
				#if no modulus is equal to zero, it is prime
				if(number%divisor==0):
					break
				#see if loop has reached last number
				if(divisor==half_number-1):
					list_of_prime_numbers.append(number)
		number+=1
	return list_of_prime_numbers

generate_prime_numbers(-1)