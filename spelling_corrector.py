from textblob import TextBlob, Word

carry_on = False


def checkIfWordCorrect(word):
    l = Word(word).spellcheck
    if (l[0][1] == "1.0"):
        return True
    return False


while (carry_on):
    word = input("Please enter the word : ")
    result = checkIfWordCorrect(word)
    if (result):
        print("Bingo, your word is correct.")
    else:
        print("Sorry your word is not correct. We have corrected it for you.")
        correct_word = TextBlob(word).correct
        print("The corrected word is :" + correct_word)

    play_again = input("Do you want to continue. Yes/No")
    if (play_again == "Yes"):
        carry_on = True
    else:
        carry_on = False
