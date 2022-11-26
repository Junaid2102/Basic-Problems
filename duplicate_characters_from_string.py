'''
Write a program to print duplicate characters in a string
'''

str1 = input("Enter the string: ")
str1 = str1.casefold()      # for using caseless
dup = []

for ch in str1:
    if str1.count(ch) > 1:
        if ch not in dup:
            dup.append(ch)
print(*dup)        # * before the list name helps us to multiply the elements in a list and show them like characters