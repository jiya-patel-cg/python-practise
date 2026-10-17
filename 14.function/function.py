#1

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
#     print("multiplication is a and b:",a*b)

# multiplication()


# def floordivision() :
#     a = int(input("enter the a:"))
#     b = int(input("enter the b:"))
#     print("floordivision is a and b:",a//b)

# floordivision()


# def numbers():
#     a = int(input("enter the a:"))
#     if a %2 == 0:
#         print("even number")
#     else:
#         print("odd number")

# numbers()

# def addition(a,b):
#     c = a+b
#     print(c)
# a = int(input("enter the a:"))
# b= int(input("enter the b:"))
# addition(a,b)

# a=10
# b=20
# c=40
# def add(a,b):
#     c= a+b
#     return c
# def sub(a,b):
#     return a-b
# def mul(a,b):
#     return a*b
# # result = mul(sub(add(a,b),c),a)
# result = mul(sub(a,b),add(b,c))
# print(result)


def double (number):
    return number*2
def add(number):
    return number+5
result = add(double(15))
print(result)