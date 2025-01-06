<<<<<<< HEAD
#String Funtions
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

str1 = "Test"
str2 = "String"
value = 100.00
print(str1+'\n'+str2+'\n'+str(value))
print(str1, str2, value, sep="\t")
print(f"str1 value is : {str1} \n str2 value is : {str2} \n value is : {value}")
print(f"{str1}\n{str2}\n{value:.2f}")
print("{}\n{}\n{}".format(str1, str2, value))


print("\n")
=======
#String Funtions
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

str1 = "Test"
str2 = "String"
value = 100.00
print(str1+'\n'+str2+'\n'+str(value))
print(str1, str2, value, sep="\t")
print(f"str1 value is : {str1} \n str2 value is : {str2} \n value is : {value}")
print(f"{str1}\n{str2}\n{value:.2f}")
print("{}\n{}\n{}".format(str1, str2, value))


print("\n")
>>>>>>> b1ad062dedd5b5b7f06ee2e2640b7a05f205ccc9
print("------------------ This is from StringFunctions.py -----------")