import random
from words import words
import string

def get_valid_words(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_words(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    guessed_letters = set()
    tries = 6

    while len(word_letters) > 0 and tries > 0:
        print('You have', tries ,'tries left and you have guessed these letters: ', ' '.join(guessed_letters))

        wordlist = [letter if letter in guessed_letters else '-' for letter in word]
        print('Current word: ', ' '.join(wordlist))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - guessed_letters:
           guessed_letters.add(user_letter)
           if user_letter in word_letters:
              word_letters.remove(user_letter)

           else:
               tries -= 1
               print('Letter is not in word.')

        elif user_letter in guessed_letters:
           print("You already guessed that letter. Please try again")

        else:
           print('Invalid character. Please try again')

    if tries == 0:
        print('you ran out of tries! the word was', word)
    else:
        print('Congrats you have guessed the word', word)


hangman()











