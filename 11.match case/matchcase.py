# # #Q1]

#
# num = int(input("Enter your choice: "))

# match num:
#     case 1:
#         print("You selected Pizza")
#     case 2:
#         print("You selected Burger")
#     case 3:
#         print("You selected Pasta")
#     case 4:
#         print("You selected Sandwich")
#     case _ :
#         print("Invalid Input")

# #Q2]


# numb = int(input("Enter your choice: "))

# match numb:
#     case 1:
#         print("Wi - Fi selected")
#     case 2:
#         print("Bluetooth selected")
#     case 3:
#         print("Mobile data selected")
#     case 4:
#         print("airplane mode selected")
#     case 5:
#         print("Exited!")
#     case _:
#         print("Invalid Input")

# #Q3]

# 
# numb = int(input("Enter your choice: "))

# match numb:
#     case 1:
#         print("Checking Balance")
#     case 2:
#         print("Withdrawing Money")
#     case 3:
#         print("Depositing Money")
#     case 4:
#         print("Changing PIN")
#     case 5:
#         print("Exited!")
#     case _:
#         print("Inavlid Input")

# #Q4]
# ligth = input("Enter the colour of Ligth at signal: ")

# match ligth:
#     case "red":
#         print("Stop")
#     case "yellow":
#         print("Wait")
#     case "green":
#         print("Go")
#     case _ :
#         print("Invalid Input")

# #Q5]
# numb = 1
# while numb != 5:

#     p

#     numb = int(input("Enter your choice: "))

#     match numb:
#         case 1:
#             print("Your Profile:")
#         case 2:
#             print("Courses:")
#         case 3:
#             print("Your Marks:")
#         case 4:
#             print("Your Attendance")
#         case 5:
#             print("Logged Out")
#         case _ :
#             print("Invalid Input")

# #Q6]

# 
# numb = int(input("Enter your choice: "))

# match numb:
#     case 1:
#         print("Electronics")
#     case 2:
#         print("Clothing")
#     case 3:
#         print("Books")
#     case 4:
#         print("Grocery")
#     case 5:
#         print("Exited!")

# #Q7]
# numb = 1
# while numb != 6:

#     
#     numb = int(input("Enter your choice: "))

#     match numb:
#         case 1:
#             print("Balance:")
#         case 2:
#             print("Mini Statement:")
#         case 3:
#             print("Fund Transfer:")
#         case 4:
#             print("Bill Payments")
#         case 5:
#             print("Customer Support")
#         case 6:
#             print("Exited!")
#         case _ :
#             print("Invalid Input")

# #Q8]
# numb = 1
# while numb != 5:



#     numb = int(input("Enter your choice: "))

#     match numb:
#         case 1:
#             print("Morning Show Details are as follows:")
#         case 2:
#             print("Afternoon Show Details are as follows:")
#         case 3:
#             print("Evening Show Details are as follows:")
#         case 4:
#             print("Night Show Details are as follows:")
#         case 5:
#             print("Exited!")
#         case _ :
#             print("Invalid Input")

# #Q9]

#
# numb = int(input("Enter your Weather: "))

# match numb:
#     case 1:
#         print("Wear Sunglasses")
#     case 2:
#         print("Carry an Umbrella")
#     case 3:
#         print("Weather may Change")
#     case 4:
#         print("Wear warm clothes")
#     case _:
#         print("Unkown Weather")

# #Q10]

# 
# numb = int(input("Enter your Payment method: "))

# match numb:
#     case 1:
#         print("UPI Payment selected")
#     case 2:
#         print("Card Payment selected")
#     case 3:
#         print("Cash Payment selected")
#     case 4:
#         print("Wallet Payment selected")
#     case _:
#         print("Invalid Payment method ")

# #Q11]

# 
# numb = int(input("Enter Extension: "))

# match numb:
#     case 1:
#         print("Document File")
#     case 2:
#         print("Image File")
#     case 3:
#         print("Image File")
#     case 4:
#         print("Audio File")
#     case 5:
#         print("Video File")
#     case _:
#         print("Unknown File Type")

# #Q12]

# 
# numb = int(input("Enter your role: "))

# match numb:
#     case 1:
#         print("Full Access")
#     case 2:
#         print("Teacher Dashboard")
#     case 3:
#         print("Student Dashboard")
#     case 4:
#         print("Limited Access")
#     case _:
#         print("Unkown Role")

#Q13]

