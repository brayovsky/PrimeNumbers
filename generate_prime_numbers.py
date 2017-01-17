#function to generate prime numbers between 0 and a given number

#ALGORITHM
"""
1. Iterate through 0 to number n, call each number between 0 and n, y
2. Iterate from 2 to (y/2)-1 and check the modulus of each number with y
3. If modulus = 0, break. If modulus is always above 0, add the number y to a return list
"""

# def generate_prime_numbers(last_number):
# 	print("called")	
# 	list_of_prime_numbers = []
# 	start_number = 2
# 	while (start_number<last_number):
# 		for divisor in range(2,start_number):
# 			print (divisor)
# 		start_number+=1

def determine_prime_number(number):
	
	#2 is a special case prime number
	#the loop can only contain numbers whose truncated  value is more than 1, 
	#therefore introduce special case for 1 and 3
	if(number==2 or number ==3):
		print("Prime number")
		return ""
	elif(number==1):
		print("Not prime number")
		return""
	else:
		half_number = int(number/2)+1
		for divisor in range(2,half_number):
			#if any modulus is equal to zero break, not prime
			#if no modulus is equal to zero, it is prime
			if(number%divisor==0):
				print ("Not prime number")
				break
			#see if loop has reached last number
			if(divisor==half_number-1):
				print("Prime number")


determine_prime_number(5)
determine_prime_number(4)
determine_prime_number(3)
determine_prime_number(1)
# generate_prime_numbers(5)