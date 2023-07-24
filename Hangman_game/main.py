import random

def mask_word(word, guessed_letters):
    return "".join([c if c.lower() in guessed_letters else "-" for c in word])

def menu(win_count=0, loss_count=0):
    choice = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: > ').lower()
    if choice == "results":
        print(f"You won: {win_count} times")
        print(f"You lost: {loss_count} times")
    return choice

def initialize_game():
    word_list = ["python", "java", "swift", "javascript"]
    word = random.choice(word_list)
    attempts = 8
    guessed_letters = []
    word_progress = "-" * len(word)
    return word, attempts, guessed_letters, word_progress

def hangman():
    win_count = 0
    loss_count = 0

    while True:
        word, attempts, guessed_letters, word_progress = initialize_game()
        plural = "s" if attempts != 1 else ""
        print(f"H A N G M A N  #{attempts} attempt{plural}")

        choice = menu(win_count, loss_count)
        if choice == "exit":
            print("Thanks for playing!")
            break

        while choice == "play" and attempts > 0:
            print(f"\n{word_progress}")
            letter = input("Input a letter: > ")

            if letter in guessed_letters:
                print("You've already guessed this letter.")
            elif len(letter) != 1:
                print("Please, input a single letter.")
            elif not letter.islower() or not letter.isalpha():
                print("Please, enter a lowercase letter from the English alphabet.")
            else:
                guessed_letters.append(letter)
                if letter in word:
                    word_progress = mask_word(word, guessed_letters)
                    if word == word_progress:
                        print(f"You guessed the word {word}!\nYou survived!")
                        win_count += 1
                        break
                else:
                    attempts -= 1
                    plural = "" if attempts != 1 else "s"
                    print(f"That letter doesn't appear in the word. #{attempts} attempt{plural}")

        if attempts == 0:
            print(f"\nYou Lost!\nYou lost: {loss_count} times.")
            loss_count += 1

hangman()