# day_number=int(input("Enter the Day Number: "))

# match day_number:
#     case 1 | 2 | 3 | 4 | 5 :
#         print("Weekday")
#     case 6 | 7 :
#         print("Weekend")
#     case _ :
#         print("Invalid Day")

# #Q14]

# 
# numb = int(input("Enter priority number: "))

# match numb:
#     case 1 | 2:
#         print("Normal")
#     case 3 | 4:
#         print("Urgent")
#     case _:
#         print("Unkown Priority number")

#Q15]

# 
# numb = int(input("Enter Your Membership Level: "))

# match numb:
#     case 1 | 2:
#         print("Basic Membership")
#     case 3 | 4:
#         print("Premium Membership")
#     case _:
#         print("Unkown Membership Level")   


# Q16]

# account = input("Enter your account type:-")
# choice = int(input("Enter your choice number:-"))

# match account:

#     case "student":

#         match choice:
#             case 1:
#                 print("View Courses")
#             case 2:
#                 print("View Marks")
#             case 3:
#                 print("View Attendance")
#             case _:
#                 print("Invalid Choice")

#     case "teacher":

#         match choice:
#             case 1:
#                 print("View Students")
#             case 2:
#                 print("Enter Marks")
#             case _:
#                 print("Invalid Choice")

#     case _:
#         print("Invalid Account Type")


# Q17]

# account = input("Enter your account type:-")
# choice=int(input("Enter your choice number:-"))

# match account:
#     case "savings":


#         match choice:
#             case 1: 
#                 print("Check Balance")
#             case 2:
#                 print("Deposit")
#             case 3:
#                 print("Withdraw")


#     case "current":


#         match choice:
#             case 1:
#                 print("Check Balance")
#             case 2:
#                 print("Deposit")
#             case 3:
#                 print("Withdraw")

#     case _:
#         print("Invalid Account type")                                            


# Q18]

# category = input("Enter your category:-")
# choice=int(input("Enter your choice number:-"))
# match category:
#     case "electronics":
#         match choice:
#             case 1:
#                 print("Mobile")
#             case 2:
#                 print("Laptop")
#             case 3:
#                 print("Headphones")
#     case "clothing":
#         match choice:
#             case 1:
#                 print("Shirt")
#             case 2:
#                 print("Jeans")
#             case 3:
#                 print("Shoes")
#     case _:
#         print("Invalid category")   

#Q19]


# category = int(input("Enter category: "))
# food = int(input("Enter food: "))

# match category:
#     case 1:
#         match food:
#             case 1:
#                 print("Paneer Selected")
#             case 2:
#                 print("Dal Selected")
#             case 3:
#                 print("Veg Biryani Selected")

#     case 2:
#         match food:
#             case 1:
#                 print("Chicken Biryani Selected")
#             case 2:
#                 print("Chicken Curry Selected")
#             case 3:
#                 print("Fish Fry Selected")

#     case _:
#         print("Invalid Category")  

#Q20]
# 
# number=int(input("Enter your choice number:-"))
# a=int(input("Enter your first integer:-"))
# b=int(input("Enter your 2nd integer:-")) 
# match number:
#     case 1:
#         print(f"Addition is {a+b}")
#     case 2:
#         print(f"Subtraction is {a-b}")          
#     case 3:
#         print(f"Multiplication is {a*b}")
#     case 4:
#         print(f"Division is {a/b}")
#     case 5:
#         print(f"Floor Division is {a//b}")
#     case _:
#         print("Invalid choice number")




#Q21]


# 
# choice=int(input("Enter your choice number:-"))   
# temp=int(input("Enter your temperature:-"))

# match choice:
#     case 1:
#         fahrenheit = (temp * 9/5) + 32
#         print(f"{temp}°C is equal to {fahrenheit}°F")


#     case 2:
#         celsius = (temp - 32) * 5/9
#         print(f"{temp}°F is equal to {celsius}°C")

#     case _:
#         print("Invalid choice number") 




#Q22]      

# 

# choice=int(input("Enter your choice number:-")) 
# num=int(input("Enter your value:-"))

# match choice:
#     case 1:
#         meters = num*1000 
#         print(f"{num} kms  is equal to {meters} meters") 
#     case 2:
#         kilometers=num/1000
#         print(f"{num} meters is equal to {kilometers} kms") 
#     case 3:
#         grams=num*1000
#         print(f"{num} kilograms is equal to {grams} grams.")
#     case 4:
#         kilograms=num/1000
#         print(f"{num} grams is equal to {kilograms} kgs.") 
#     case _:
#         print("Invalid choice number") 



