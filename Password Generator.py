import random
import string

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
	characters = ""
	
	if use_upper:
		characters += string.ascii_uppercase
	
	if use_lower:
		characters += string.ascii_lowercase
	
	if use_digits:
		characters += string.digits
		
	if use_symbols:
		characters += string.punctuation
		
	if characters == "":
		return "Please select at least one character type."
		
	password = ""
	
	for i in range(length):
		password += random.choice(characters)
		
	return password
	
	
while True:
	print("\n========== PASSWORD GENERATOR ==========")
	print("1. Generate Password")
	print("2. Exit")
	
	choice = input("Enter your choice: ")
	
	if choice == "1":
		length = int(input("Enter password length: "))
		
		print("\nSelect character types:")
		upper = input("Include Uppercase Letters? (y/n): ").lower() == "y"
		lower = input("Include Lowercase Letters? (y/n): ").lower() == "y"
		digits = input("Include Numbers? (y/n): ").lower() == "y"
		symbols = input("Include Special Characters? (y/n): ").lower() == "y"
		
		password = generate_password(
		   length,
		   upper,
		   lower,
		   digits,
		   symbols
		   )
		   
		print("\nGenerated Password:")
		print(password)
		
		#Password Strength Check
		strength = 0
		
		if length >= 8:
			strength += 1
		if upper:
			strength += 1
		if lower:
			strength += 1
		if digits:
			strength += 1
		if symbols:
			strength += 1
			
		print("\n Password Strength:")
		
		if strength <= 2:
			print("Weak")
		elif strength <= 4:
			print("Medium")
		else:
			print("Strong")
			
	elif choice == "2":
		print("Exiting Password Generator...")
		break
		
	else:
		print("Invalid Choice! Please try again.")