1
# for i in range(5):
#     print("Hello")

# 2
# for i in range(1,10):
#     print(i, end=" ")

# 3
# for i in range(1,11):
#     print(i, end=" ")

# 4
# for i in range(10,0, -1):
#     print(i, end=" ")

# 5
# for i in range(5,50,5):
#     print(i)


# 6
# for i in range(2,20):
#     if i%2==0:
#         print(f"{i} is Even")
# 7
# for i in range(1,19):
#     if i%2==1:
#         print(f"{i} is Odd")
 #26
# for row in range(4):
#     for column in range(4):
#         print("*", end="")
#     print()

27
# for row in range(4):
#     for column in range(5):
#         print("*", end="")
#     print()

#28
for row in range(1, 5):
    for column in range(4,row-1,-1):
        print("*", end="")
    print("")
# b=int(input("Enter the number b"))
# for row in range("(*)",b):
#      for column in range("*", row + "*"):
#        print(column, end="")
#      print("")

# for i in range(5,0,-1):
#     print("*"*i)
# num=int(input("Enter the num:"))
# for i in range ("*",num ):
#     for j  in range("*",num-1):
#          print(" ", end="")
#     for k in range(1,i+1):
#      print("*",end="")
#     print()

# total=0
# flag=True
# grade="" 

# for i in range(5):
#    marks=int(input("Enter your marks"))
#    total+=marks
#    if marks<35:
#       flag=False

# if flag:
#    percentage=total/5
#    if percentage>=90:
#       grade="A+"
#    elif percentage>=80:
#       grade="A"
#    elif percentage>=70:
#       grade="B"
#    elif percentage>=60:
#       grade="C"
#    elif percentage>=50:
#       grade="D"
#    else:
#       grade="F"



# if flag==True:
#    print(total,percentage,grade)
#    print("Pass")
# else:
#    print("You're Fail")

# b=int(input("Enter the number b"))
# for row in range(5):
#      print()
#      for column in range(1):
#         print("*", end="")
# print("")

# row_number:5
# if row in range(5):
#     print()
# elif column in range(n-1):
#    print ("*")

# n=int(input("enter a number n"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
      
#         if i==n or j==n or j==1 or i==3 :
#            print("*",end="  ")
#         elif i==3 and j!=2 and j!=4:
#                print("*",end= "  ")
          
#         else:
#             print(end="   ")
#     print()


