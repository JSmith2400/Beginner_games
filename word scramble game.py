#number scramble game

import random 

#creates a list of words that can be picked and sets high score to none
words = ["python", "programming", "challenge", "computer"]
high_score = None


def play_game():
    global high_score

    #chooses a word from the list and jumbles them up
    target_word = random.choice(words)
    scrambled = "".join(random.sample(target_word, len(target_word)))

    #creates the 'hint' variable which reveals the first letter in the correct place
    first = target_word[0]
    rest = list(target_word[1:])
    random.shuffle(rest)
    hint = first + "".join(rest)

    print("\nnscramble this word: ", scrambled)

    #sets the users guess and attempts to 0 every time the game is played
    usr_guess = ""
    attempts = 0
                        
    while usr_guess != target_word:
        
        usr_guess = input("Your guess: ").lower()
        attempts += 1

        #if the user guessed the correct word
        if usr_guess == target_word:
            print(f"\nCorrect! You guessed the word in {attempts} attempts.")
            
            #checks if this is a new high score
            if high_score is None or attempts < high_score:
                print("New high score!!")
                high_score = attempts

        #if the user gets it wrong
        else:
            print("Nope, try again!")
            #offers the user a hint every 3 attempts which they can accept or decline
            if attempts % 3 == 0:
                hint_ask = input("would you like a hint? <Y/N>").lower()
                if hint_ask == "y":
                    print(hint)

#main game loop
while True:
    #if this is the first game
    if high_score == None:
        play_ask = input("Would you like to play? <Y/N> ").lower()
        if play_ask == "y":
            play_game()
        else:
            print("Goodbye!")
            break
    #else offer them to play again
    else:
        print(f"\nWould you like to play again? Your current high score is: {high_score} attempts")
        again_ask = input("Select <Y/N> : ").lower()
        if again_ask == "y":
            play_game()
        else:
            print("Goodbye!")
            break
        
        
