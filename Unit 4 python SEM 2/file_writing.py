file = open("demo_file.txt", "w")
file.write("Hello! This is the first line in the file.\n")
file.write("Python file handling demonstration.\n")
file.close()

print("Data written Successfully. \n")

file = open("demo_file.txt", "r")
content = file.read()
print(content)
file.close()

file = open("demo_file.txt", "a")
file.write("Data appended to the file successfully. \n")
file.close()    

file = open("demo_file.txt", "r")
content = file.read()
print(content)
file.close()