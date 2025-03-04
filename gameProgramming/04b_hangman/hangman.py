import random 
wordList = 'lilwayne meekmill lildurk money pineforst icecream lilpoppa whiteboy yeezy zachariah slot conerback nickle dummy scott youngboy williams jackson tea chicken football sports gherbo rylo nocap youngthug kodakblack partynextdoor jcole rodwave'.split()
#.split() will split a string into separate elements, by default based on SPACE
# code review by Aidan Moody

# VARIABLE_NAMES that are ALL CAPS AREE CONSTANTS and not meant to change
HANGMAN_BOARD = ['''
    +----+
         |        
         |        
         |        
         |        
       =====''', '''
    +----+
    O    |        
         |        
         |        
         |        
       =====''', '''   
    +----+
    O    |        
    |    |        
         |        
         |        
       =====''', '''
    +----+
    O    |        
    |\   |        
         |        
         |        
       =====''', '''
    +----+
    O    |        
   /|\   |        
         |        
         |        
       =====''', '''
    +----+
    O    |        
   /|\   |        
     \   |        
         |        
       =====''', '''
    +----+
    O    |        
   /|\   |        
   / \   |        
         |        
       =====''']

def getRandomWord(wordList):
    wordIndex = random.randint(0 , len(wordList) - 1)
    # len(listName) - 1 is most common way to prevent index out of range errors
    # print(wordIndex)
    return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_BOARD[len(missedLetters)])
    print()

    # display the missed letters
    print('Missed Letters:', end = ' ')
    for letter in missedLetters:
        print(letter, end = ' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters: 
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

            # The : character is used to SLICE strings into pieces.
            # [:i] means slice from the start until index i
            # [i+1:] means slice from i+1 until the END
            # [startingPoint:endingPoint]
            
    for letter in blanks:
        print(letter, end = ' ')
    print()

def getGuess(alreadyGuessed):
    # Only allow: single character, A-Z only, not guessed already
    while True: # default 'infinite' loop
        print('Please guess a letter and press enter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.\n')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter an English letter only.')
        elif guess in alreadyGuessed:
            print('Already guessed. Please guess a different letter!')
        else:
            return guess 
        
def playAgain():
    print('Do you want to play again. Yes or No, then press enter.')
    return input().lower().startswith('y') # Return True/False based on input

# START THE ACTUAL GAME
print('Let\'s  Play Hangman!') # \ ESCAPES special characters.
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(wordList)
print("Testing Secret Word: " + secretWord)
gameIsDone = False 

# GAME LOOP BEGINS HERE
while True: # 99% of the time the loop is done this way 
    # TWO WAYS TO EXIT while True: return OR break 
    # DISPLAY BOARD
    displayBoard(missedLetters, correctLetters, secretWord)

    guess = getGuess(missedLetters + correctLetters)
    
    if guess in secretWord: # Is the guess in the secretWord? 
        correctLetters = correctLetters + guess

        # CHECK FOR VICTORY
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters: 
                foundAllLetters = False 
                break 
        if foundAllLetters:
            print('Coongratulation! You have guessed correctly.\n')
            gameIsDone = True
    else: # MISSED LETTER GUESS 
        missedLetters = missedLetters + guess 

        if len(missedLetters) == len(HANGMAN_BOARD) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('You have lost due to using all guesses.\n')
            print('The secret word was ' + secretWord)
            gameIsDone = True

    if gameIsDone:
        if playAgain():
            secretWord = getRandomWord(wordList)
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
        else: 
            break  
