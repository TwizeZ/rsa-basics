from math import pow, gcd


































































































#Felix Larsson
#TEINF20
#22-04-2022
#RSA Encryption Application

def egcd(a, b):
	x,y, u,v = 0,1, 1,0
	while a != 0:
		q, r = b//a, b%a
		m, n = x-u*q, y-v*q
		b,a, x,y, u,v = a,r, u,v, m,n
		gcd = b
	return gcd, x, y

def encrypt():
	
	x = int(input("Enter message you'd like to encrypt [x]: ")) 

	# Loop checking for a valid answer in r.
	while True:
		r = int(input("Enter value for [r]: "))

		# If given number is greater than 1
		if r > 1:

			# Iterate from 2 to n / 2
			for i in range(2, int(r/2)+1):

				# If num is divisible by any number between
				# 2 and n / 2, it is not prime
				if (r % i) == 0:
					print(f"{r} is not a prime number. Please input a prime number.")
					break
			else:
				print("Valid answer.")
				print()
				break

		else:
			print(f"{r} is not a prime number. Please input a prime number.")
			continue
	
	# Loop checking for a valid answer in q.
	while True:
		q = int(input("Enter value for [q]: "))

		# If given number is greater than 1
		if q > 1:

			# Iterate from 2 to n / 2
			for i in range(2, int(q/2)+1):

				# If num is divisible by any number between
				# 2 and n / 2, it is not prime
				if (q % i) == 0:
					print(f"{q} is not a prime number. Please input a prime number.")
					break
			else:
				print("Valid answer.")
				print()
				break

		else:
			print(f"{q} is not a prime number. Please input a prime number.")
			continue
	
	# Loop for checking for a valid answer in e.
	while True:
		e = int(input("Enter value for [e]: "))

		m = (r-1) * (q-1)

		if e > 1 and e < m:
			
			if gcd(e, m) == 1:
				pass
			
			else:
				print(f"Greatest common divisor of {e} and {m} is not 1. Please input a different integer.")
				continue

			print("Valid answer.")
			print()
			break
		else:
			print(f"{e} is not a number within the limit of 1 and {m}.")
			continue

	bgcd, a, b = egcd(e, m)
	d = a
	if d < 0:
		d = (m + d)
	else:
		pass

	# Formel för att beräkna den offentliga nyckeln
	n = r * q
	
	def encrypt(me):
		# en = pow(me,e)
		# y = en % n
		y = (x**e) % n
		print(f"Encrypted value is {y}")
		return y
	
	print(f"[d] = {d}")
	print(f"Original message was {x}.")
	y = encrypt(x)



def decrypted():
	y = int(input("Enter message you would like to decrypt [y]: "))

		# Loop checking for a valid answer in r.
	while True:
		r = int(input("Enter value for [r]: "))

		# If given number is greater than 1
		if r > 1:

			# Iterate from 2 to n / 2
			for i in range(2, int(r/2)+1):

				# If num is divisible by any number between
				# 2 and n / 2, it is not prime
				if (r % i) == 0:
					print(f"{r} is not a prime number. Please input a prime number.")
					break
			else:
				print("Valid answer.")
				print()
				break

		else:
			print(f"{r} is not a prime number. Please input a prime number.")
			continue
	
	# Loop checking for a valid answer in q.
	while True:
		q = int(input("Enter value for [q]: "))

		# If given number is greater than 1
		if q > 1:

			# Iterate from 2 to n / 2
			for i in range(2, int(q/2)+1):

				# If num is divisible by any number between
				# 2 and n / 2, it is not prime
				if (q % i) == 0:
					print(f"{q} is not a prime number. Please input a prime number.")
					break

			else:
				print("Valid answer.")
				print()
				break

		else:
			print(f"{q} is not a prime number. Please input a prime number.")
			continue

	# Loop for checking for a valid answer in e.
	while True:
		e = int(input("Enter value for [e]: "))

		m = (r-1) * (q-1)

		if e > 1 and e < m:
			
			if gcd(e, m) == 1:
				pass
			
			else:
				print(f"Greatest common divisor of {e} and {m} is not 1. Please input a different integer.")
				continue

			print("Valid answer.")
			print()
			break
		else:
			print(f"{e} is not a number within the limit of 1 and {m}.")
			continue
	
	bgcd, a, b = egcd(e, m)
	d = a
	if d < 0:
		d = (m + d)
	else:
		pass

	# formel för att beräkna den offentliga nyckeln
	n = r * q
	
	def decrypt(me):
		# en = pow(me,e)
		# x = en % n
		x = (y**d) % n
		print(f"Decrypted value is {x}")
		return y

	print(f"[d] = {d}")
	print(f"Encrypted value was {y}.")
	x = decrypt(y)



def main():
	while True:
		choice = input("Would you like to [1] encrypt, or [2] decrypt?: ")
		if choice == "1":
			encrypt()
			break
		elif choice == "2":
			decrypted()
			break
		else:
			print("That is not an option!")
			continue
	
	print("Would you like to enter another value? [yes, no]")
	another = input(">> ")
	if "yes" in another:
		main()
	else: 
		print("Terminating application...")

if __name__ in "__main__":
	
	main()