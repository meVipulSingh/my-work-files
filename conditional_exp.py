# a = 10

# if a==1:
#     if a>7:
#         print("Its not equal to 7")
# # elif a>36:
# #     print("The value is not greater than 6")
# # elif a!=7:
# #     print("The value is equal to 34")
# else:
#     print("It's a false statement")


# def func(a,b,c,d,):
#     print(a,b,c,d)


# args = [1,2,3,4]
# kwargs = {"a":1, "b":5, "c":7, "d": 4,}

# func(*args)


# age = int(input("Enter your age: "))

# if age>=18:
#     print("Yes you are eligible")
# else:
#     print("No try next time")


# age = int(input("Enter your age: "))

# if age>18:
#     print("yes you can work")

# else:
#     print("You cannot work")


# num1 =int(input("Enter number 1 here "))
# num2 =int(input("Enter number 2 here "))
# num3 =int(input("Enter number 3 here "))
# num4 =int(input("Enter number 4 here "))

# if (num1>num2):
#     f1 = num1
# else:
#     f1 = num2

# if (num3>num4):
#     f2 = num3
# else:
#     f2 = num4

# if (f1>f2):
#     print(f1," is greatest")

# else:
#     print(f2," is greatest")


# sub1 = int(input("Enter your chemestry marks: "))
# sub2 = int(input("Enter your maths marks: "))
# sub3 = int(input("Enter your physics marks: "))

# percentage = (sub1+ sub2+sub3)/3

# if percentage>=40:
#     print("Your percentage are",percentage,"You passed congratualtions")

# elif percentage==33:
#     print("Your percentage are",percentage,"Your're just passed")

# else:
#     print("Your percentage are",percentage,"You're failed")



# text = input("Enter your word: ")

# if ('make a lot of money' in text):
#     print("spam")
# elif ('click this' in text):
#     print("spam")
# elif ('subscribe this' in text):
#     print("spam")
# elif ('buy now' in text):
#     print("spam")

# else:
#     print("no spam")


# user = input("Enter your name: ")

# length = len(user)

# if length<10:
#     print("Contain less then 10 chracter")

# else:
#     print("Contain more then 10 chracter")

# user = input("Enter a name: ")

# names = ['vipul', 'akansha', 'shanaya', 'rhea']

# if user in names:
#     print(user,"is persent in the list")
# else:
#     print(user,"is not present in the list")


# sub1 = int(input("Enter your chemestry marks: "))
# sub2 = int(input("Enter your maths marks: "))
# sub3 = int(input("Enter your science marks: "))
# sub4 = int(input("Enter your hindi marks: "))

# a = (sub1+sub2+sub3+sub4)/4

# if a>90:
#     print(a,"Your marks are exilent")

# elif a>80:
#     print(a,"You got A")

# elif a>70:
#     print(a,"You got B")

# elif a>60:
#     print(a,"You got C")

# elif a>50:
#     print(a,"You got D")

# else:
#     print(a,"You failed")



user = input("Enter your word: ")

user=user.lower()

if 'vipul' in user:
    print("post talking about vipul")

else:
    print("no they are not")