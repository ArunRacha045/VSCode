
def my_function():
    print("Hello From My Function!")

# print(a simple greeting)
my_function()
print("\n")

def my_function_with_args(username, greeting):
    print("Hello, %s, From My Function!, I wish you %s"%(username, greeting))

#prints - "Hello, John Doe, From My Function!, I wish you a great year!"
my_function_with_args("John Doe", "a great year!")
print("\n")    

def sum_two_numbers(a, b):
    return a + b

# after this line x will hold the value 3!
x = sum_two_numbers(1,2)
print("\n")


#------- Print a table -------
def table(num):
    for i in range(1,11):
        print(" %d X %d = %d" %(num,i,num*i))

#--- Print table
table(2)
print("\n")
#---- Calculation ------
def cal_add_sub_mul(cal,num1,num2):
        if cal=="add":
             print("Add of %d + %d =%d" %(num1,num2,num1+num2))
        elif cal=="sub":
             print("Sub of %d - %d =%d" %(num1,num2,num1-num2))
        else:
             print("Multi of %d * %d =%d" %(num1,num2,num1*num2))     

#---- Calculation ------
cal_add_sub_mul("add",6,4)
cal_add_sub_mul("sub",6,4)
cal_add_sub_mul("multi",6,4)
print("\n")

# ------- Number or a String
def num_string(check1):
     if isinstance(check1,str):
          print("%s is a String" %check1)
     if isinstance(check1,int):
          print("%d is a Number" %check1)
num_string("Arun")
num_string(120)
print("\n")


#-------- List examples
def list_add_print():
     mylist = []
     mylist.append("Apple")
     mylist.append("Cat")
     mylist.append("Egg")
     mylist.append("Bus")
     mylist.append("Dog")
     print("%d count of the list items" %len(mylist))
     mylist.insert(5,"Egg")
     print("Number of Eggs in the List is : %d" %mylist.count("Egg"))
     for n in mylist:
          print(n)
     mylist.reverse()
     print("\n After reverse")
     for n in mylist:
          print(n)
     mylist.sort()
     print("\n After Sort")
     for n in mylist:
          print(n)
     mylist.remove("Egg")
     print("\n After Remove Egg")
     for n in mylist:
          print(n)
     print("\n Index of Cat %d " %mylist.index("Cat"))
     mylist.clear()
     print(mylist)               
list_add_print()

print("------------------ This is from Functions.py -----------")