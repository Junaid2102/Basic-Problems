'''
Write a program to reverse the string
'''


def simpreverse(str1):
    str2 = ""
    for i in str1:
        str2 = i+str2
    print(str2)

# Recursively


def reverseString(str1):
    if len(str1) == 0:
        return
    temp = str1[0]
    reverseString(str1[1:])
    print(temp, end="")


str1 = input("Enter the string: ")
reverseString(str1)
print('\n')
simpreverse(str1)