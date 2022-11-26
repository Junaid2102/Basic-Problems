'''
Write a program to print whether strings are anagram or not
'''
from collections import Counter
str1 = input("Enter the string: ")
str1 = str1.casefold()      # for using caseless
dup = Counter(str1)
# print(dup)
for i in str1:
    if dup[i] == 1:
        print(i)

