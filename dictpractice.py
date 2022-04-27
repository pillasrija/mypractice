# write a python program to sort(ascending and descending) a dictionary by value
import operator
d = {1:2, 3:4, 4:3, 2:1, 0:0}
print('original dictionary :',d)
sorted_d = sorted(d.items(),key=operator.itemgetter(1))
print('Dictionary in ascending order by value:',sorted_d)
sorted_d = dict(sorted(d.items(),key=operator.itemgetter(1),reverse=True))
print('Dictionary in descending order by value:',sorted_d)


# write a python program to add a key to a dict
d = {0:10, 1:20}
print(d)
d.update({2:30})
print(d)

# write a python program to check whether a given key already exist in a dict

d = {1:10, 2:20, 3:30, 4:40, 5:50, 6:60}
def is_key_present(x):
    if x in d:
        print('key is present in the dictionary')
    else:
        print('key is not present in the dictionary')
is_key_present(5)
is_key_present(9)

# write a python script to generate and print a dictionary that contains a number in the from (x,x*x)

n = int(input("Input a number"))
d = dict()
for x in range(1,n+1):
    d[x] = x*x

print(d)



