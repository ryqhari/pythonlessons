

# Enter operation: "add"/ "subtract"
# if operation is "add"
# enter a: 
# enter b
# a + b
# if operation is "subtract":
# 8 - 10
# anything else
# 8 * 10
operation = input("Enter operation('add'/'subtract'): ")
a = int(input("Enter a: "))
b = int(input("Enter b: "))

if operation == "add":
    print(a + b)
elif operation == "subtract":
    print(a - b)
else:
    print(a * b)