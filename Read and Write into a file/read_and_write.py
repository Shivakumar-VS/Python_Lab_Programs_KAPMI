text = input("Enter the data to be written in the file: ")

file = open("abc.txt","w")
file.write(text)
file.close()

file = open("abc.txt","r")
data = file.read()
print("Data in the file is: ", data)
file.close()

print("Data read from the file successfully")
print(data)