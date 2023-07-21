'''
    Course: Computer Programming
    Year: 2019
    
    Student Name: Diego Esteban Quintero Rey
    Username: diquintero

    Program: process_tweets.py
    Project: Tweets Word Cloud 
'''

from string import ascii_letters

def clean_line(line):
    '''
    Removes all non-alphabetic characters, except '', '@', and '#', from the line.

    call: clean_line("This is a #hashtag!, this a is a Number123  @userName")
    output: 'this is a #hashtag this a is a number  @username'
    '''
    special_characters = {" ", "@", "#"}  # Set of special characters that won't be removed
    clean_tweet = ""  # Initialize an empty string to store the cleaned tweet

    for char in line:
        # Check if the character is alphabetic or one of the special characters
        if (char in ascii_letters) or (char in special_characters):
            clean_tweet += char  # Add the character to the clean_tweet string

    clean_tweet_lowercase = clean_tweet.lower()  # Convert the cleaned tweet to lowercase
    return clean_tweet_lowercase  # Return the cleaned and lowercase tweet

def get_tweet_text(line):
    '''
    Receives a line from the tweets file and extracts the tweet text, which is returned as a string.
    The input line has the following structure:
    source, text, created_at, retweet_count, favorite_count, is_retweet, id_str

    call: get_tweet_text("Twitter,Thank you!,11-15-2017 10:58:18,96,433,false,9307")
    output: 'Thank you!'
    
    The function iterates through each character in the line and collects characters
    between the first and the second comma to extract the tweet text.
    '''

    comma_count = None  # The tweet text is between the first and second comma
    tweet_text = ""

    for char in line:
        if char == "," and comma_count is None:
            comma_count = True
            continue
        if char == "," and comma_count:
            comma_count = False
            break
        if comma_count:
            tweet_text += char

    return tweet_text

def read_stopwords():

    # This function reads the stop words from the 'stopwords.txt' file and stores them in a set.

    stop_words_set = set()  # Initialize an empty set to store the stop words.

    with open("stopwords.txt", "r") as stop_words_file:
        stop_words = stop_words_file.read().split()  # Read the words from the file and split them into a list.

        for word in stop_words:
            stop_words_set.add(word)  # Add each word to the set to eliminate duplicates.

    return stop_words_set  # Return the set of stop words.

def process_tweet_text(text):
    '''
    Receives the text of a tweet and processes it:
    - Removes any non-alphabetic character, except ' ', '@', and '#'.
    - Converts it to lowercase.
    - Splits it into words.
    - Filters out all the words that are stop words.
    - Returns the remaining words as a list.
    
    call: process_tweet_text("this is a #hashtag this a is a number  @username")
    output: ['#hashtag', 'number', '@username']
    '''
    stopwords = read_stopwords()  # Get the set of stop words from the 'stopwords.txt' file.
    words = clean_line(text).split()  # Clean the tweet text and split it into words.
    result = []  # Initialize an empty list to store the filtered words.

    for word in words:
        if word not in stopwords:
            result.append(word)  # Add the word to the result list if it's not a stop word.

    return result  # Return the list of remaining words after filtering out stop words.

def process_tweet_file(file_name):
    '''
    Receives the name of the file containing the tweets. Processes it to obtain
    all the tweet texts. Extracts the words from it and counts their frequencies.
    Returns the result as a dictionary, where the keys are words, and the values are word frequencies.
    '''
    word_freqs = {}  # Initialize an empty dictionary to store word frequencies.

    with open(file_name, "r", encoding="utf-8") as tweets:
        for line in tweets:
            text = get_tweet_text(line)  # Extract the tweet text from the line.
            words = process_tweet_text(text)  # Process the tweet text to get a list of words.

            for word in words:
                word_freqs[word] = word_freqs.get(word, 0) + 1  # Update word frequencies in the dictionary.

    return word_freqs  # Return the dictionary containing word frequencies.

def print_statistics(word_freqs):
    '''
    Receives a dictionary with word frequencies and prints the statistics.
    '''
    total_number_of_words = 0  # Initialize a variable to store the total number of words.

    for word, frequency in word_freqs.items():
        total_number_of_words += frequency  # Count the total number of words.

    total_number_of_different_words = len(set(word_freqs.keys()))  # Count the total number of different words.

    most_frequent_words_list = [(frequency, word) for word, frequency in word_freqs.items()]
    '''
    Creates a list where each element is a sublist containing each word and its corresponding
    frequency from the word frequency dictionary. This is done to invert the order, starting with
    the frequencies, so that it can be sorted by frequency in descending order.
    '''
    most_frequent_words_list.sort(reverse=True)  # Sort the list in descending order of frequency.

    most_frequent_word = most_frequent_words_list[0][1]  # Get the most frequent word from the sorted list.
    most_frequent_word_freq = most_frequent_words_list[0][0]  # Get the frequency of the most frequent word.

    print('The total number of words is:', total_number_of_words)
    print('The total number of different words is:', total_number_of_different_words)
    print('The most frequent word is:', most_frequent_word)
    print('With a frequency of:', most_frequent_word_freq)

def write_words(word_freqs, file_name):
    '''
    Escriba las palabras junto con sus frecuencias, una palabra por línea
    con la palabra y la frecuencia separadas por un espacio:
            great 484
            fabulous 200
    '''
    # your code here
    with open("words.txt", "w") as words_file:
        for palabra, frecuencia in word_freqs.items():
            words_file.write("{} {}\n".format(palabra, frecuencia))
    words_file.close()
    return

def write_words(word_freqs, file_name):
    '''
    Write the words along with their frequencies, one word per line,
    with the word and frequency separated by a space:
            great 484
            fabulous 200
    '''
    with open(file_name, "w") as words_file:
        for word, frequency in word_freqs.items():
            words_file.write("{} {}\n".format(word, frequency))
    
    # No need to close the file explicitly when using 'with open' context manager.
    # The file will be closed automatically when exiting the 'with' block.

word_freqs = process_tweet_file('tweets.txt')
print_statistics(word_freqs)
write_words(word_freqs, 'words.txt')

