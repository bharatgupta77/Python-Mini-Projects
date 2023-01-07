from textblob import TextBlob, Word

carry_on = True

"""
function to check whether spelling of word is correct.
Word Class - A simple word representation. 
Includes methods for inflection, translation, and WordNet integration.
"""


def checkIfWordCorrect(word):
    # spellcheck method returns a list of tuples which consist of a correct_word/word having same rhyme
    # and there matching accuracy to the word (range 0-1). (1.0 means correct word).

    spell_list = Word(word).spellcheck()
    for item in spell_list:
        if (item[1] == 1.0):
            return True
    return False


while (carry_on):
    word = input("Please enter the word : ")
    result = checkIfWordCorrect(word)
    if (result):
        print("Bingo, your word is correct.")
    else:
        print("Sorry your word is not correct. We have corrected it for you.")

        # Return obj which is of TextBlob type after correcting it
        correct_word = TextBlob(word).correct()
        print("The corrected word is : " + str(correct_word))

    play_again = input("Do you want to continue, y-Yes/n-No : ")
    if (play_again == "y"):
        carry_on = True
    else:
        print(" Adios :) . See you next time....")
        carry_on = False