# Q23] 

# Account_type=input("Enter your account type:-")
# amount=int(input("Enter your amount:-"))

# match Account_type:
#     case "savings": 
#         if amount>0:
#             print("Withdrawal Request Accepted") 
#         else:
#             print("Invalid amount") 
#     case "current":
#         if amount>0:
#             print("Withdrawal request Accepted")
#         else:
#             print("Invalid Amount") 
#     case _:
#         print("Invalid CAccount Type")




# Q24] 


# choice=int(input("Enter your choice Number:-"))
# age=int(input("Enter your age:-"))

# match choice:
#     case 1:
#         if age>=18:
#             print("You can start the exam")
#         else:
#             print("You are under threshold age")
#     case 2:
#         print("You can see your result")
#     case 3:
#         print("Exam ended")
#     case _:
#         print("Invalid choice number")               
    


#Q25]
# 

# ticket_type = int(input("Enter ticket type: "))
# age = int(input("Enter your age: "))
# match ticket_type:
#     case 1:
#         if age<=5:
#          print("Free Ticket")
#         else:
#             print("Your selected ticket type is ", ticket_type)
#     case 2:
#         if age<=5:
#             print("Free Ticket")
#         else:
#             print("Your selected ticket type is ", ticket_type)
#     case 3:
#          if age<=5:
#                      print("Free Ticket")
#          else:
#                      print("Your selected ticket type is ", ticket_type)
#     case _:
#        print("Invalid ticket type") 



# Q26]

# 

# choice = int(input("Enter device: "))

# match choice:
#     case 1:
#         print("Light Controller Opened")
#     case 2:
#         print("Fan Controller Opened")
#     case 3:
#         print("AC Controller Opened")
#     case 4:
#         print("TV Controller Opened")
#     case _:
#         print("Invalid Device")



# Q27]

# 
# choice = int(input("Enter department: "))

# match choice:
#     case 1:
#         print("General Medicine Selected")
#     case 2:
#         print("Cardiology Selected")
#     case 3:
#         print("Orthopedics Selected")
#     case 4:
#         print("Pediatrics Selected")
#     case 5:
#         print("Emergency Selected")
#     case _:
#         print("Invalid Department")


# Q28]

# 

# choice = int(input("Enter choice: "))

# match choice:
#     case 1:
#         print("Book Ticket Selected")
#     case 2:
#         print("Cancel Ticket Selected")
#     case 3:
#         print("Check PNR Selected")
#     case 4:
#         print("Train Schedule Selected")
#     case 5:
#         print("Exit")
#     case _:
#         print("Invalid Choice")


# Q29]

# 

# choice = int(input("Enter choice: "))

# match choice:
#     case 1:
#         print("Search Book Selected")
#     case 2:
#         print("Issue Book Selected")
#     case 3:
#         print("Return Book Selected")
#     case 4:
#         print("View Issued Books Selected")
#     case 5:
#         print("Exit")
#     case _:
#         print("Invalid Choice")



# Q30]

# 

# status = input("Enter status: ").strip().lower()

# match status:
#     case "placed":
#         print("Your order has been placed")
#     case "confirmed":
#         print("Your order has been confirmed")
#     case "preparing":
#         print("Your order is being prepared")
#     case "out_for_delivery":
#         print("Your order is on the way")
#     case "delivered":
#         print("Your order has been delivered")
#     case "cancelled":
#         print("Your order has been cancelled")
#     case _:
#         print("Invalid Order Status")


# Q31]

# 

# banking_type = int(input("Enter banking type: "))

# match banking_type:

#     case 1:
#       
#         option = int(input("Enter option: "))

#         match option:
#             case 1:
#                 print("Personal Banking - Balance Selected")
#             case 2:
#                 print("Personal Banking - Transfer Selected")
#             case 3:
#                 print("Personal Banking - Loan Selected")
#             case _:
#                 print("Invalid Option")

#     case 2:
#        
#         option = int(input("Enter option: "))

#         match option:
#             case 1:
#                 print("Business Banking - Balance Selected")
#             case 2:
#                 print("Business Banking - Payroll Selected")
#             case 3:
#                 print("Business Loan Selected")
#             case _:
#                 print("Invalid Option")

