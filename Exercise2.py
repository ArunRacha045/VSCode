#Exercise

# You will need to write a format string which prints out the data using the following syntax: Hello John Doe. Your current balance is $53.44.

data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."
format_string1="Hello"

print(format_string % data)
print("%s %s %s.Your current balance is $%s" %(format_string1,data[0],data[1],data[2]))
print("------------------ This is from Exercise2.py -----------")