import random

list=['UMBRELLA','CHETAH','TENNIS','DENTIST','CUSHION']
word= random.choice(list)
chances= len(word)
guess_word='-'*len(word)

print("WELCOME TO THE HANGMAN GAME")
print(f"Guess the complete word")

while chances != 0:
    print(guess_word)
    user_input= input("Enter a letter: ").upper() # to convert user input to uppercase
    if user_input in word:
        for i in range(len(word)):
            if user_input==word[i]:
                guess_word= guess_word[:i]+user_input+guess_word[i+1:]

        if guess_word==word:
            print("Congratulations. You guessed the word")
            break

    else:
        chances-=1
        print("Thats a wrong guess")
        print(f"Total have {chances} chances left")

if chances==0:
    print(f'Sorry you run out of chances. The word was {word}')