#     case _:
#         print("Invalid Banking Type")


# 32]

#

# role = int(input("Enter role: "))

# match role:

#     case 1:
#         
#         option = int(input("Enter option: "))

#         match option:
#             case 1:
#                 print("Student Marks Selected")
#             case 2:
#                 print("Student Attendance Selected")
#             case 3:
#                 print("Student Homework Selected")
#             case _:
#                 print("Invalid Option")

#     case 2:
#         
#         option = int(input("Enter option: "))

#         match option:
#             case 1:
#                 print("Enter Marks Selected")
#             case 2:
#                 print("Teacher Attendance Selected")
#             case 3:
#                 print("Assign Homework Selected")
#             case _:
#                 print("Invalid Option")

#     case 3:
#        
#         option = int(input("Enter option: "))

#         match option:
#             case 1:
#                 print("Child Marks Selected")
#             case 2:
#                 print("Child Attendance Selected")
#             case 3:
#                 print("Contact Teacher Selected")
#             case _:
#                 print("Invalid Option")

#     case _:
#         print("Invalid Role")



# 33]


# transport = int(input("Enter transport: "))

# match transport:

#     case 1:
#         
#         option = int(input("Enter option: "))

#         match option:
#             case 1:
#                 print("Economy Selected")
#             case 2:
#                 print("Business Selected")
#             case _:
#                 print("Invalid Option")

#     case 2:
#       
#         option = int(input("Enter option: "))

#         match option:
#             case 1:
#                 print("Sleeper Selected")
#             case 2:
#                 print("AC Selected")
#             case _:
#                 print("Invalid Option")

#     case 3:
#         
#         option = int(input("Enter option: "))

#         match option:
#             case 1:
#                 print("Ordinary Selected")
#             case 2:
#                 print("Volvo Selected")
#             case _:
#                 print("Invalid Option")

#     case _:
#         print("Invalid Transport")


# Q 34]

#

# choice = int(input("Enter choice: "))

# match choice:

#     case 1:
#         print("Game Started")

#     case 2:
#         print("Game Loaded")

#     case 3:
#      
#         option = int(input("Enter setting: "))

#         match option:
#             case 1:
#                 print("Sound Settings Opened")
#             case 2:
#                 print("Graphics Settings Opened")
#             case 3:
#                 print("Controls Settings Opened")
#             case _:
#                 print("Invalid Setting")

#     case 4:
#         print("Exit")

#     case _:
#         print("Invalid Choice")



# Q 35]

# 

# category = int(input("Enter category: "))

# match category:

#     case 1:
#        
#         item = int(input("Enter item: "))

#         match item:
#             case 1:
#                 print("Soup Selected")
#             case 2:
#                 print("Spring Roll Selected")
#             case 3:
#                 print("Garlic Bread Selected")
#             case _:
#                 print("Invalid Item")

#     case 2:
#         
#         item = int(input("Enter item: "))

#         match item:
#             case 1:
#                 print("Pizza Selected")
#             case 2:
#                 print("Pasta Selected")
#             case 3:
#                 print("Biryani Selected")
#             case _:
#                 print("Invalid Item")

#     case 3:
#       
#         item = int(input("Enter item: "))

#         match item:
#             case 1:
#                 print("Ice Cream Selected")
#             case 2:
#                 print("Cake Selected")
#             case 3:
#                 print("Gulab Jamun Selected")
#             case _:
#                 print("Invalid Item")

#     case 4:
#        
#         item = int(input("Enter item: "))

#         match item:
#             case 1:
#                 print("Coffee Selected")
#             case 2:
#                 print("Tea Selected")
#             case 3:
#                 print("Juice Selected")
#             case _:
#                 print("Invalid Item")

#     case _:
#         print("Invalid Category")



# Q36] 



# payment = int(input("Enter payment type: "))

# match payment:

#     case 1:
#      
#         option = int(input("Enter option: "))

#         match option:
#             case 1:
#                 print("Scan QR Selected")
#             case 2:
#                 print("Enter UPI ID Selected")
#             case _:
#                 print("Invalid Option")

#     case 2:
#        
#         option = int(input("Enter option: "))

#         match option:
#             case 1:
#                 print("Credit Card Selected")
#             case 2:
#                 print("Debit Card Selected")
#             case _:
#                 print("Invalid Option")

#     case 3:
#       
#         option = int(input("Enter option: "))

