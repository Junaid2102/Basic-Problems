'''
Write a program to print whether strings are anagram or not
'''

str1 = input("Enter the string: ")
str1 = str1.casefold()      # for using caseless
str2 = input("Enter the second string: ")
str2 = str2.casefold()

if sorted(str1) == sorted(str2):
    print("Strings are anagram")
else:
    print("Strings aren't anagram")