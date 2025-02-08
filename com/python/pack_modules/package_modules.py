def table1(num):
    print("From Table1 in package_modules.py \n")
    for i in range(1,11):
        print(" %d X %d = %d" %(num,i,num*i))

def strinfun1(astring):
    #String Funtions
    print("From Stringfunc1 in package_modules.py \n")
    print("\n")
    #------------- String --------------
    print("single quotes are ' '")
    print("Length of the string : %d" % len(astring))
    print("Index of the letter r is : %d" % astring.index("r"))
    print("count of letter of u in the string : %d" % astring.count("u"))
    #---- from index 3 to 7 it will print that is 'lo w'
    print("%s from this string it will display the index of 1 to 3 : %s" % (astring,astring[1:3]))
    #------ revers a string -----------
    print("easily reverse a string from %s to %s" %(astring,astring[::-1]))
    print(astring.upper())
    print(astring.lower())
