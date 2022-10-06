'''
    Write a code that prints all the zeroes from the list to the end of the list
    Muhammad Junaid Alam
'''

my_list = [1, 3, 5, 0, 7, 2, 0, 3, 0, 7, 8, 5]
j = 0
for i in range(len(my_list)):
    if my_list[i] != 0:
        my_list[j], my_list[i] = my_list[i], my_list[j]
        j+=1

print(my_list)