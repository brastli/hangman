import random
''' import tool'''
class user:
    pass
''' create the class for user'''


class import_file:
    pass
''' create the class for import_file'''

class imported_file(import_file):
    pass
''' create the  inheritance relationship class for imported_file'''

class target_word:
    pass
''' create the class for target_word'''

class length:
    pass
''' create the class for length'''

class count:
    pass
''' create the class for count'''

class guessed:
    pass
''' create the class for guessed'''

class limit:
    pass
''' create the class for limit'''

class display:
    pass
''' create the class for display'''

user1 = user()
''' create the user'''
print("\nWelcome\n")
name = input("Please enter your name: ")
user1.name = name
print("Hello " + user1.name + " , enjoy the game")
'''get the name of the user and welcome the user'''
file1 = import_file()
file1.name = 'x.txt'
text = imported_file()
text.to_read = open(file1.name, 'r')
text.to_read = text.to_read.read()
text.to_read = text.to_read.split()
a = len(text.to_read)
b = random.randint(0, a)
'''read the txt file and select a random word'''
word_to_guess = target_word()
word_to_guess.word = text.to_read[b]
length_word = length()
length_word.word = len(word_to_guess.word)
'''get the length of the random word'''
worng_times = count()
worng_times.guess = 0
'''create a total count for user'''
guessed_word = guessed()
guessed_word.guessed = []
'''create the the guessed word'''
guess_limit = limit()
guess_limit.guess = 5
'''create a limit'''
guessed_display = display()
guessed_display.show = '_' * length_word.word
'''create the display for gussing the word'''


def hangman():
    guess = input("This is the word you need to guess: " + guessed_display.show + " Enter your guess: \n")
    guess = guess.strip()
    '''get the variables'''

    if guess in word_to_guess.word:
        guessed_word.guessed.extend([guess])
        index = word_to_guess.word.find(guess)
        word_to_guess.word = word_to_guess.word[:index] + "_" + word_to_guess.word[index + 1:]
        guessed_display.show = guessed_display.show[:index] + guess + guessed_display.show[index + 1:]
        '''to replace the _ with the correct guessed letter'''
        print(guessed_display.show + "\n")

    elif guess in guessed_word.guessed:
        print("Try again.\n")
        '''tell the user that the letter the user guessed is wrong'''
    else:
        worng_times.guess += 1

        if worng_times.guess == 1:

            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |        \n"
                  "  |        \n"
                  "__|__\n")
            print("Wrong guess. You have " + str(guess_limit.guess - worng_times.guess) + " guesses\n")

        elif worng_times.guess == 2:

            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /   \n"
                  "  |        \n"
                  "__|__\n")
            print("Wrong guess. You have " + str(guess_limit.guess - worng_times.guess) + " guesses\n")

        elif worng_times.guess == 3:

            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|  \n"
                  "  |        \n"
                  "__|__\n")
            print("Wrong guess. You have " + str(guess_limit.guess - worng_times.guess) + " guesses\n")

        elif worng_times.guess == 4:

            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    /   \n"
                  "__|__\n")
            print("Wrong guess. You have " + str(guess_limit.guess - worng_times.guess) + " guess\n")

        elif worng_times.guess == 5:
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Wrong guess. You lost\n")
            print("The word you need to guess is: ", guessed_word.guessed, word_to_guess.word)
            '''tell the user how many chances that the user has'''
    if word_to_guess.word == '_' * length_word.word:
        print("You have win the game")
        '''tell the user lose the game'''
    elif worng_times.guess != guess_limit.guess:
        hangman()
        '''repeat the hanngman'''

hangman()
'''start the game'''
