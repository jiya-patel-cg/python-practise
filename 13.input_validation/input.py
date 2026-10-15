#1
# num = int(input("enter the num"))
# if 0<=num<=100:
#     print("valid marks")
# else:
#     print("invalid marks")

# #2
# num = int(input("enter the num"))
# if num>=0:
#     print("accepted number")
# else:
#     print("unaccepted number")

#3
# age = int(input("enter the age"))
# if 0<=age<=120:
#     print("accept age")
# else:
#     print("error")

# #4
# num = int(input("Enter your choice: "))

# match num:
#     case 1:
#         print("view profile")
#     case 2:
#         print("Edit profile")
#     case 3:
#         print("settings")
#     case 4:
#         print("Exits")
#     case _ :
#         print("Invalid Input")

#5
# password = input("enter the at least 8 character")
# if len(password)>=8:
#     print("valid password")
# else:
#     print("error")

#6
# temp = int(input("enter the temp"))
# if -20<=temp<=45:
#     print("accepted temp")
# else:
#     print("not accepted")

#9
# num = int(input("enter the num"))
# if num%3==0 or num%5==0:
#     print("accepted number")
# else:
#     print("not accepted")

# 11.
# while True:
#     num = int(input("Enter number : "))
#     if 10 <= num <= 50:
#         print("Accepted:", num)
#         print("Even" if num % 2 == 0 else "Odd")
#         break
#     else:
#         print("Invalid! Must be between 10 and 50.")

# # 12.
# balance = 2000
# while True:
#     deposit = int(input("Enter deposit amount: "))
#     if deposit > 0:
#         balance += deposit
#         print("Deposit successful! New balance:", balance)
#         break
#     else:
#         print("Invalid! Deposit must be positive.")

# # 13.
# while True:
#     num = int(input("Enter integer (1-100): "))
#     if 1 <= num <= 100:
#         print("Accepted number:", num)
#         break
#     else:
#         print("Invalid! Must be between 1 and 100.")


# # 14.
# while True:
#     marks = int(input("Enter marks (0-100): "))
#     if 0 <= marks <= 100:
#         if marks >= 75:
#             print("Result: Distinction")
#         elif marks >= 60:
#             print("Result: First Class")
#         elif marks >= 35:
#             print("Result: Pass")
#         else:
#             print("Result: Fail")
#         break
#     else:
#         print("Invalid! Enter between 0 and 100.")
# # 15.
# while True:
#     username = input("Enter username: ").strip()
#     password = input("Enter password: ").strip()
    
#     if len(username) >= 5 and " " not in username and len(password) >= 8 and password != "":
#         print("Login successful!")
#         break
#     else:
#         print("Invalid! Username ≥5 chars, no spaces. Password ≥8 chars.")


# # 16.
# while True:
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))
#     operator = input("Enter operator (+, -, *, /): ")
    
    
    
#     if operator == "+":
#         print("Result:", num1 + num2)
#     elif operator == "-":
#         print("Result:", num1 - num2)
#     elif operator == "*":
#         print("Result:", num1 * num2)
#     elif operator == "/":
#         print("Result:", num1 / num2)
#     break

# # 17.
