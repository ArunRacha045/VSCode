print('Greg\'s book.')
print("'Greg's book.'")
print('"Greg\'s book."')
print("Greg\'s book.")
# print('"Greg's book."')  # ---- Error in this line

#anything = float(input("Enter a number: "))
#something = anything ** 2.0
#print(anything, "to the power of 2 is", something)

table = 2
list(map(lambda i: print(f"{table} X {i} = {table*i}"), range(1, 11)))

table = 4
m = map(lambda i: print(f"{table} X {i} = {table*i}"), range(1, 11))
list(m)

my_list = [0, 3, 12, 8, 2]
print(list(my_list))

numbers = [1, 8, 3, 6, 4, 7, 10, 2]
print(numbers)
#print(sorted(numbers))
result = sorted(filter( lambda x : x%2==0, numbers))
print(list(result))


#----- desk.dataframe 
#import dask.dataframe as dd
#df = dd.read_csv('large_dataset.csv')

