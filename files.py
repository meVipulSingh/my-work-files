# f = open("sample.txt",'w')
# f.write('hello this is vipul singh addadsddsd')
# # f.close()
# f = open('sample.txt')
# t = f.read()
# if 'twinkle' in t:
#     print("Twinkle present")
# else:
#     print("Twinkle not present")


# def game():
#     return 70

# score = game()

# with open("highscore.txt") as f:
#     highscore = int(f.read())

# if highscore<score:
#     with open("highscore.txt", 'w') as f:
#         f.write(str(score))



# for i in range(2,20):
#     with open(f"Tables/Multiplication Table of {i}.txt",'w') as f:
#         for n in range(1,11):
#             f.write(f"{i} x {n} = {i*n}\n")
          


# with open("sample.txt") as f:
#     content = f.read()
# content= content.replace('donkey', 'monkey')
# with open("sample.txt",'w') as f:
#     f.write(content)

# with open("sample.txt", 'w') as f:
#     f.write()

# my code to check if perticular string is present in file or not

# with open("sample.txt") as f:
#     containr = f.read()

# if 'twinkle' in containr:
#     print("Yes twinkle is present")
# else:
#     print("Twinkle is not present")

# for i in range(2,21):
#     with open(f"Tables/Multipication table of {i}.txt",'w') as f:
#         for l in range(1,11):
#             f.write(f"{i}x{l} = {i*l}\n")

# with open('log.txt') as f:
#     content =f.read().lower()


# if 'python' in content:
#     print("yes python is present ")


# from os import read

# x = ['bad', 'stupid', 'idiots']

# with open("sample.txt") as f:
#     content = f.read()
# for x in x:
#     content = content.replace(x, "none")

# with open("sample.txt", 'w') as f:
#     f.write(content)

# to copy any file to other file

file_1 = 'sample.txt' 
file_2 = 'this.txt' 


with open(file_1) as f:
    f1 = f.read()

with open(file_2) as f:
     f2 = f.read()
    
if f1 == f2:
    print("Its identical")
else:
    print("files arre non identical")