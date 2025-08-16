# Create an empty dictionary
contacts = {}

# Input 5 contacts
for i in range(5):
    name = input(f"Enter name {i+1}: ")
    phone = int(input(f"Enter phone number for {name}: "))
    contacts[name] = phone

# Store all phone numbers in a list
phone_list = list(contacts.values())

# Display results
print("\nContact Directory:", contacts)
print("Phone Numbers List:", phone_list)

# Built-in functions
print("Total contacts:", len(contacts))
print("Maximum phone number:", max(phone_list))
print("Minimum phone number:", min(phone_list))
print("Sorted phone numbers:", sorted(phone_list))
