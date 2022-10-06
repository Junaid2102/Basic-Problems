'''
    Write a code to print duplicate items
    Muhammad Junaid Alam
'''

my_list = [1, 3, 5, 0, 7, 2, 0, 3, 0, 7, 8, 5]
out = []
for i in my_list:
    count = my_list.count(i)
    if count > 1:
        if out.count(i) == 0:
            out.append(i)

print(out)