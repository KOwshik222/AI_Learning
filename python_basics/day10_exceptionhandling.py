#🧾 Summary Table
#Exception	When it happens
#ValueError	wrong input type
#ZeroDivisionError	divide by zero
#TypeError	wrong data types
#IndexError	wrong list index
#KeyError	wrong dictionary key
#FileNotFoundError	file missing
#NameError	variable not defined
#AttributeError	wrong method
#mportError	module missing
#"in python we have inbuilt error handling so we just need to declare them in catch"
try:
    a= int(input("enter a number"))
    b = 0
    print(a/b)
except:
    print("zero division error")


try:
    num = int(input("Enter number: "))
    result = 10 / num

except ValueError:
    print("Invalid input")

except ZeroDivisionError:
    print("Cannot divide by zero")

else:
    print(result)


