

def calculator(num1,num2):
    if calculate == '+':
        return num1 + num2
    elif calculate == '-':
        return num1 - num2
    elif calculate == '*':
        return num1 * num2
    elif calculate == '/': 
        return num1 / num2
    

num1 = int(input("Enter number: "))
calculate = input("Enter operator: ")
num2 = int(input("Enter number: "))

x = calculator(num1,num2)
print(x)








