'''
    Print a string is palindrome or not!!
'''


def palindrome(sentence):
    l = [i for i in sentence]
    rl = l[::-1]
    print(rl)
    # print(l)
    if (l == rl):
        print("Is Palindrome!!")
    else:
        print("Not palindrome!!")


sentence = input("Enter the Sentence: ")
palindrome(sentence)
