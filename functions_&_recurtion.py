# my name is vipul
# marks = [65, 76, 49, 80]
# percentage = ((sum(marks)/400)*100)
# print(f"your percentage are {percentage}%")


# def my_function(f):
#   print(f + " Refsnes")

# my_function("Emil")
# my_function("Tobias")
# my_function("Linus")



# no argument no return concept 
# def message():
#   print("hello python")

# message()

# with agrument no return concept
# def vipul(a,b):
#   c = (a+b)
#   print(c)
# user1 = int(input("Enter first number: "))
# user2 = int(input("Enter second number: "))
# vipul(user1,user2)

# no argument with return
# def add():
#   a = int(input("Enter a number: "))
#   b = int(input("Enter a number: "))
#   c = (a+b)
#   return c

# e = add()  
# print(e)

# with argument with return

# def add(a,b):
#   c = (a+b)
#   return c
# user1 = int(input("Enterr a number: "))
# user2 = int(input("Enterr a number: "))
# f =add(user1,user2)
# print(f)


# this code is from comment section of code with harry
# code for how to find the sum of natural numbers


# n = int(input("Enter any numberer: "))
# def sum(n):
#   if n==1:
#     return 1
#   return n + sum(n-1)
# num = sum(n)
# print("THe sum of natural numbers: ", num)

# this code is from website
# def findsum(n):
#   sum =0
#   x = 1
#   while x <=n :
#     sum = sum +x
#     x = x +1
#   return sum

# n = 5
# print(findsum(n))

# to find the biggest number 
# user1 = int(input("Enter your number: "))
# user2 = int(input("Enter your number: "))
# user3 = int(input("Enter your number: "))
# def Smallest(a,b,c):
#   if a<b:
#     if a<c:
#       return(a)
#     else:
#       return(c)
#   else:
#     if b<c:
#       return(b)
#     else:
#       return(c)

# d= Smallest(user1,user2,user3)    
# print(f"Smallest number is ***{d}***")



# # sum of natural number using recurtion

# n = int(input("Enter a natural number: "))
# def sum(n):
#     if n==1:
#         return 1
#     else:
#         return n + sum(n-1)
# x = sum(n)
# print(x)


# def greatest(num1,num2,num3):
#     if num1>num2:
#         if num1>num3:
#             return num1
#         else:
#             return num3
#     else:
#         if num2>num3:
#             return num2
#         else:
#             return num3
# user = greatest(22,34,56)
# print(user,"is the greatest of three numbers given")


# inch to cm converter


# def inch(cm):
#     return float(cm*2.54)

# user = int(input("Enter your number: "))
# i = inch(user)
# print(user,"inch is equal to ",i, "centimeter")


# 

# n = 6
# for i in range(n):
#     print('*'*(n-i))


def remove_and_split(string, word):
    newstr = string.replace(word, "")
    return newstr.strip()

this = "    harry is good     boy "
n = remove_and_split(this, "harry")
print(n) 