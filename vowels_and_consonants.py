'''
Write a program to find the count of vowels and consonants in string
'''

str1 = input("Enter the string: ")
vowels = 0
consonants = 0
str1 = str1.casefold()

for i in range(0, len(str1)):
    if str1[i] == 'a' or str1[i] == 'e' or str1[i] == 'i' or str1[i] == 'o' or str1[i] == 'u':
        vowels += 1
    else:
        consonants += 1

print("Vowels are: ", vowels)
print("Consonants are: ", consonants)