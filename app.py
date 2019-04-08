import json
from difflib import get_close_matches

#Import the data from the json file and store it
data = json.load(open("data.json"))

def define(word):
    #Account for capitalization (RaIn), acronyms (USA, NASA, etc.), countries/states (Texas, etc.)
    word = word.lower()
    if word in data: 
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    
    #If the word entered by the user doesn't match any of the words in the 
    #dictionary, find the closest word and ask if the user wanted the definition of 
    #the predicted word.

    #Predicted word is based on finding the difference ratio 
    #between the input word and each word in the dictionary
    elif len(get_close_matches(word, data.keys())) > 0:
        userInput = input("Did you mean %s ? Enter Y for Yes or N for No: " % get_close_matches(word, data.keys())[0])
        if userInput.lower() == 'y':
            return data[get_close_matches(word, data.keys())[0]]
        else:
            return "Sorry, can not figure out which word you have in mind!"
    else:
        return "No such word in dictionary!"

#Ask the user to enter a word to be defined
word = input("Enter a word to define: ")
result = define(word)

#Depending on the type of the returned value, display a different result message.
#If there is an error, display the error.
#If the result is a list of definitions, display each definition on its own line.
if type(result) == str:
    print(result)
else:
    for w in result:
        print("\n" + w)