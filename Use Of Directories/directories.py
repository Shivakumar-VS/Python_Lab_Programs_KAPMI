# python program to Demonstrate use of Dictionaries. 
# Creating a dictionary 
my_dict = { 
    "name": "vishva", 
    "age": 24, 
    "city": "INDIA" 
} 
# Accessing values in the dictionary 
print("Name:", my_dict["name"]) 
print("Age:", my_dict["age"]) 
print("City:", my_dict["city"]) 

# Adding a new key-value pair 
my_dict["email"] = "vishva@example.com" 

# Updating a value in the dictionary 
my_dict["age"] = 28 

# Removing a key-value pair 
del my_dict["city"] 

# Displaying all key-value pairs in the dictionary 
print("All key-value pairs in the dictionary:") 
for key, value in my_dict.items(): 
    print(key + ":", value) 

# Checking if a key exists in the dictionary 
if "email" in my_dict: 
    print("Email exists in the dictionary") 
else: 
    print("Email does not exist in the dictionary") 
# Clearing all key-value pairs in the dictionary 
my_dict.clear() 
print("Dictionary after clearing all key-value pairs:", my_dict)