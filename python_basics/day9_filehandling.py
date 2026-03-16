#opening a file
#file = open("filename", "mode")
#. Reading a File

file = open("data.txt", "r")

content = file.read()

print(content)

file.close()

#5. Reading File Line by Line
file = open("data.txt", "r")

for line in file:
    print(line)

file.close()



#6. Writing to a File
file = open("data.txt", "w")

file.write("Hello Python\n")
file.write("Learning AI\n")

file.close()


#7. Appending to a File

#Append means adding data without deleting old data.

file = open("data.txt", "a")

file.write("Day 9 completed\n")

file.close()
#8. Best Method (Using with)

with open("data.txt", "r") as file:
    content = file.read()
    print(content)


#9. Example Program (Reading Numbers)

#If file contains:

10
20
30
40

#Program:

total = 0

with open("numbers.txt", "r") as file:
    for line in file:
        total += int(line)

print("Sum:", total)
