sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = []
for word in words:
      if word != "the":
          word_lengths.append(len(word))
print(words)
print(word_lengths)

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = [int(x) for x in numbers if x > 0]
print(newlist)


lst = []
del lst
# print(lst) # --- This will give error NameError: name 'lst' is not defined

lst = [1, 2, 3, 4, 5]
lst.insert(1, 6)
del lst[0]
lst.append(1)
print(lst)

lst = [1, [2, 3], 4]
print(lst[1])
print(len(lst))

my_list = [8, 10, 6, 2, 4]
my_list.sort()
print(my_list)

lst = [5, 3, 1, 2, 4]
print(lst)
lst.reverse()
print(lst)

lst = ["D", "F", "A", "Z"]
lst.sort()
print(lst)

# ----------- reference of list_2 as list_1 or list_2 = list_1[:]
list_1 = [1]
list_2 = list_1
list_1[0] = 2
print(list_2)

# ---- my_list[start:end] output is: [8, 6]
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)

#--- start from 3 to end
my_list = [10, 8, 6, 4, 2]
new_list = my_list[3:]
print(new_list)

# --------- in and not in
my_list = [0, 3, 12, 8, 2]
print(5 in my_list)
print(5 not in my_list)
print(12 in my_list)

# --- removing the duplicated values
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
unique_list = []  # New list to store unique elements

for item in my_list:
    if item not in unique_list:
        unique_list.append(item)  # Add only if not already in list

print("The list with unique elements only:")
print(unique_list)

# my_list.remove(value) --- removes by value and del or pop(index) to remove by index. my_list.pop(2) or del my_list[2]


