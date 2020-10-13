import json
from difflib import get_close_matches

dictionary = dict()

with open('data.json') as f:
    dictionary = json.load(f)


def printResult(modified_word):
    for i in range(len(dictionary[modified_word])):
        print(str(i + 1) + "." + dictionary[modified_word][i])


input_word = input("Enter A Word:\n")
words = get_close_matches(input_word, [key for key, value in dictionary.items()])
for word in words:
    if word != input_word:
        print("Did You Mean \033[1m" + word + "\033[0m")
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
