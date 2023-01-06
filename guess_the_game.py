import random as r


def guess_the_number(num):

    # Total tries are 4
    no_of_tries = 4

    # Counter is maintained for manipulation
    tries_counter = no_of_tries

    # Normal counter for tracking ith try
    i = 0
    while (tries_counter > 0):
        print("Guess the number between 0-20")
        n = int(input())

        # if guess is greater than number
        if (n > num):
            print(
                "Oops, not correct. Number is lesser than your guess. No. of tries left = " + str(tries_counter - 1) + ". :( .")
        # if guess is that number
        elif (n == num):
            try_suffix = "tries"
            if (i == 1):
                try_suffix = "try"
                print("Bingo, you guess the correct number in " +
                      str(i+1) + " " + str(try_suffix) + ". :) .")
                return
            else:
                print("Bingo, you guess the correct number in " +
                      str(i+1) + " " + str(try_suffix) + ". :) .")
                return

        # if guess is lesser than the number
        else:
            print(
                "Oops, not correct. Number is greater than your guess. No. of tries left = " + str(tries_counter - 1) + ". :( .")

        # doing incrementing and decrementing operations for calculating i try and remaining tries.
        i = i+1
        tries_counter = tries_counter - 1

    # if all tries are exhausted then inform player and reveal the number
    if (i == no_of_tries):
        print("Yikes.... No tries Left. The number was " +
              str(num) + " .Try again next time. :( :(")


num = int(r.randint(1, 19))
guess_the_number(num)
