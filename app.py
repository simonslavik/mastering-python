age = 20
print("Hello, World!")
print("I am", age, "years old.")
price = 19.99
print("The price is $", price)
first_name = "John"
last_name = "Doe"
print("My name is", first_name, last_name)
is_student = True
print("Am I a student?", is_student)
height = 5.9
print("My height is", height, "feet")
# This is a simple Python script that demonstrates variable assignment and printing to the console.

name = input("Press Enter to exit... ")
print("Exiting the program. Goodbye!")
# This is a simple Python script that demonstrates variable assignment and printing to the console.

birth_year = 2004
age = 2024 - birth_year
print("I am", age, "years old.")
print("Hello, World!")

# This is a simple Python script that demonstrates variable assignment and printing to the console.
print("Hello, World!")
age = 20
print("I am", age, "years old.")
price = 19.99
print("The price is $", price)
first_name = "John"
last_name = "Doe"
print("My name is", first_name, last_name)
is_student = True
print("Am I a student?", is_student)
height = 5.9
print("My height is", height, "feet")
# This is a simple Python script that demonstrates variable assignment and printing to the console.

int(input("Press Enter to exit... "))
float(input("Press Enter to exit... "))

bool(input("Press Enter to exit... "))
str(input("Press Enter to exit... "))


first = "10"

course = "Python for Beginners"

course.find("Python")

course.replace("Beginners", "Absolute Beginners")

print("python" in course )

print(10 + 3 * 2)

x = 10
x = x + 3
print(x)

x += 3 
print(x)

x *= 3
print(x)

x = 10 + 3 * 2 ** 2
print(x)

x = (10 + 3) * 2 ** 2
print(x)

x = 3 > 2 and 3 > 1
print(x)

price = 25
print(price > 10 and price < 30)
print(price > 10 or price < 30)

temperature = 35
if temperature > 30:
    print("It's a hot day")
    print("Drink plenty of water")
elif temperature > 20:  
    print("It's a nice day")
elif temperature > 10:
    print("It's a bit cold")
else:
    print("It's cold")
print("Enjoy your day!")

and (both)
or (at least one)
not (inverts)
name = "John"

if len(name) < 3:
    print("Name must be at least 3 characters")
elif len(name) > 50:
    print("Name can be a maximum of 50 characters")
else:
    print("Name looks good!")                           
# This is a simple Python script that demonstrates variable assignment and printing to the console.
print("Hello, World!")

weight = int(input("Weight: "))
unit = input("(K)g or (L)bs: ")
if unit.upper() == "K":
    converted = weight * 2.20462
    print("Weight in pounds:", converted)
elif unit.upper() == "L":
    converted = weight / 2.20462
    print("Weight in kilograms:", converted)

else:
    print("Invalid unit")   
# This is a simple Python script that demonstrates variable assignment and printing to the console.
print("Hello, World!")

while True:
    name = input("Enter your name: ")
    if name != "":
        break  
    print("Hello " + name)
print("Thank you!")
# This is a simple Python script that demonstrates variable assignment and printing to the console.
print("Hello, World!")  

i = 1
while i <= 5:
    print(i * "*")
    i = i + 1
print("Done")

names = ["John", "Bob", "Mosh", "Sarah", "Mary"]

print(names[])
print(names[2:])
print(names[:3])
print(names[2:4])
print(names[:])
names[0] = "Jon"
print(names[0])
print(names)
print(len(names))
names.append("Peter")
print(names)
names.insert(0, "Paul")
print(names)
names.remove("Mosh")
print(names)
names.pop()

numbers = [1, 2, 3, 4, 5]

for item in numbers:
    print(item)

for name in names:
    print("Hello " + name)

i = 0
while i < len(names):
    print(names[i])
    i = i + 1

for i in range(5):
    print(i)
for i in range(5, 10):
    print(i)
for i in range(5, 10, 2):
    print(i)    

for i in range(len(names)):
    print(names[i]) 

# This is a simple Python script that demonstrates variable assignment and printing to the console.
print("Hello, World!")
print("Hello, World!")
print("Hello, World!")
print("Hello, World!")
print("Hello, World!")

def greet_user(first_name, last_name):
    print(f"Hello {first_name} {last_name}")
    print("Welcome aboard")
