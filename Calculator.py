import math

def calculator():
	while True:
		print("\n===== CALCULATOR =====")
		print("1. Addition")
		print("2. Subtraction")
		print("3. Multiplication")
		print("4. Division")
		print("5. Modulus")
		print("6. Power")
		print("7. Floor Division")
		print("8. Square Root")
		print("9. Exit")
		
		choice = input("Enter your choice (1-9): ")
		
		if choice == '9':
			print("Calculator Closed.")
			break
			
		elif choice == '8':
			num = float(input("Enter a number: "))
			if num >= 0:
				print("Square Root =", math.sqrt(num))
			else:
				print("Cannot find square root of a negative number.")
				
		elif choice in ['1', '2', '3', '4', '5', '6', '7']:
			num1 = float(input("Enter first number: "))
			num2 = float(input("Enter second number: "))
			
			if choice == '1':
				print("Result =", num1 + num2)
				
			elif choice == '2':
				print("Result =", num1 - num2)
				
			elif choice == '3':
				print("Result =", num1 * num2)
				
			elif choice == '4':
				if num2 != 0:
					print("Result =", num1 / num2)
				else:
					print("Error! Division by zero.")
					
			elif choice == '5':
				if num2 != 0:
					print("Result =", num1 % num2)
					
			elif choice == '6':
					print("Result =", num1 ** num2)
					
			elif choice == '7':
				if num2 != 0:
					print("Result =", num1 // num2)
				else:
					print("Error! Division by zero.")
					
		else:
			print("Invalid Choice! Please try again.")
			
calculator()
						
					
			  