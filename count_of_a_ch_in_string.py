'''
Write a program to find the count of a character in a string
'''

str1 = input("Enter the string: ")
str2 = input("Enter the character you wanna find: ")

str1 = str1.casefold()
count = 0
for i in range(0, len(str1)):
    if str1[i] == str2:
        count += 1

print(count)