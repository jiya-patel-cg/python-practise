# str = input("enter the str:")
# for char in str:
#     if char=="o":
#       print(char)
#       break


# str = input("enter the str:").strip().lower()
# flag=True
# count=0
# for char in str:
#     count+=1
#     if char =="o":
#         flag = False
#         print("found")
        
# print(count)
# if flag:
#     print("not found")



# str = input("enter the str:")
# flag = True
# count=0
# a = len(str)-1
# for char in range(0,a):
#     count+=1
#     if char =="o":
#         flag =False
#         print("found")
#         break

# print(count)
# if flag:
#     print("not found")



# str = input("enter the str:")
# flag=True
# a=len(str)
# for i in range(a):
#     if str[i]=="o":
#         flag = False
#         print("found")
#         break
# if flag:
#     print("not found")

# for i in range(1, 6):
#     if i == 5:
#         break

#     print(i)


# #1
# for i in range(1,10):
#     if i == 6:
#         break
#     print(i)

# #2
# num = int(input("enter the num"))
# for i in range(10,50):
#     if i==30:
#         break
#     print("found")

# # #3
# number =int(input("enter the number:"))
# for num in number:
#     if num ==0:
#         break
#     print(num)

# #4
# for i in range(1,100):
#     if i %17==0:
#         break
#     print(i)

#5
# for i in range(1,20):
#     if i%2==0:
#         continue
#     print(i)

# #6
# num = [10,-2,30,-5,40,-8]
# for num in num:
#     if num<0:
#      continue
#     print(num)

# #7
# for i in range(1,20):
#     if i %3==0:
#         continue
#     print(i)

#8
# num = [5, 12, 8, 21, 30, 7]
# for num in num:
#     if num >10:
#         continue
#     print(num)

# #9
# temp=int(input("enter the temp"))
# if temp>0:
#    pass
#    print("weather")



# #10
# for i in range(1, 6):
#     if i == 3:
#         pass

# #11
# num = int(input("enter the num"))
# for i in range(1,num):
#   if num>0:
#     pass

#   elif num<0:
#     continue
#   elif num ==0:
#     break
#   print(num)

#12
# numbers = [12, 5, -4, 18, 0, 25, 30]

# for number in numbers:

#     if number < 0:
#         continue

#     if number == 0:
#         break

#     print(number)


#13
# numbers = [10,12,-5,5,8,0]
# for numbers in numbers:
#     if numbers == 5:
#         break
# else:
#     print("number found")
for i in range(1, 5):
    if i == 2:
        pass
    elif i == 3:
        continue
    elif i == 4:
        break
    print(i)
else:
    print("Completed")
print("Outside")