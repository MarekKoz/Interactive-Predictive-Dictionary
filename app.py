import json
from difflib import get_close_matches


data = json.load(open("data.json"))

def define(word):
    word = word.lower()
    if word in data: 
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        userInput = input("Did you mean %s ? Enter Y for Yes or N for No: " % get_close_matches(word, data.keys())[0])
        if userInput.lower() == 'y':
            return data[get_close_matches(word, data.keys())[0]]
        else:
            return "Sorry, can not figure out which word you have in mind!"
    else:
        return "No such word in dictionary!"

word = input("Enter a word to define: ")
result = define(word)

if type(result) == str:
    print(result)
else:
    for w in result:
        print("\n" + w)