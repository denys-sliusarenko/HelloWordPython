name = input("Input name: ")
print("Hello,", name)
print("2+3=", 2 + 3)

x = 3.9e3
print(x)  # 3900.0
 
x = 3.9e-3
print(x)  # 0.0039

#dynamical type
user_id = "12tomsmith438"  # type str
print(user_id)
 
user_id = 234  # type int
print(user_id)

user_id = "12tomsmith438"
print(type(user_id))  # <class 'str'>
 
user_id = 234
print(type(user_id))  # <class 'int'>

print(7 / 2)  # 3.5
print(7 // 2)  # 3


print(6**2) # 6^2= 36



first_number = "2"
second_number = 3
third_number = int(first_number) + second_number
print(third_number) # 5



a = 5
b = 6
result = 5 == 6 
print(result)  # False
print(a != b)  # True
print(a > b)  # False
print(a < b)  # True
 
bool1 = True
bool2 = False
print(bool1 == bool2)  # False


age = 22
weight = 58
result = age > 21 and weight == 58
print(result) # True


age = 22
isMarried = False
result = age > 21 or isMarried
print(result) # True



age = 22
isMarried = False
print(not age > 21) # False
print(not isMarried) # True


age = 22
if age > 21:
    print("Ok")
print("Bad")


age = 18
if age > 21:
    print("Ok")
else:
    print("Bad")


    age = 18
if age >= 21:
    print("Ok")
elif age >= 18:
    print("Not bad")
else:
    print("Bad")



number = int(input("Input number: "))
i = 1
factorial = 1
while i <= number:
    factorial *= i
    i += 1
print("Factorial", number, "=", factorial)


number = int(input("Input number: "))
factorial = 1
for i in range(1, number+1):
    factorial *= i
print("Factorial", number, "=", factorial)



for i in range(1, 10):
    for j in range(1, 10):
        print(i * j, end="\t")
    print("\n")


def say_hello():
    print("Hello function")

say_hello()
say_hello()
say_hello()

def display_info(name, age):
    print("Name:", name, "\t", "Age:", age)

display_info("Tom", 22)


import myModule
myModule.main()