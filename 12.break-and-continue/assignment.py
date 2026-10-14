#1
# for i in range(1, 8):
#     if i == 5:
#         break
#     print(i)
# print("Finished")

# #2
# word = "skyline"

# for ch in word:
#     if ch in "aeiou":
#         break
#     print(ch)

#3
# n = 2

# while n <= 10:
#     print(n)
#     if n == 6:
#         break
#     n += 2

# #4
# limit = int(input("enter the limit"))
# for limit in range(1,limit+1):
#     if limit == 7:
#         break
#     print(limit)

# #6
# numbers = [10,-5,-4,-3,2,20,30]
# for numbers in numbers:
#     if numbers<0:
#         continue
#     print(numbers)

# #7
# for row in range(1, 4):
#     for col in range(1, 5):
#         if col == 3:
#             break
#         print(row, col)

#8
# str = input("enter a str:")
# target = input("enter a target:")
# for str in target:
#     if str == target:
#      continue
#     print("found") 
        
# else:
#     print("not found")

#9
# for i in range(1, 7):
#     if i == 4:
#         continue
#     print(i)

#10
# for ch in "education":
#     if ch in "aeiou":
#         continue
#     print(ch, end="")

#11
# n = 0

# while n < 5:
#     n += 1
#     if n == 3:
#         continue
#     print(n)

# #12
# num = int(input("enter a num:"))
# for num in range(1,num):
#     if num %3==0:
#         continue
#     print(num)

#13
# str = input("enter a str:")
# char = input("enter a char:")
# for  str in char:
#     if str == char:
#         continue
#     print("char")


#14
# input_marks = input("enter a marks:").split()

# for marks in input_marks:
#     num = int(marks)
#     if marks<40:
#         print(marks)


# # 15
# for i in range(1, 5):
#     if i == 2:
#         continue
#     print("A", i)
#     print("B", i)

#16
# n = 1

# while n <= 5:
#     if n == 3:
#         n += 1
#         continue

#     print(n)
#     n += 1

#17
# ch = input("enter a string")
# for ch in ch:
#     if ch in "aeiou":
#         continue
#     print(ch, end="")

# #18
# for i in range(1, 4):
#     print(i)
# else:
#     print("Done")

#19
# for i in range(1, 5):
#     if i == 2:
#         continue
#     print(i)
# else:
#     print("Completed")

#20
# for i in range(1, 5):
#     if i == 3:
#         break
#     print(i)
# else:
#     print("Completed")
# print("Outside loop")


#21
# for item in []:
#     print("Inside")
# else:
#     print("Else block")

#22
# user_number = input("enter the number:")
# number = int(user_number).split()
# target = int(input("enter the num"))
# for num in number:
  
#     if number == target:
#         print("found")
#         break
#     else:
#         print("not found")

#23
# str = input("enter a str:")
# target = input("enter a target:")
# for str in target:
#     if str == target:
#       print("found") 
#     break
   
        
# else:
#     print("not found")

#24
# n = int(input("enter the n"))
# count=0
# for i in range(1,n):
#     for j in range(1,n-1):
    
#         if i%j==0:
#             count=count+1
# # print(count)
#             if count==2:
#                 print(f"{j} is a Prime number")
#                 break
#             else:  
#                 print(f"{j} is not a Prime number")
#                 # break

#25
# values = [2, 4, 6, 8]

# for value in values:
#     if value % 2 != 0:
#         print("Odd found")
#         break
# else:
#     print("All are even")

#26
#case A
# for x in range(3):
#     continue
# else:
#     print("A")
# ans yes

#case B
# for x in range(3):
#     break
# else:
#     print("B")
# ans no

#case c
# for x in range(0):
#     print(x)
# else:
#     print("C")
# yes
#27

# numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))


# target = int(input("Enter the target number: "))

# for num in numbers:
#     if num == target:
#         print("Found")
#         break
# else:
#     print("Not found")

#28
# for i in range(1, 4):
#     if i == 2:
#         pass
#     print(i)

#29
# x = 10

# if x > 5:
#     pass

# print("Finished")

#30
# for letter in "cat":
#     pass

# print("Loop ended")

#31
# for i in range(1,6):
#     if i%2==0:
#        pass
#     print(i)
    
#32
# menu=input("Enter: ")
# if menu=="Cake":
#     print("Cake!")
# elif menu=="Pastry":
#     pass
# else:
#     print("Unknwon")
# print("Program closed!")
# #33
# A
# for i in range(1, 5):
#     if i == 3:
#         pass
#     print(i)

#B
# for i in range(1, 5):
#     if i == 3:
#         continue
#     print(i)

#34
# for i in range(1, 6):
#     if i == 3:
#         continue
#     print(i)

#35
# for i in range(1, 6):
#     if i == 2:
#         continue
#     if i == 4:
#         break
#     print(i)
# else:
#     print("Finished")

#36
# list = [-4,-2,4,7,9]
# target = int(input("enter a number"))
# for list in list:
#     if list == target:
#         print("found")
#         break
#     else:
#         print("not found")
    
#38
# for row in range(1, 4):
#     for col in range(1, 4):
#         if col == 2:
#             continue
#         if row == 3:
#             break
#         print(row, col)
#     else:
#         print("Inner loop completed")
