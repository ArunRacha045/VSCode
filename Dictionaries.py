phbook = {
    "ABC" : 123,
    "DEF" : 456,
    "XYZ" : 789
}

zipCode = {"MA" : 12143 ,"NY" : 44552 , "TX" : 54789 }

print(f"{phbook}\n{zipCode}")

for name,number in phbook.items():
    print(f" Name is : {name} Number is : {number}")

# delete the key value from Dir
del zipCode["TX"]
for name,number in zipCode.items():
    print(f" Name is : {name} Number is : {number}")

# delete the key value from dir
zipCode.pop("NY")
#print(zipCode)
if "NY" not in zipCode:
    print(f"NY is not in : {zipCode}")

# Add a new value
zipCode.update({"NY": 44552})
#print(zipCode)
if "NY" in zipCode:
    print(f" NY is in : {zipCode} ")

# Add a new value
zipCode["CA"]=98765
print(f"CA added : {zipCode}")

# ------------ Sort by Key ----------
# Sort the dictionary by values
sorted_by_value = sorted(zipCode.items(), key=lambda x: x[0])

# Convert the sorted list of tuples back into a dictionary
sorted_dict_by_value = dict(sorted_by_value)

print("Sorted by values:", sorted_dict_by_value)
print("-------------- This is from Dictionaries.py ----------------------")

d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
d3 = {}

for item in (d1, d2):
    d3.update(item)

print(d3)

colors = (("green", "#008000"), ("blue", "#0000FF"))

colors_dictionary = dict(colors)
print(colors_dictionary)

my_dictionary = {"A": 1, "B": 2}
copy_my_dictionary = my_dictionary.copy()

