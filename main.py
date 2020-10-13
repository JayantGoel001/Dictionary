import json

dictionary = dict()


def printResult(modified_word):
    for i in range(len(dictionary[modified_word])):
        print(str(i + 1) + "." + dictionary[modified_word][i])


with open('data.json') as f:
    dictionary = json.load(f)

word = input("Enter A Word:\n")
if word in dictionary:
    printResult(word)
elif word.title() in dictionary:
    printResult(word.title())
elif word.upper() in dictionary:
    printResult(word.upper())
elif word.lower() in dictionary:
    printResult(word.lower())
else:
    print("Oops Result Not Found")
