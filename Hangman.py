import random

list = ["engineering", "google", "programmer", "nasa"]
word = random.choice(list)

hangman_lifes = ['''
  +---+
  |   |
      |
      | (6 lives more)
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      | (5 lives more)
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   | (4 lives more)
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   | (3 lives more)
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  | (2 lives more)
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  | (only 1 live more)
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  | (Hanged)
 / \  |
      |
=========''']

print("Welcome to Hangman Game")
print()

lives = 6  #declaring total lives of hangman
incorrect_letters = [] # creating empty list for incorrect letters enterd

# creating blank interface 
blank_list = []
for j in range(0,len(word)):
  blank_list += "_"
print(blank_list)
print(hangman_lifes[0])
print()

end_of_game = False #declaring codition for while loop
while not end_of_game:
  print(f"Incorrect letters enterd {incorrect_letters}")
  guess = input("Guess a letter?\n")
  guess = guess.lower()
  print()

  #when user give correct guess
  for i in range(0,len(word)):
    if word[i] == guess:
      for i in range(0,len(blank_list)):
        if guess == word[i]:
          blank_list[i] = guess
  #when user give incorrect guess          
  if guess not in word:
    lives = lives - 1
    incorrect_letters += guess
    print(hangman_lifes[6-lives])
    if lives == 0:
      print("you LOSS")
      print(f"The word is {word}")
      end_of_game = True
        
  print(' '.join(blank_list))
  print()

  #giving condition for while loop to stop 
  if "_" not in blank_list:
    end_of_game = True
    print("You WON")
