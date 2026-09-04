#que 1
name=input("enter your name:")
print(name)
#que 2
city=input("enter your city:")
print(city)
#que 3
name=input("enter your name:")
age=int(input("enter your age:"))
print(f"your name is {name} and age is {age}")
#que 4  input () returns string value

#que 5
a=input("value of a:")
print(type(a))

#que 6
first_name,last_name=input("enter your name:").split()
print(first_name,last_name)

#que7
full_name=input("enter your full name:")
city=input("enter your city:")
college=input("enter your college name:")
print(full_name,city,college)

#que8
name1,name2=input("enter two names:").split()
print(name1,name2)

#que 9
name1,name2,name3=input("enter three names:").split()
print(name1,name2,name3)

#que10
a=25
b=int(a)
print(b,type(a), type(b))

#que11
a="25" 
b=str(a)
print(b,type(a), type(b))

#que12
a=25.5
b=float(a)
print(b,type(a), type(b))

#que13
a=100
b=str(a)
print(b,type(a), type(b))

#que 14
a=int(input("enter a number:"))
print(type(a))

#que 15
a=float(input("enter a number:"))
print(type(a))

#que 16
a = int(input("enter first number:"))
b = int(input("enter second number:"))

print(a + b)

#que 17
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(a + b)

#que 18
name = "Rahul"
age = 20
print(f"my name is{name}and my age is{age} years old")
#que19
a=10
b=20
print(f"{a+b}")

#que 20
name=input("enter your name:")
age=input("enter your age:")
print(f"your name is {name}and your age is {age}")
# que 21
product_price =float(input("enter price"))
print(f"product_price: ${product_price: .2f}")

#que22 when we have to type only 2 points after decimal we can use : 2f

#que23
a=input("Enter product name:_")
b=input("Enter price:-")
c=input("Enter quantity:_")
print(f"Name of product is {a}, Price of product {b}, and quantity is {c} grams.")

#que24
print("A", "B", "C", sep="-") # this is show list datatypes

#que 25
print("2026", "08", "19",sep="-")

#que26
print("hello",end="")
print("word")

#que27
a=int(input("enter your first number:"))
b=int(input("enter your second number:"))
print(f"sum of{a}and{b} is {a+b}")

#que28
price = float(input("enter your product price:"))
quantity = int(input("enter your product quantity:"))
print(f"total cost:{price * quantity:.2f}")

#que29
name=input("Enter your name:-")
age=int(input("Enter your age:-"))
marks=float(input("Enter your marks:-"))
print(f" My name is {name} I am {age} years old and I scored {marks} in exam.")

#que30
name=input("Enter your name:-")
age=int(input("Enter your age:-"))
height=float(input("Enter your height:-"))
city=input("Enter your city name:-")
print(f"His name is {name} He is {age} years old His height is {height:.2f} , he lives at {city}")