a=1
b=2
sum = lambda a,b : a+b
c= sum(a,b)
print(c)

sub = lambda a,b : b-a
c=sub(a,b)
print(c)

mul = lambda a,b : a*b
c=mul(a,b)
print(c)

#--------Odd------
l = [2,4,7,3,14,19]
for i in l:
    # your code here
    my_lambda = lambda x : (x % 2) == 1
    print(my_lambda(i))

my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [1, 2, 3, 4, 5]

results = list(map(lambda x, y: (x, y), my_strings, my_numbers))

print(results)