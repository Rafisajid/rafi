#print("hello rafi sajid")
#print("i love to play games")

#name = "rafi sajid"
#print("My name is : "+ (name))

#first_name = "rafi"
#last_name = "sajid"
#full_name = first_name +" "+ last_name
#print("My name is : "+(full_name))

#age = 20
#age += 1
#age = age + 1
#print("my age is :"+str(age))

#height = 5.11
#print("my height is :"+str(height)+"inch")

#Human = True
#print("you are a human :"+str(Human))

#name = "rafi sajid"
#age = 20
#attractive = True

#name , age, attractive = "bro", 21, True
#print(name)
#print(age)
#print(attractive)

#name = "sajid"

#print(len(name))
#print(name.find("f"))
#print(name.capitalize())
#print(name.upper())
#print(name.lower())
#print(name.isdigit())
#print(name.isalpha())
#print(name.count("j"))
#print(name.replace("s","g"))
#print(name*3)

#x = 1
#y = 11.2
#z = "3"

#x = float(x)
#y = float(y)
#z = float(z)

#print("x is "+str(x))
#print("Y is "+str(y))
#print(z*3)

#name = input("what's your name ?:")
#age = int(input("your age is :"))
#height = float(input("my height is :"))

#print("assalamualykum " +(name))
#print("iam "+str(age)+" years old")
#print("my height is "+str(height)+"inch")

#import math

#pi = 3.14
#x = 1
#y = 2
#z = 3

#print(round(pi))
#print(math.ceil(pi))
#print(math.floor(pi))
#print(abs(pi))
#print(pow(pi,2))
#print(math.sqrt(pi))
#print(max(x, y, z))
#print(min(x, y, z))


#name = "rafi sajid"

#first_name = name[:4]
#last_name = name[:11]
#funky_name = name[0:11:1]
#reversed_name = name[::-1]
#print(reversed_name)

#website = "http://google.com"
#website2 = "http://wikipedia.com"
#slice = slice(7,-4)
#print(website[slice])
#print(website2[slice])

age = int(input("how old are you?: "))

if age == 100:
    print("you are a century old!")
elif age >= 18:
    print("you are an adult!")
elif age <= 0:
    print("you haven't born yet!")
else:
    print("you are a child!")


#temp = int(input("what is the temperature outside?: "))

#if not (temp >= 0 and temp <=30):
    #print("the temperature is bad today!")
    #print("stay inside of home")
#elif not (temp < 0 or temp > 30):
    #print("the temperature is good today")

#while 1==1:
    #print("Help! I'm stuck in a loop")

#name = None
#while not name:
  #name = input("enter your name :")
#print("hello "+name)

#for i in range(10):
    #print(i+1)
#for i in range (20,100+1,3):
    #print(i)
#for i in  ("rafi sajid"):
   # print(i)

#import time

#for seconds in range(10,0,-1):
     #print(seconds)
     #time.sleep(1)
#print("eid mubarak")

#rows = int(input("how many rows?: "))
#columns = int(input("how many columns?: "))
#symbol = input("Enter a symbol to use: ")

#for i in range(rows):
    #for j in range(columns):
        #print(symbol, end="")
    #print()


#while True:
    #name = input("Enter your name : ")
    #if name != "":
        #break

#phone_number = "018_245_90704"

#for i in phone_number:
    #if i =="_":
        #continue
    #print(i, end="")


#for i in range(1,21):
    #if i == 13:
        #pass
    #else:
        #print(i)

#food = ["pizza","rice","hotdog","mushroom"]

#food[0] = "apple"

#food.append("chicken")
#food.remove("hotdog")
#food.pop()
#food.insert(0,"cake")
#food.sort()
#food.clear()

#for i in food:
    #print(i)


#drinks = ["coke","water","soda"]
#dinner = ["grill chicken","birayani","meat"]
#dessert = ["rosho golla","rosh malaiy","tofi"]

#food = [drinks,dinner,dessert]

#print(food[1][2])


#student = ("sajid",20,"Male")

#print(student.count("Male"))
#print(student.index("sajid"))

#for i in student:
    #print(i)

#if "sajid"in student:
    #print("sajid is here!")


#utensils = {"fork","spoon","knife",}
#dishes = {"bowl","plate","cup","knife"}

#utensils.add("napkin")
#utensils.remove("spoon")
#utensils.clear()
#utensils.update(dishes)
#dinner_table = utensils.union(dishes)

#print(utensils.difference(dishes))
#print(utensils.intersection(dishes))

#for i in dinner_table:
    #print(i)



#capitals = {"USA":"Washington DC", "India":"New Delhi","China":"Beijing"}

#capitals.update({"Germany":"Berlin"})
#capitals.update({"USA":"Las Vegas"})
#capitals.pop("China")
#capitals.clear()
#print(capitals["USA"])
#print(capitals.get("India"))
#print(capitals.keys())
#print(capitals.values())
#print(capitals.items())

#for keys,values in capitals.items():
    #print(keys, values)


name = "Rafi sajid"

#if(name[0].islower()):
    #name = name.capitalize()

first_name = name[0:4].upper()
last_name = name[5:].lower()

print(last_name)

name = "rafi sajid@"

#if(name[0].islower()):
    #name = name.capitalize()

first_name = name[0:4].upper()
last_name = name[5:10].upper()
last_symbol = name[-1]

print(last_symbol)


def hello(first_name,last_name,age):
    print("Hello !"+first_name+" "+last_name)
    print("You are "+str(age)+ " years old")
hello("Sajid","Rafi",21 )
