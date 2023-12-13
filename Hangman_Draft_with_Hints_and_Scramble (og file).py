import random  # random module provides functions that generate random numbers and etc
import csv
import word_lists


def choosing_word(topic):  # choosing a word from the topics

    if topic == 'Movies':
        word = random.choice(word_lists.movies)
        return word
    elif topic == 'TV-Shows':
        word = random.choice(word_lists.tvshows)
        return word
    elif topic == 'Sports':
        word = random.choice(word_lists.sports)
        return word
    elif topic == 'Fruits':
        word = random.choice(word_lists.fruits)
        return word
    elif topic == 'Animals':
        word = random.choice(word_lists.animals)
        return word
    elif topic == 'Random Words':
        word = random.choice(word_lists.randomwords)
        return word
    elif topic == 'If you want to learn new words':
        word = random.choice(word_lists.new_words)
        return word


def display(w_t_g, g):
    displays = ""
    for i in w_t_g:
        if i == g or i in correct_letters:
            displays += (str(i) + " ")
        else:
            displays += "_ "
    return displays


# The display_word function takes a word and a list of guessed letters as parameters and
# returns a string that represents the current state of the word with underscores for
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


def scramble():
    jumbled_words = ['golsalesen', 'esronigap', 'acealbrno', 'bijngee', 'ulbatsni', 'kabnogk', 'erouebnml', 'sdtasemra',
                     'rvocavune', 'kklmtooshc']
    cities = ['losangeles', 'singapore', 'barcelona', 'beijing', 'istanbul', 'bangkok', 'melbourne', 'amsterdam',
              'vancouver', 'stockholm']
    x = random.choice(cities)
    ind = cities.index(x)
    y = jumbled_words[ind]
    return x, y


def hint(w):
    with open("NewWords(CSV).csv", 'r') as f:
        csvreader = csv.reader(f)
        l = list(csvreader)
        for row in l:
            if w in row[0]:
                print(row[1])


correct_letters = []


def solohangman():
    guessed_letters = []
    word_to_guess = choosing_word()
    attempts = 0
    max_attempts = maximum_attempts(word_to_guess)
    chs = 0

    print("Welcome to hangman!!! Hope you enjoy this exciting game")
    for i in word_to_guess:
        print("_ ", end="")

    while max_attempts - attempts > 0:

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

        c = 0
        for char in current_display:
            if char == "_":
                c += 1

        if c > 2 and (max_attempts - attempts) < 3 and word_to_guess in word_lists.new_words:
            print("do u want a hint?\nif you want type YES or else type NO")
            e = input()
            if e == "YES":
                hint(word_to_guess)
            else:
                pass
        else:
            pass

        if "_" not in current_display:
            print("Congratulations! You have guessed the word:", word_to_guess)
            break

        if attempts == max_attempts and chs < 1:
            print("\nOne more chance to guess the word! Unscramble the city name")
            scrambled_word = scramble()
            print(scrambled_word[1])
            str = input()
            if str == scrambled_word[0]:
                print("Congratulations! You have gained an attempt.")
                attempts -= 1
                chs += 1
            else:
                print("Sorry, You ran out of attempts. The word was:", word_to_guess)
                chs += 2

        if attempts == max_attempts and chs == 1:
            print("Sorry, You ran out of attempts. The word was:", word_to_guess)


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
    print("\nEnter the word")
    word_to_guess = input().lower()
    attempts = 0
    max_attempts = maximum_attempts(word_to_guess)
    points = 0
    chs = 0

    for i in word_to_guess:
        print("_ ", end="")

    while max_attempts - attempts > 0:
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

        if attempts == max_attempts and chs < 1:
            print("\nOne more chance to guess the word! Unscramble the city name")
            scrambled_word = scramble()
            print(scrambled_word[1])
            str = input()
            if str == scrambled_word[0]:
                print("Congratulations! You have gained an attempt.")
                attempts -= 1
                chs += 1
            else:
                print("Sorry, You ran out of attempts. The word was:", word_to_guess)
                chs += 2
                points = 0
                game_count.append(1)

        if attempts == max_attempts and chs == 1:
            print("Sorry, You ran out of attempts. The word was:", word_to_guess)
            points = 0
            game_count.append(1)

    points_table(points)
    print("\nWant to continue the game?\nYes or No")
    cont = input().lower()
    if cont == "yes" or cont == 'y':
        correct_letters.clear()
        multihangman()
    else:
        exit()


point = [0, 0]


def points_table(p):
    global x, y
    print("\nPoints:")
    if len(game_count) % 2 == 0:
        point[0] += p
        print(x + ": " + str(point[0]))
        print(y + ": " + str(point[1]))
    else:
        point[1] += p
        print(x + ": " + str(point[0]))
        print(y + ": " + str(point[1]))
