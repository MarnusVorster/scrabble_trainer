"""Module to scrabble the words using the word list file."""
import random


def fetch_similar_words(word: str) -> [str]:
    """
    Loop through the word list and fetch words with the same starting character and length.
    If nothing is found return the original passed in word.
    :param word: The word to use for the lookup.
    :return: List of found words.
    """
    start_char = word[0]
    word_len = len(word)
    found_word_list = []

    with open("corncob_lowercase.txt") as fp:
        for line in fp:
            # Remove unnecessary characters
            new_line = line.strip()
            if new_line.startswith(start_char) and len(new_line) == word_len:
                found_word_list.append(new_line)
    return found_word_list or [word]


def scrabble_sentence(sentence: str) -> str:
    """
    Main method to scrabble a sentence.

    STEPS:
    1. Read in a sentence.
    2. Break the sentence into words.
    3. Run a lookup with each word and get the matching scrabble words.
    4. Randomly selects from the scrabble word list.
    5. Append it to the resultant_sentence.
    :param sentence: The sentence to do a scrabble lookup on.
    :return: The scrabbled sentence.
    """
    if not sentence.strip():
        raise ValueError('word or sentence is empty of not valid!')
    # Break sentence into a word list
    word_list = sentence.split(' ')
    resultant_sentence = []
    for word in word_list:
        try:
            # Send word to fetch_similar_words and get the lookup word list.
            found_word_list = fetch_similar_words(word)
            # Randomly select a word from the list
            resultant_sentence.append(random.choice(found_word_list))
        except KeyError:  # It's cheaper to except than using a if to validate.
            resultant_sentence.append(word)
    return " ".join(resultant_sentence)
