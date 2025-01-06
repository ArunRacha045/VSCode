#If elif else
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

age = 16
required_age = 18

if age >= required_age:
    # do something
    print("You are eligible to vote!")
elif age == 16:  # else if
    # do something else
    print("You are just about to turn 18!")
else:
    # do another thing
    print("You are not eligible to vote yet.")

print("------------------ This is from If_elif_else.py -----------")