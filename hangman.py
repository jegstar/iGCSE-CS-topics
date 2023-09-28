def generateClue(guessedLetters, wordToGuess):
    output = ''
    for i in range(len(wordToGuess)):
        if wordToGuess[i] in guessedLetters:
            output += wordToGuess[i] +' '
        else:
            output += '_ '

    return output

userGuessedLetters = ''
lives = 5
hiddenWord = 'alpaca'

clue = generateClue(userGuessedLetters, hiddenWord)
print(clue)
print("You have", lives, "lives remaining")
while lives > 0 and '_' in clue:
    # validate input
    letter = input("Enter a single letter").lower()

    while not letter.isalpha() or len(letter) != 1:
        print("U dum or wot")
        letter = input("Enter a single letter").lower()

    userGuessedLetters += letter

    if not letter in hiddenWord:
        lives -= 1
    
    clue = generateClue(userGuessedLetters, hiddenWord)
    print(clue)
    print("You have", lives, "lives remaining")

if lives == 0:
    print("u ded")
else:
    print("u not ded")


