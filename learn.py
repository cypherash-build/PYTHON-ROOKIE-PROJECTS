print("Down Payment calculator ")
price = input("WHats the price of property? ")
credit_good = True
if credit_good:
    down_payment = int(price)/10
    result = f' you have to pay {down_payment}'
    print(result)
else:
    down_payment = int(price)/5
    result = f' you have to pay {down_payment}'
    print(result)

print("thank You")

# ***************************************** INTELLIGENT ADVISOR ***********************************************
temp = input("Whats the temperature outside?")
if int(temp) <= 10:
    print("Its a cold day , keep yourself warm")
elif int(temp) >= 30:
    print("Its A sunny day , stay hydrated ")
else:
    print("Its the perfect weather")

print("enjoy your day ")

# *************************************** CHARACTER LIMIT ENFORCER **********************************************

name = input("Whats your name ")
if len(name) <= 3:
    print("Name should be at least 3 characters")
elif len(name) >= 10:
    print("Name cant be more than 10 characters")
else:
    print("Name looks good")
print("have a nice day!")

# ************************************* POUND TO KILOS AND VICE VERSA *******************************************
q = input(''' Which calc You wanna use 
               { 0 } : Pounds To KILOS
               { 1 } : Kilos TO POUNDS
               ''')
weight = input("Enter Your Weight")
if int(q) == 0:
    result = int(weight)/2.205
    print(f"you weigh {result} KILOS")
elif int(q) == 1:
    result = int(weight)*2.205
    print(f'you weigh {result} in POUNDS')
else:
    print('''please Select a unit FROM "0" and "1" ''')
print("Have a nice day")

# ****************************************** CHRISTMAS TREE MAKER *************************************************
i = input("HOW MUCH LONG U WANT YOUR CHRISTMAS TREE? ")
x = 0
y = int(i)
z = int(i)-1
while int(x) <= int(i) or int(y) == 0:
    print(" " * int(y), "*" * int(x), "*" * int(x))
    x = x + 1
    y = y - 1
print(" " * z, "||")
print(" " * z, "||")
print("done")
