#basic structure 
student = {
    "name" : "koushik",
    "age" : 22,
}
print(student)
#accessing values
student = {
    "name": "koushik",
    "age": 22
}
print(student["name"])
#changing values
student = {
    "name": "koushik",
    "age" : 22
}
student["age"] = 23
print(student)
#adding new data
student = {
    "name": "koushik",
    "age" : 22
}
student["city"] = "hyderabad"
print(student)
# remove
student = {
    "name": "Koushik",
    "age": 22,
    "city": "Hyderabad"
}

student.pop("city")

print(student)
