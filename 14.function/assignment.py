#1
# def function(name):
#     print("welcome", name)

# function("welcome to python")
# function("welcome to python")
# function("welcome to python")

#2
# def function(name):
#     print("Hello", name)

# function("Asha")

#3
# def show_number(number):
#     print(number)

# show_number(25)

#4
# def add(a, b):
#     return a + b

# answer = add(2, 3)
# print(answer)

#5
# def square(number):
#     result = number * number
#     return result

# print(square(5))

#6
# def numbers():
#     a = int(input("enter the a:"))
#     if a %2 == 0:
#         print("even number")
#     else:
#         print("odd number")

# numbers()


#7
# def full_name(first_name,last_name):
#    return "jiya", "patel"
# full_name("JIYA","PATEL")
# print(full_name)

# def fullname(first, last):
#     return first + " " + last
# fullname("Jiya", "Patel")
# print(fullname("Jiya", "Patel"))

#8
# def introduce(name, age, city):
#     print("Name:", name)
#     print("Age:", age)
#     print("City:", city)

# introduce("jiya", 18, "Patan")

#9
# def substraction() :
#     a = int(input("enter the a:"))
#     b = int(input("enter the b:"))
#     print("substraction is a and b:",a-b)

# substraction()

#10
# def get_min_max(a, b):
#     if a>b:
#        return "bigger"
    
#     else:
#         return "small"
# a=int(input("Enter Number: "))
# b=int(input("Enter Number: "))    
# print(get_min_max(a, b))    
    
 #11
# def addition() :
#     a = int(input("enter the a:"))
#     b = int(input("enter the b:"))
#     print("addition is a and b:",a+b)

# addition()

# def substraction() :
#     a = int(input("enter the a:"))
#     b = int(input("enter the b:"))
#     print("substraction is a and b:",a-b)

# substraction()


# def multiplication() :
#     a = int(input("enter the a:"))
#     b = int(input("enter the b:"))
#     print("product is a and b:",a*b)

# multiplication()

# def division():
#     a = int(input("enter the a:"))
#     b = int(input("enter the b:"))
#     print("divsion is a and b")


#13
# def classify_number(a):
#     if a>0:
#        return "Positive"
#     elif a<0:
#         return "Negative"
#     else:
#         return "Zero"
# a=int(input("Enter Number: "))    
# print(classify_number(a))    
    
#  #14
# def product(price, quantity=1):
#     return price * quantity

# price = int(input("enter the price"))
# quantity = int(input("enter the quantity"))
# print(product(price,quantity))

#15
# def create_email(username, domain="example.com"):
#     return username + "@" + domain

# print(create_email("jiya"))
# print(create_email("jiya", "gmail.com"))

#16
# def format_name(first, last, uppercase=False):
#     name = first + " " + last
#     if uppercase:
#         return name.upper()
#     return name

# print(format_name("jiya", "patel"))
# print(format_name("jiya", "patel", True))

#17
# def percentage(marks, total=100):
# #     return (marks / total) * 100

# # print(percentage(80))
# # print(percentage(45, 50))

#18
# def convert_minutes(minutes, seconds_per_minute=60):
#     return minutes * seconds_per_minute
# print(convert_minutes(30))

#19
# def student_details(name, age, city):
#     print("Name:", name)
#     print("Age:", age)
#     print("City:", city)

# student_details(city="Pune", name="Rahul", age=18)

#20
# def bill(item, quantity=1, price=100):
#     return quantity * price

# print(bill("Book"))
# print(bill("Pen", 3, 20))
# print(bill("Bag", price=500, quantity=2))



# 21.
def analyze_number(number):
    absolute_value = -number if number < 0 else number
    even = number % 2 == 0
    digits = len(str(absolute_value))
    return absolute_value, even, digits

print(analyze_number(-246))


# # 22.
# def calculate_stats(a, b, c):
#     return min(a, b, c), max(a, b, c), a + b + c

# print(calculate_stats(10, 5, 20))


# # 23.
# def make_sentence(subject, verb, object):
#     return subject + " " + verb + " " + object

# print(make_sentence(object="Python", verb="learns", subject="Rahul"))


# # 24.
# def apply_discount(price, discount=0):
#     return price - (price * discount / 100)

# print(apply_discount(1000))
# print(apply_discount(1000, 20))


# # 25.
# def calculate_pay(hours, rate=200, bonus=0):
#     return hours * rate + bonus

# print(calculate_pay(8))
# print(calculate_pay(8, 300))
# print(calculate_pay(8, bonus=500))
# print(calculate_pay(8, rate=300, bonus=500))


# # 26.
# def get_coordinates(x=0, y=0):
#     return x, y

# print(get_coordinates())
# print(get_coordinates(x=5))
# print(get_coordinates(y=10))
# print(get_coordinates(x=5, y=10))


# # 27.
# def compare(a, b):
#     difference = a - b
#     difference = -difference if difference < 0 else difference

#     if a > b:
#         result = "A is greater"
#     elif b > a:
#         result = "B is greater"
#     else:
#         result = "Equal"

#     return result, difference

# print(compare(10, 5))
# print(compare(3, 8))
# print(compare(7, 7))


# # 28. 
# def convert_temperature(value, scale="C"):
#     if scale == "C":
#         return (value * 9 / 5) + 32
#     elif scale == "F":
#         return (value - 32) * 5 / 9

# print(convert_temperature(25))
# print(convert_temperature(98.6, "F"))


# # 29. 
# def calculate_result(marks, passing_marks=35):
#     if marks >= passing_marks:
#         return "Pass"
#     else:
#         return "Fail"

# print(calculate_result(75))
# print(calculate_result(30))
# print(calculate_result(40, 50))

#30
# def order_summary(item, quantity=1, price=100, delivery_fee=40):
#     return quantity* price + delivery_fee
# print(order_summary("book"))
# print(order_summary("pen",quantity=5,price=50,delivery_fee=10))
