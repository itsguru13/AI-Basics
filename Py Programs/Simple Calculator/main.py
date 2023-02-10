a = int(input("Enter first number: "))
b = int(input("Enter first number: "))

case = input("'A'ddition, 'S'ubtraction, 'M'ultiplication, 'D'ivision? ").upper()
if(case == "A"):
    result = a+b
elif(case == "S"):
    result = a-b
elif(case == "M"):
    result = a*b
elif(case == "D"):
    result = a/b

print(f"Result: {result}")
