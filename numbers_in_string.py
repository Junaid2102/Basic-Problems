'''
Write a program to check whether string have all numeric data or not
'''

str1 = input("Enter the string: ")
if str1.isnumeric():
    print("String contains numeric data")
else:
    print("String contains other data than numeric")