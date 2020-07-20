# INF360 - Programming in Python
# Seth Whitaker
# Assignment 4
# Mad Libs
# 07/03/2020

import os

# Main function executes automatically 
def main():

    # default madlib text file path
    textFilePath = "madlib.txt"
    

    # First check to see if the default file exists in working dir
    print("Checking to see if madlib.txt exists in current working directory...")

    if os.path.isfile("madlib.txt"):
        print("File found!")
    else:
        # if default file does not exist, get file path from user
        while True:
            print("File not found.")
            textFilePath = input("Please enter the path of a madlibs text file:\n")
            if os.path.isfile(textFilePath):
                print("File found!")
                break

    # Open file
    textFile = open(textFilePath)
    # Prompt user to replace key words
    newText = enterWords(textFile)
    # Give feedback to user on the new file
    print(newText)
    # Close file
    textFile.close()

    # Create a file to store results
    # NOTE: if 101+ files are created, madlib-result.txt will be overwritten
    newFilePath = "madlib-result"

    # Check to see if file already exists
    if os.path.isfile(newFilePath+".txt"):
        # if it does, append a digit (1-100) to the end
        for i in range(1, 101):
            if not os.path.isfile(newFilePath+str(i)+".txt"):
                newFilePath = newFilePath+str(i)
                break

    # add .txt extension
    newFilePath = newFilePath + ".txt"

    # create file
    newFile = open(newFilePath, 'w')
    # write result text to file
    newFile.write(newText)
    # give feedback to user
    print("Result saved to file " + newFilePath)
    # close the file
    newFile.close()

    

    
    
# This function checks to see if candidate word is a key word
#       and prompts user to enter a replacement
def replaceWord(word):
    # new word to replace existing word
    replacement = word
    # if word is a keyword, prompt user to replace it
    if word == "NOUN" or word == "VERB":
        replacement = input("Enter a " + word.lower() + ": ")
    elif word == "ADJECTIVE" or word == "ADVERB":
        replacement = input("Enter an " + word.lower() + ": ")
    
    return replacement



# This function iterates through the text of the madlibs file and 
#       searches for words that start with a capital letter, and prompts
#       user to replace the words if they are key words (NOUN, VERB, ADJECTIVE, ADVERB)
def enterWords(file):

    # read text from file
    text = file.read()

    # Determines when to end the loop 
    endoftext = False

    # keep track of position in text
    index = 0
    while not endoftext:

        # find uppercase letter
        while len(text) > index and not text[index].isupper():
            index += 1

        # save start of word position
        wordStart = index
        
        # find where the word stops being uppercase
        while len(text) > index and text[index].isupper():
            index += 1

        # check if end of file
        if len(text) <= index:
            endoftext = True

        # Check if word is key word and replace it if it is
        newWord = replaceWord(text[wordStart:index])

        # If word got replaced
        if newWord != text[wordStart:index]:
            # insert into text
            text = text[0:wordStart] + newWord + text[index:len(text)]
            # adjust position in new text
            index = wordStart+len(newWord)

    return text

        
# call main at end of file
main()