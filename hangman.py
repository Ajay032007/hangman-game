import random

words = ["apple", "chair", "table", "phone"]
word = random.choice(words)

guessed = ["_"] * len(word)
attempts = 5

print("Hangman Game")

while attempts > 0:
    print("Word:", " ".join(guessed))
    guess = input("Enter letter: ").lower()

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
        print("Correct")
    else:
        attempts -= 1
        print("Wrong, attempts left:", attempts)

    if "_" not in guessed:
        print("You win! Word:", word)
        break

if "_" in guessed:
    print("You lose! Word:", word)