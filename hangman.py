import random
from words import word_list

def get_word():
    word=random.choice(word_list) #gets a random word from words.py
    return word.upper() #returns upper case

def play(word):
    word_completion = "_" * len(word) #for blanks
    guessed=False
    guessed_letters=[] # storing guessed letters
    guessed_words=[] #storing guessed words
    tries=6 #6 tries since displayhangman has 0 to 6 (7)
    print("Let's Play Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")

    while not guessed and tries>0: 
        guess=input("Please guess a letter or a word: ").upper() #user input
        if len(guess)==1 and guess.isalpha(): #when only one letter is entered
            if guess in guessed_letters: 
                print("You already guessed the letter ",guess)
            elif guess not in word:
                print(guess," is not in the word.")
                tries-=1
                guessed_letters.append(guess)
            else:
                print("good job,", guess ," is in the word!")
                guessed_letters.append(guess)
                words_as_list=list(word_completion) #making the underscore wala variavle into a list 
                indices=[i for i,letter in enumerate(word) if letter == guess] #one to extract index for letter replacemnet in underscores
                for index in indices:
                    words_as_list[index]=guess #replacing underscore with correct guess
                word_completion="".join(words_as_list) #to make it into a string again
                if "_" not in word_completion: #if the whole word is guessed
                    guessed=True
        
        elif len(guess)==len(word) and guess.isalpha(): # when a whole word is guessed
            if guess in guessed_words:
                print("You already guessed the word ",guess)
            elif guess!=word:
                print(guess," is not the word.")
                guessed_words.append(guess)
                tries-=1
            else:
                guessed=True
                word_completion=word
        else:
            print("Not A Valid Guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed: 
        print("Congrats, you guessed the word! you Win!!")
    else:
        print(f"sorry, you ran out of tries. the word was {word}. maybe next time")


def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]

def main():
    word="AMMAR" #get_word()
    play(word)
    while input("Play again? (Y/N) ").upper() == "Y":
        word="AMMAR" #get_word()
        play(word)

if __name__=="__main__":
    main()

