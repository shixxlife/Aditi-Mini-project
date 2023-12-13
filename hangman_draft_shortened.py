import random  # random module provides functions that generate random numbers and etc
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


def scramble():
    jumbled_words = ['golsalesen', 'esronigap', 'acealbrno', 'bijngee', 'ulbatsni', 'kabnogk', 'erouebnml', 'sdtasemra',
                     'rvocavune', 'kklmtooshc']
    cities = ['losangeles', 'singapore', 'barcelona', 'beijing', 'istanbul', 'bangkok', 'melbourne', 'amsterdam',
              'vancouver', 'stockholm']
    x = random.choice(cities)
    ind = cities.index(x)
    y = jumbled_words[ind]
    return x, y
