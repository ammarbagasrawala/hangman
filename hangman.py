import random
from words import word_list

def get_word():
    word=random.choice(word_list)
    return word.upper()

def play(word):
    word_completion = "_" * len(word)
    guessed=False
    guessed_letters=[]
    guessed_words=[]
    tries=6
    print("Let's Play Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")

    while not guessed and tries>0:
        guess=input("Please guess a letter or a word: ").upper()
        if len(guess)==1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter ",guess)
            elif guess not in word:
                print(guess," is not in the word.")
                tries-=1
                guessed_letters.append(guess)
            else:
                print("good job,", guess ," is in the word!")
                guessed_letters.append(guess)
                words_as_list=list(word_completion)
                indices=[i for i,letter in enumerate(word) if letter == guess]
                for index in indices:
                    words_as_list[index]=guess
                word_completion="".join(words_as_list) #to make it into a string
                if "_" not in word_completion: 
                    guessed=True
        
        elif len(guess)==len(word()) and guess.isalpha():
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
        word=get_word
        play(word)

if __name__=="__main__":
    main()