def multi1(first, second, third, *therest):
    print("First: %s" %(first))
    print("Second: %s" %(second))
    print("Third: %s" %(third))
    print("And all the rest... %s" %(list(therest)))

multi1(1, 2, 3, 4, 5)

def multi2(first, second, third, **options):
    if options.get("action") == "sum":
        print("The sum is: %d" %(first + second + third))

    if options.get("number") == "first":
        return first

result = multi2(1, 2, 3, action = "sum", number = "first")
print("Result: %d" %(result))

def multi3(a, b, c, *args):
    return len(args)

def multi4(a, b, c, **kwargs):
    return kwargs["magicnumber"] == 7


# test code
if multi3(1, 2, 3, 4) == 1:
    print("Good.")
if multi3(1, 2, 3, 4, 5) == 2:
    print("Better.")
if multi4(1, 2, 3, magicnumber=6) == False:
    print("Great.")
if multi4(1, 2, 3, magicnumber=7) == True:
    print("Awesome!")