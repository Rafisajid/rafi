from tkinter import Y

print("i am sajid")
print("i love to play football")
print("right now iam interested in coding")

#name = "sajid"
first_name = "rafi"
last_name = "sajid"
full_name = first_name +" "+ last_name
print("hello "+full_name)

age = 19
#age = 19 + 1
#age = age + 1
age += 1
print("my age is :"+str(age))
height = 5.11
print("my is height is :"+str(height)+"inch")

human = True
print("iam a human :"+str(human))
#name = "rafi sajid"
#age = 20
#sex = "Male"

name , age, sex = "rafi sajid", 20, "male"
print(name)
print(age)
print(sex)

name = "rafi sajid"
#print(len(name))
#print(name.find("s"))
#print(name.capitalize())
#print(name.upper())
#print(name.lower())
#print(name.isdigit())
#print(name.isalpha())
#print(name.count("a"))
#print(name.replace("f","n"))
#print(name*3)

x = 9
y = 2.6
z = "5"

y = int (y)
z = int (z)

x = str(x)
y = str(y)

#y = float (y)
#z = float (z)
#x = float (x)

print(x)
print(y)
print(z)

name = input("what is ur name :")
age = int(input("how old are you?:"))
height =float(input("how tall are u :"))
print("hello "+name)
print("your age is " + str(age) + " years old" )
print("you are "+str(height)+"inch tall")

pi = 3.14
x = 1
y = 2
z = 3
#print(math.ceil(pi))
#print(round(pi))
#print(math.floor(pi))
#print(abs(pi))
#print(pow(pi,2))
#print(math.sqrt(pi))
print(max(x, y, z))
print(min(x, y, z)) 

name = "rafi sajid"

first_name = name[:5]
last_name = name[5:10]
funky_name = name[0:10:3]
reverse_name = name[::-1]


print(reverse_name)

#website1 = "http://google.com"
#website2 = "http://wikipedia.com"
#slice = slice(7,-4)
#print(website2[slice]) 
