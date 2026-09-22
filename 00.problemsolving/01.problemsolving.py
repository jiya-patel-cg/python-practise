
# 2
total=0
flag=True

for i in range(10):
     marks=int(input("Enter your marks: "))
     total+=marks
     if marks<35:
         flag=False
percentage=total/5
if flag:
    
     if percentage>=75:
         print("Excellent")
     elif percentage>=50:
         print("Good")
     elif percentage>=35:
         print("Pass")
     else:
         print("Fail")
else:
     print("Fail")

if flag==True:
     print("You're pass !!")
else:
     print("You're fail !!")
 

# 3

ring=input("Enter any string").lower()
# for i in string:
#     if i == "aeiou":
#         vowel+=2
        
#     elif "a"<=i<="z":
#         consonant+=1
       
#     elif "0"<=i<="9":
#         digit+=3
       
#     else: 
#         Special_character+=4
# total=vowel+consonant+digit+Special_character
# print(total)

# 4# vowel=0
# consonant=0
# digit=0
# Special_character=0
# st

# for i in range(1,6):
#     password=input(f"Enter a password {i} : ")

#     length=False
#     upper=False
#     lower=False
#     digit=False
#     special=False
#     count=0
#     if len(password)>=8:
#         length=True
    
#     for ch in password:
#         if password.isupper():
#             upper=True
#             count+=1
#         elif password.islower():
#             lower=True
#             count+=1
#         elif password.isdigit():
#             digit=True
#             count+=1
#         else:
#             special=True
#             count+=1
    
# if count==5:
#     print("Strong password")
# elif count>=3:
#     print("Mediam password")
# else:
#     print("Weak password")

# 5

# sent=input("Enter a sentence: ")
# length=len(sent)

# if length>=6:
#     print("long")
# elif length>=4:
#     print("Medium")
# else:
#     print("Short")

# 6

# odd=0
# even=0
# for i in range(1,6):
#     num=int(input(f"Enter a number {i} : "))


#     for ch in str(num):
#         if int(num)%2==0:
#             even+=1
#         elif int(num)%2!=0:
#             odd+=1
# print(f"Even number is {even}")
# print(f"Odd number is {odd}")

# if even>odd:
#     print("Last digit is Even")
# elif even<odd:
#     print("Last digit is Odd")
# else:
#     print("Both digit are equal")


# 8

# total=0

# Budget=0
# regular=0
# Premium=0
# Luxury=0

# for i in range(1,9):
#     price=float(input(f"Enter a price {i} :"))
#     total+=price
#     if price<500:
#         print("Budget")
#         Budget+=1
#     elif 500<=price<1999:
#         print("Regular")
#         regular+=1
#     elif 1999<=price<4999:
#         print("Premium")
#         Premium+=1
#     else:
#         print("Luxury")
#         Luxury+=1  

# Average=total/8
# print(f"Budget is {Budget}") 
# print(f"Regular is {regular}") 
# print(f"Premiun is {Premium}") 
# print(f"Luxury is {Luxury}") 
# print(f" Average amount is {Average}")

#9

string=input("enter the string of your choices :")
vowels=0
consonant=0
digit=0
special=0

for i in range(len(string)):
    ch=string[i]

    if i%2==0:
        position_type="Even" 
    else:
        position_type="Odd"

    if ch.lower() in "aeiou":
        char_type="Vowel"
        vowels+=1

    elif ch.isalpha():
        char_type="consonant" 
        consonant+=1

    elif ch.isdigit():
        char_type="digit"
        digit+=1 

    else:
        char_type="special"
        special 
