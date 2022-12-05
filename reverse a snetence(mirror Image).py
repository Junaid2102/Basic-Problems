'''
    Print a sentence in a reverse order (mirror Image)
'''


def reverseWord(sentence):
    l = [i for i in sentence]
    # print(l)
    nl = l[::-1]
    print(nl)
    print(''.join(str(i) for i in nl))


sentence = input("Enter the Sentence: ")
reverseWord(sentence)