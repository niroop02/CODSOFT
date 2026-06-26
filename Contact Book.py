contacts = {}

while True:
	print("\n===== CONTACT BOOK =====")
	print("1. Add Contact")
	print("2. View Contacts")
	print("3. Search Contact")
	print("4. Update Contact")
	print("5. Delete Contact")
	print("6. Exit")
	
	choice = input("Enter your choice(1-6): ")
	
	if choice == "1":
		name = input("Enter Name: ")
		phone = input("Enter Phone Number: ")
		
		if name in contacts:
			print("Contact already exists!")
		else:
			contacts[name] = phone
			print("Contact Added Successfully!")
			
	elif choice == "2":
		if len(contacts) == 0:
			print("No contacts found.")
		else:
			print("\n--- Contact List ---")
			for name, phone in contacts.items():
				print("Name:", name, "|Phone:", phone)
	
	elif choice == "3":
		search_name = input("Enter Name to Search: ")
		
		if search_name in contacts:
			print("Contact Found")
			print("Name:", search_name)
			print("Phone:", contacts[search_name])
		else:
			print("Contact not found. ")
			
	elif choice == "4":
		update_name = input("Enter Name to Update: ")
		
		if update_name in contacts:
			new_phone = input("Enter New Phone Number: ")
			contacts[update_name] = new_phone
			print("Contact Updated Successfully!")
		else:
			print("Contact not found.")
			
	elif choice == "5":
		delete_name = input("Enter Name to Delete: ")
		
		if delete_name in contacts:
			del contacts[delete_name]
			print("Contact Deleted Successfully!")
		else:
			print("Contact not found.")
			
	elif choice == "6":
		print("Thank you for using Contact Book!")
		break
		
	else:
		print("Invalid Choice! Please try again.")
	
		
				
				
    