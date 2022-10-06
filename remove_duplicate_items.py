'''
    Write a code to remove duplicate items from the list
    Muhammad Junaid Alam
'''

my_list = [1, 3, 5, 0, 7, 2, 0, 3, 0, 7, 8, 5]
out = []
for i in my_list:
    if i not in out:
        out.append(i)

print(out)