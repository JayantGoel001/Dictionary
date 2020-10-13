import json

dictionary = dict()
with open('data.json') as f:
    dictionary = json.load(f)

word = input("Enter A Word:\n")
if word in dictionary:
    for i in range(len(dictionary[word])):
        print(str(i)+"."+ dictionary[word][i])
else:
    print("Oops Result Not Found")