greet_user("John", "Doe")
greet_user("Mary", "Smith")
greet_user("Jane", "Johnson")
# This is a simple Python script that demonstrates variable assignment and printing to the console.

print("Hello, World!")
def square(number):
    return number * number
result = square(3)

print("Hello World!")

x = 1 
y = 2
unit_price = 3.99

print("Mosh Hamedani")

print("o-----")

print(" |||||")

print("*" * 10)
price = 10
print(price)
name = "Mosh"
print(name)
age = 20
print(age)
rating = 4.9
print(rating)
is_published = False
print(is_published)
print("Hello, World!")
print("I am", age, "years old.")
price = 19.99
print("The price is $", price)
first_name = "John"
last_name = "Doe"
print("My name is", first_name, last_name)
is_student = True

input("Press Enter to exit... ")
print("Exiting the program. Goodbye!")
print("Am I a student?", is_student)
height = 5.9
print("My height is", height, "feet")



name = input("what is your name? ")
favorite_color = input("What is your favorite color? ")
print(name + " likes " + favorite_color)

birth_year = int(input("Birth year: "))
age = 2024 - birth_year
print("Your age is: " + str(age))
print("Hello, World!")

weight_lbs = input("Weight (lbs): ")
weight_kg = int(weight_lbs) * 0.453592
print("Weight (kg): " + str(weight_kg))
print("Hello, World!")
birth_year = 2004

course = "Python for Beginners"
print(f"{course} is a great course!")
print(f"{course} is {2 + 3} times better than the previous version.")


course = "Python for Beginners"
print(len(course))

print(course.upper())
print(course.lower())
print(course)


course.find("P")
course.replace("Beginners", "Absolute Beginners")

print(course.replace("P", "J"))

print("Python" in course )
print("python" in course )
print("Hello, World!")
print(10 + 3 * 2)

len("Hello, World!")


