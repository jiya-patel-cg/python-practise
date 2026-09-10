# level 1
# que 1
# a=int(input("Enter any integers"))
# if a>0:
#     print("positive")
# elif a<0:
#     print("negative")   
# elif a==0:
#     print("zero") 

#que2
# a=int(input("Enter any integers"))
# if a>0 and a%2==0:
#     print("positive even")
# elif a<0 and a%2==0:
#     print("negative even")
# elif a>1 and a%2==1:
#     print("positive odd")
# elif a<1 and a%2==1:
#     print("negative odd")
# elif a==0:
#     print("zero")

#que3
# num1=int(input("enter a num 1"))
# num2=int(input("enter a num 2"))
# if num1>num2:
#     print("num1")
# elif num2>num1:
#     print("num2")
# elif num1==num2:
#     print("both are equal")

# #que4
# num1=int(input("Enter a number 1"))
# num2=int(input("Enter a number 2"))
# num3=int(input("Enter a number 3"))
# if num1<num2 and num1<num3:
#     print("num1")
# elif num2<num3 and num2<num3:
#     print("num2")
# elif num3<num1 and num3<num1:
#     print("num3")
# elif num1==num2==num3:
#      print("numbers are equaal")

#que5
# num1=int(input("Enter a num1"))
# num2=int(input("Enter a num2"))
# num3=int(input("Enter a num3"))
# if num1>num2 and num1>num2:
#     print(f"the biggest number is{num1}")
# elif num2>num3 and num2>num1:
#     print(f"the biggest number is{num2}")
# elif num3>num1 and num3>num2:
#     print(f"the biggest number is {num3}")
# elif num1==num2==num3:
#     print("numbers are equal")

#que6
# num=int(input("Enter a num"))
# if num%5 and num%11:
#     print("both numbers are divisible")
# elif num%5:
#     print("divisible by 5")
# elif num%11:
#     print("divisible by 11")
# else:
#     print("divisible by neither")

#que7
# num=int(input("Enter a number"))
# if num%3 and num%7:
#     print("both numbers are divisible")
# elif num%3:
#     print("divisible by 3")
# elif num%7:
#     print("divisible by 7")
# else:
#     print("divisible by neither")

#que 8
# marks=int(input("Enter a number"))
# if marks<0:
#     print("invalid marks")
# elif marks>100:
#     print("invalid marks")
# elif marks>=40:
#     print("pass")
# elif marks<=40:
#     print("fail")

#que9
# marks=int(input("Enter a number"))
# if marks<0 and marks>100:
#     print("invalid marks")
# elif marks>=90:
#     print("Grade A")
# elif marks>=80:
#     print("Grade B")
# elif marks>=70:
#     print("Grade C")
# elif marks>=60:
#     print("Grade D")
# elif marks>=40:
#     print("Grade E")
# elif marks<=40:
#     print("fail")

#que10
# age=int(input("Enter your age"))
# if age<0:
#     print("invalid age")
# elif age<18:
#     print("cannot vote")
# elif age>18 or age>120:
#     print(" can vote")

# level 2

# que 11
# year=int(input("enter year: "))
# if year%4==0:
#     print("This year is a leap year")
# else:
#     print("This year is not a leap year")

#que12
# a=input("Enter a first character")
# if "A"<=a <="Z":
#     print("uppercase")
# elif "a"<=a <="z":
#     print("lowercase")
# elif 0<=str(a) <=9:
#     print("digit")
# else:
#     print("special character")

#que13
# a=input("enter a one alphabet:").lower()
# if a in "aeiou":
#     print("vowel")
# else:
#     print("consonant")


#que 14
# cost_price=int(input("Enter a cost_price"))
# selling_price=int(input("Enter a selling_price"))
# if selling_price>cost_price:
#     print("profit")
# elif selling_price<cost_price:
#     print("loss")
# elif selling_price==cost_price:
#     print("No profit and No loss")


#que15
# num=input("Enter a 3 digit number:")
# a=num%10
# num=num//10
# b=num%10
# c=num//10
# print(a+b+c)

#que16
# unit=int(input("enter number of unit:-"))

# if unit <= 100:
#     bill = unit*5
# elif unit <= 200:
#     bill = (100*5) + (unit - 100)*7
# else:
#     bill = (100*5)+(100*7)+(unit-200)*10

# print("bill is",bill)
#que18

# a=int(input("enter your first number"))

# b=int(input("enter your second number"))

# print("1.addition\n2.subtaration\n3.multiplication\n4.division\n5.flor division\n choose your opretion")

# aop=int(input("eneter your opretion number"))

# if aop == 1:

#     print(a+b)

# elif aop == 2:

#     print(a-b)

# elif aop == 3:

#     print(a*b)

# elif aop == 4:

#     print(a/b)

# elif aop == 5:

#     print(a//b)
# else:
#     print("you choose other number")

# que20
# a=int(input("Enter a first length"))
# b=int(input("Enter a second length"))
# c=int(input("Enter a third length"))
# if a+b>c and b+c>a and c+a>b:
#     print("valid")
# else:
#     print("invalid")


 
