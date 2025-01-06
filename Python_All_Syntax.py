# below program will display the value of the var that print on the screen
my_name = "Arun Kumar";
print("Your name is : "+ my_name+" !");

x = 1
if x == 1:
    # indented four spaces
    print("x is 1.")

# ------------------------- New ------------------------	
myfloat = 7.0
print(myfloat)
myfloat = float(7)
print(myfloat)

print("\n")
one = 1
two = 2
three = one + two
print(" one=1 and two=2, one+two= %d" %three)

print("\n")
hello = "hello"
world = "world"
helloworld = hello + " " + world
if isinstance(helloworld, str):
    print(helloworld+"\n")

print("\n")
#-------------------------------New ----------------
a, b = 3, 4
print("a value is : %d" %a +", b value is : %d" %b)
print("a value is : %d, b value is : %d" % (a,b))

print("\n")
# change this code
mystring = "hello"
myfloat = 10.0
myint = 20

# testing code ----------------------- New -----------
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)

print("\n")
# List and for example 
mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
for x in mylist:
    print("x value in mylist : %d" %x)

print("\n")
numbers = [1,2,3]
strings = ["hello","world"]
names = ["John", "Eric", "Jessica"]

# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
#print(names)
for x in names:
    print(x)

print("\n")
#-----------------New -----------
string1 = "count" * 6
print(string1)
print([1,2,3] * 3)    

print("\n")
#-----------------New -----------
even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)

print("\n")
#-----------------New -----------
# This prints out "John is 23 years old."
name = "John"
age = 23
print("%s is %d years old." % (name, age))


print("\n")
#-----------------New ----------- output : ---  Hello John Doe. Your current balance is $53.44.
data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."
format_string1="Hello"

print(format_string % data)
print("%s %s %s.Your current balance is $%s" % (format_string1,data[0],data[1],data[2]))

print("\n")
#------------- String --------------
astring = "Hello world!"
print("single quotes are ' '")
print("Length of the string : %d" % len(astring))
print("Index of the letter o is : %d" % astring.index("o"))
print("count of letter of l in the string : %d" % astring.count("l"))
#---- from index 3 to 7 it will print that is 'lo w'
print("%s from this string it will display the index of 3 to 7 : %s" % (astring,astring[3:7]))
#------ revers a string -----------
print("easily reverse a string from %s to %s" %(astring,astring[::-1]))
print(astring.upper())
print(astring.lower())
print("To check string %s is Start with Hello is True or False. %s" % (astring,astring.startswith("Hello")))
print("To check string %s is End with asdfasdfasdf is True or False. %s" % (astring,astring.endswith("asdfasdfasdf")))
#------------Split-------------
afewwords = astring.split(" ")
print("After split the string with spces : %s" %afewwords)

# Slicing the string into bits
s = "Strings are awesome!"
print("The first five characters of %s are '%s'" % (s,s[:5])) # Start to 5
print("The next five characters of %s are '%s'" %  (s,s[5:10])) # 5 to 10
print("The thirteenth character of %s is '%s'" %  (s,s[12])) # Just number 12
print("The characters with odd index  of %s are '%s'" % (s,s[1::2])) #(0-based indexing)
print("The last five characters  of %s are '%s'" %  (s,s[-5:])) # 5th-from-last to end

#---------------------------Conditions -----------------
print("\n")
x = 2
print(x == 2) # prints out True
print(x == 3) # prints out False
print(x < 3) # prints out True

name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")

print("\n")
#------------- New IN condition---
name = "John"
if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")

print("\n")
#--------------- IF - ELSE -------------
x = 2
if x == 2:
    print("x equals two!")
else:
    print("x does not equal to two.")


print("\n")
#------------ IF - ELIF - ELSE
status = "inactive"
user_status = "active"

if status == "active":
    # do something
    print("User is active!")
elif user_status == "active":  # else if
    # do something else
    print("User is now active!")
else:
    # do another thing
    print("User is inactive!")

#---------------- IS key word & == ----------------------
print("\n")
x = [1,2,3]
y = [1,2,3]
print(x == y) # Prints out True
print(x is y) # Prints out False because they are different objects in memory  

#---------------- not oparetor ----------------------
print("\n")
print(not False)
print((not False) == (False))

#---------------- LOOP ----------------------
print("\n")
primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)

# Prints out the numbers 0,1,2,3,4
for x in range(5):
   print(x)

print("\n")
# Prints out 3,4,5
for x in range(3, 6):
    print(x)

print("\n")
# Prints out 3,5,7 ----- range(start, stop, step) step: The increment (or decrement) between each number in the sequence.
for x in range(3, 8, 2):
    print(x)

# Prints out 0,1,2,3,4
print("\n")
# -------------------- while loop -----------------
count = 0
while count < 5:
    print(count)
    count += 1  # This is the same as count = count + 1


print("\n")
# -------------------"break" and "continue"
# Prints out 0,1,2,3,4
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

print("\n")
# Prints out only odd numbers - 1,3,5,7,9
for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)



print("\n")
print("------------------ This is from Python_All_Syntax.py -----------")