#         match option:
#             case 1:
#                 print("Add Money Selected")
#             case 2:
#                 print("Pay Using Wallet Selected")
#             case _:
#                 print("Invalid Option")

#     case _:
#         print("Invalid Payment Type") 



# Q37]

# 

# subject = int(input("Enter subject: "))

# match subject:

#     case 1:
#     
#         option = int(input("Enter option: "))

#         match option:
#             case 1:
#                 print("Python Selected")
#             case 2:
#                 print("Java Selected")
#             case 3:
#                 print("C++ Selected")
#             case _:
#                 print("Invalid Option")

#     case 2:
#       
#         option = int(input("Enter option: "))

#         match option:
#             case 1:
#                 print("Algebra Selected")
#             case 2:
#                 print("Calculus Selected")
#             case 3:
#                 print("Statistics Selected")
#             case _:
#                 print("Invalid Option")

#     case 3:
#        
#         option = int(input("Enter option: "))

#         match option:
#             case 1:
#                 print("English Selected")
#             case 2:
#                 print("Presentation Selected")
#             case 3:
#                 print("Interview Skills Selected")
#             case _:
#                 print("Invalid Option")

#     case _:
#         print("Invalid Subject")




# Q 38]

#

# choice = int(input("Enter choice: "))

# match choice:

#     case 1:
#         option = int(input("Enter option: "))

#         match option:
#             case 1:
#                 print("Engine Started")
#             case 2:
#                 print("Engine Stopped")
#             case _:
#                 print("Invalid Option")

#     case 2:
#        
#         option = int(input("Enter option: "))

#         match option:
#             case 1:
#                 print("Headlights Selected")
#             case 2:
#                 print("Indicators Selected")
#             case 3:
#                 print("Hazard Lights Selected")
#             case _:
#                 print("Invalid Option")

#     case 3:
#        
#         option = int(input("Enter option: "))

#         match option:
#             case 1:
#                 print("Music Playing")
#             case 2:
#                 print("Music Paused")
#             case 3:
#                 print("Next Song")
#             case 4:
#                 print("Previous Song")
#             case _:
#                 print("Invalid Option")

#     case 4:
#        
#         option = int(input("Enter option: "))

#         match option:
#             case 1:
#                 print("Navigation Started")
#             case 2:
#                 print("Navigation Stopped")
#             case _:
#                 print("Invalid Option")

#     case _:
#         print("Invalid Choice")



# Q39]


# role = int(input("Enter role: "))

# match role:

#     case 1:
#        
#         option = int(input("Enter option: "))

#         match option:
#             case 1:
#                 print("View Profile Selected")

#             case 2:
#                 leave_days = int(input("Enter number of leave days: "))

#                 if leave_days > 0:
#                     print("Leave Request Submitted")
#                 else:
#                     print("Invalid Leave Days")

#             case 3:
#                 print("View Salary Selected")

#             case _:
#                 print("Invalid Option")

#     case 2:
#         
#         option = int(input("Enter option: "))

#         match option:
#             case 1:
#                 print("View Team Selected")
#             case 2:
#                 print("Approve Leave Selected")
#             case 3:
#                 print("View Reports Selected")
#             case _:
#                 print("Invalid Option")

#     case _:
#         print("Invalid Role")


# Q40]

#

# role = int(input("Enter role: "))

# match role:

#     case 1:
#         
#         option = int(input("Enter option: "))

#         match option:
#             case 1:
#                 print("Opening Student Profile")
#             case 2:
#                 print("Opening Student Marks")
#             case 3:
#                 print("Opening Student Attendance")
#             case 4:
#                 print("Opening Student Courses")
#             case _:
#                 print("Invalid Option")

#     case 2:
#        
#         option = int(input("Enter option: "))

#         match option:
#             case 1:
#                 print("Opening Students")
#             case 2:
#                 print("Opening Enter Marks")
#             case 3:
#                 print("Opening Teacher Attendance")
#             case 4:
#                 print("Opening Teacher Courses")
#             case _:
#                 print("Invalid Option")

#     case 3:
#        
#         option = int(input("Enter option: "))

#         match option:
#             case 1:
#                 print("Opening Fees")
#             case 2:
#                 print("Opening Admissions")
#             case 3:
#                 print("Opening Notices")
#             case 4:
#                 print("Opening Departments")
#             case _:
#                 print("Invalid Option")

#     case _:
#         print("Invalid Role")