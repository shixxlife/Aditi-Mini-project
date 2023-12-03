import random  # random module provides functions that generate random numbers and etc


def choosing_word():  # choosing a word from the topics

    # TODO: Use a separate file to store words

    movies = ["fastandfurious", "harrypotter", "marvelavengers", "conjuring", "thenun", "incredibles", "inception",
              "barbie", "deadpool", "spiderman", "ironman", "thor", "thedarkknight", "avatar", "jurassicpark",
              "johnwick", "terminator", "oppenheimer", "barbie", "joker"]
    tvshows = ["friends", "modernfamily", "theoffice", "loki", "mahabharat", "gameofthrones", "kotafactory",
               "aspirants", "suits", "wednesday", "simpsons", "mandalorian", "bigbangtheory", "moneyheist", "mirzapur",
               "moonknight", "queensgambit", "daredevil", "sherlock", "strangerthings"]
    randomwords = ["computer", "algorithm", "keyboard", "language", "library", "internet", "science", "research",
                   "technology", "innovation", "universe", "galaxy", "astronomy", "philosophy", "education",
                   "knowledge", "discovery", "creativity", "exploration", "invention"]
    sports = ["soccer", "basketball", "tennis", "swimming", "golf", "volleyball", "cricket", "baseball", "hockey",
              "table tennis", "badminton", "rugby", "athletics", "cycling", "boxing", "skiing", "surfing", "karate",
              "wrestling", "sailing"]
    animals = ["dog", "cat", "elephant", "lion", "tiger", "giraffe", "zebra", "bear", "snake", "monkey", "dolphin",
               "kangaroo", "koala", "penguin", "panda", "owl", "rhinoceros", "hippopotamus", "cheetah", "crocodile"]
    fruits = ["apple", "orange", "banana", "grape", "kiwi", "watermelon", "strawberry", "blueberry", "pineapple",
              "mango", "pear", "peach", "plum", "cherry", "raspberry", "blackberry", "avocado", "pomegranate", "lemon",
              "lime"]

    print(
        '''Which topic do you choose to play Hangman??\n\nOptions are-->\nA)Movies\nB)TV-Shows\nC)Sports\nD)Fruits\nE)Animals\nF)Random Words\n\nChoose the letters accordingly''')

    topic = input()

    if topic == 'A':
        word = random.choice(movies)
        return word
    elif topic == 'B':
        word = random.choice(tvshows)
        return word
    elif topic == 'C':
        word = random.choice(sports)
        return word
    elif topic == 'D':
        word = random.choice(fruits)
        return word
    elif topic == 'E':
        word = random.choice(animals)
        return word
    elif topic == 'F':
        word = random.choice(randomwords)
        return word


def display(w_t_g, g):
    displays = ""
    for i in w_t_g:
        if i == g or i in correct_letters:
            displays += (str(i) + " ")
        else:
            displays += "_ "
    return (displays)


# The display_word function takes a word and a list of guessed letters as parameters and returns a string that represents the current state of the word with underscores for
# unguessed letters and actual letters for guessed ones.
def maximum_attempts(w):
    z = len(w)
    ma = 0
    if z <= 5:
        ma = 5
    elif z > 5 and z <= 10:
        ma = 7
    else:
        ma = 9
    return ma


correct_letters = []


def solohangman():
    guessed_letters = []
    word_to_guess = choosing_word()
    attempts = 0
    max_attempts = maximum_attempts(word_to_guess)

    print("Welcome to hangman!!! Hope u enjoy this exciting game")
    for i in word_to_guess:
        print("_ ", end="")
    while True:
        print("\nAttempts left:", max_attempts - attempts)
        guess = input("Enter a letter: ").lower()

        current_display = display(word_to_guess, guess)
        print(current_display)

        if guess in guessed_letters:
            print("You have already guessed that letter. Try again")
            continue
        guessed_letters.append(guess)

        if guess not in word_to_guess:
            attempts += 1
            print("Incorrect guess!")
        else:
            print("Correct Guess!")
            correct_letters.append(guess)

        if "_" not in current_display:
            print("Congratulations! You have guesses the word:", word_to_guess)
            break

        if attempts == max_attempts:
            print("Sorry, You ran out of attempts. The word was:", word_to_guess)
            break


x = ""
y = ""


def details():
    global x, y
    print("Enter the Player-1 name")
    x = input()
    print("Enter the Player-2 name")
    y = input()
    return (x, y)


game_count = []


def multihangman():
    guessed_letters = []
    print("Enter the word")
    word_to_guess = input().lower()
    attempts = 0
    max_attempts = maximum_attempts(word_to_guess)
    points = 0
    for i in word_to_guess:
        print("_ ", end="")

    while True:
        print("\nAttempts left:", max_attempts - attempts)
        guess = input("Enter a letter: ").lower()

        current_display = display(word_to_guess, guess)
        print(current_display)

        if guess in guessed_letters:
            print("You have already guessed that letter. Try again")
            continue
        guessed_letters.append(guess)

        if guess not in word_to_guess:
            attempts += 1
            print("Incorrect guess!")
        else:
            print("Correct Guess!")
            correct_letters.append(guess)

        if "_" not in current_display:
            print("Congratulations! You have guesses the word:", word_to_guess)
            points = 5
            game_count.append(1)
            break

        if attempts == max_attempts:
            print("Sorry, You ran out of attempts. The word was:", word_to_guess)
            points = 0
            game_count.append(1)
            break

    points_table(points)
    print("Want to continue the game?\nYes or No")
    cont = input().lower()
    if cont == "yes" or cont == 'y':
        correct_letters.clear()
        multihangman()
    else:
        exit()


point = [0, 0]


def points_table(p):
    global x, y
    print("Points:")
    if len(game_count) % 2 == 0:
        point[0] += p
        print(x + ": " + str(point[0]))
        print(y + ": " + str(point[1]))
    else:
        point[1] += p
        print(x + ": " + str(point[0]))
        print(y + ": " + str(point[1]))


print("Welcome to Hangman! Hope you enjoy this exciting game")
print("Enter the mode: Solo or Multiplayer")
mode = input().lower()
if mode == "solo":
    solohangman()
else:
    details()
    multihangman()