print(10/3)
print(10//3)
print(10 % 3)

print(10 ** 3)

x = 10
x = x + 3
print(x)

x += 3
print(x)

x *= 3
print(x)


x = 10 + 3 * 2 ** 2
print(x)


x = 2.9

print(round(x))

is_hot = True

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
else:
    print("It's a cold day")
    print("Wear warm clothes")
print("Enjoy your day!")
# This is a simple Python script that demonstrates variable assignment and printing to the console.
print("Hello, World!")  

price = 100000 
has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down payment: ${down_payment}")


# This is a simple Python script that demonstrates variable assignment and printing to the console.
print("Hello, World!")  
print("Hello, World!")
print("Hello, World!")

if 1 + 1 == 2:
    print("Math works!")   
print("Hello, World!")
print("Hello, World!")
print("Hello, World!")  

temperature = 35
if temperature > 30:    
    print("It's a hot day")
    print("Drink plenty of water")
elif temperature > 20:

    print("It's a nice day")
elif temperature > 10:
    print("It's a bit cold")
else:
    print("It's cold")
print("Enjoy your day!")
# This is a simple Python script that demonstrates variable assignment and printing to the console.
print("Hello, World!")


if has_good_credit and not has_criminal_record:
    print("Eligible for loan")
# This is a simple Python script that demonstrates variable assignment and printing to the console.
print("Hello, World!")      
print("Hello, World!")
print("Hello, World!")
print("Hello, World!")  


i = 1
while i <= 5:
    print(i * "*")
    i = i + 1
print("Done")
# This is a simple Python script that demonstrates variable assignment and printing to the console.
print("Hello, World!")
print("Hello, World!")
print("Hello, World!")
print("Hello, World!")
print("Hello, World!")              



names = ["John", "Bob", "Mosh", "Sarah", "Mary"]
print(names[0])
print(names[-1])
print(names[2:])
print(names[:3])
print(names[2:4])
print(names[:])
names[0] = "Jon"
print(names[0])
print(names)
print(names)
print(len(names))
names.append("Peter")
print(names)
names.insert(0, "Paul")
print(names)
names.remove("Mosh")
print(names)
names.pop()
print(names)
print(names.index("Sarah"))
print("Mosh" in names)
print("Mary" in names)
print("Hello, World!")

numbers = [1, 2, 3, 4, 5]
for item in numbers:
    print(item) 
for name in names:
    print("Hello " + name)
i = 0
while i < len(names):
    print(names[i])
    i = i + 1
for i in range(5):
    print(i)
for i in range(5, 10):
    print(i)
for i in range(5, 10, 2):
    print(i)




started = False

while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started!")
        else:
            started = True
            print("Car started...Ready to go!")
    elif command == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started = False
            print("Car stopped.")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to exit
""")
    elif command == "quit":
        break
    else:
        print("I don't understand that...")
# This is a simple Python script that demonstrates variable assignment and printing to the console.
print("Hello, World!")

for item in "python":
    print(item)
print("Hello, World!")
print("Hello, World!")
print("Hello, World!")
print("Hello, World!")
print("Hello, World!")

for item in ["Mosh", "John", "Sarah"]:
    print(item)
print("Hello, World!")

for item in range(10):
    print(item)
print("Hello, World!")

for item in range(5, 10, 2):
    print(item)
print("Hello, World!")

for item in range(5):
    for x in range(3):
        print(item, x)
print("Hello, World!")

for x in range(4):
    for y in range(3):
        print(f"({x}, {y})")
print("Hello, World!")

numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    print('x' * x_count)
print("Hello, World!")      

names = ["John", "Bob", "Mosh", "Sarah", "Mary"]

print(names[-1])


names[0] = "Jon"
print(names)

numbers = [1, 2, 3, 4, 5]
max = max(numbers)

print(max)

print("Hello, World!")

for x in numbers:
    max = 0
    if x > max:
        max = x
print(max)
print("Hello, World!")  

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0][1])

for row in matrix:
    for item in row:
        print(item)
print("Hello, World!")  

numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)
print("Hello, World!")
def greet_user(first_name, last_name):
    print(f"Hello {first_name} {last_name}")
    print("Welcome aboard")
greet_user("John", "Doe")
greet_user("Mary", "Smith")
greet_user("Jane", "Johnson")
# This is a simple Python script that demonstrates variable assignment and printing to the console.
print("Hello, World!")
def square(number):
    return number * number
result = square(3)
print(result)
print("Hello, World!")
def square(number):
    return number * number
print(square(3))
print(square(4))
print(square(5))


numbers = [2, 3, 4, 5]
numbers2 = numbers.copy()

numbers.append(6)
print(numbers)

numbers = (1,2,3)
numbers.count(1)
numbers.index(2)
print("Hello, World!")


customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}

print(customer["name"])
print(customer.get("birthdate", "Jan 1, 1990"))

phone = input("Phone: ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
}

output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "
print(output)
print("Hello, World!")
message = input("> ")
words = message.split(' ')
emojis = {
    ":)": "😊",
    ":(": "😞"
}   
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)
print("Hello, World!")
def emoji_converter(message):

    words = message.split(' ')
    emojis = {
        ":)": "😊",
        ":(": "😞"
    }   
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output
message = input("> ")
print(emoji_converter(message))
print("Hello, World!")
try:
    age = int(input("Age: "))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print("Age cannot be 0.")
except ValueError:
    print("Invalid value")


print("Hello, World!")
class Point:



    def move(self):
        print("move")
    def draw(self):
        print("draw")       
    def __init__(self, x, y):
        self.x = x
        self.y = y  
point1 = Point(10, 20)
print(point1.x)
print(point1.y)


for word in words: 
    output += emojis.get(word, word) + " "
print(output)
print("Hello, World!")
class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y  

    def move(self):
        print("move")
    def draw(self):
        print("draw")
point1 = Point(10, 20)
print(point1.x)
print(point1.y)
point1.x = 11
print(point1.x)
point1.y = 22
print(point1.y)
point1.draw()
point1.move()


print("Hello, World!")
def greet_user(first_name, last_name):
    print(f"Hello {first_name} {last_name}")
    print("Welcome aboard")
greet_user("John", "Doe")
greet_user("Mary", "Smith")
greet_user("Jane", "Johnson")
# This is a simple Python script that demonstrates variable assignment and printing to the console.
print("Hello, World!")
def square(number):
    return number * number
result = square(3)
print(result)
print("Hello, World!")
def square(number):
    return number * number
print(square(3))
print(square(4))
print(square(5))    




