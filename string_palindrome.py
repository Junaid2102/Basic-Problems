'''
    Write a code to print whether a string is palindrome or not
    Muhammad Junaid Alam
'''

x = input()
x = x.casefold()        # for caselesss comparison
rev_x = reversed(x)
if list(x) == list(rev_x):l
    print("Yes")
else:
    print("No")