import string
from collections import Counter

def is_palindrome(text):
    """
    >>> is_palindrome('Mr. Owl ate my metal worm')
    True
    >>> is_palindrome('Eva, can I see bees in a cave?')
    True
    """
    #second method
    """
    filtered_text = list(filter(str.isalpha, text.lower()))
    return True if filtered_text == filtered_text[::-1] else False
    """
    #first method
    filtered_text = [letter.lower() for letter in text if letter.isalpha()]
    return True if filtered_text == filtered_text[::-1] else False


def is_isogram(text):
    """
    >>> is_isogram('uncopyrightables')
    True
    """

    #method 1
    filtered_text = list(filter(str.isalpha, text.lower()))
    for letter in filtered_text:
        if filtered_text.count(letter) > 1:
            return False
    return True

    #method 2
    """
    duplicate = []
    filtered_text = [letter.lower() for letter in text if letter.isalpha()]
    for letter in filtered_text:
        if letter in duplicate:
            return False
        duplicate.append(letter)
    return True
    """


def is_pangram(text):
    """
    >>> is_pangram('The quick brown fox jumps over the lazy dog')
    True
    """
    #method 1
    filtered_text = [letter.lower() for letter in text if letter.isalpha()]
    for letter in list(map(chr, range(97, 123))):
        if letter not in filtered_text:
            return False
    return True

    #method 2
    """
    filtered_text = [letter.lower() for letter in text if letter.isalpha()]
    alphabet = string.ascii_lowercase
    for letter in alphabet:
        if letter not in filtered_text:
            return False
    return True
    """


def is_anagram(text1, text2):
    """
    >>> is_anagram('Justin Timberlake', "I'm a jerk but listen")
    True
    """
    #method 1
    filtered_text1 = list(filter(str.isalpha, text1.lower()))
    filtered_text2 = [letter.lower() for letter in text2 if letter.isalpha()]
    filtered_text1.sort()
    filtered_text2.sort()
    return True if filtered_text1 == filtered_text2 else False

    #method 2
    """
    filtered_text1 = list(filter(str.isalpha, text1.lower()))
    filtered_text2 = [letter.lower() for letter in text2 if letter.isalpha()]
    return True if Counter(filtered_text1) == Counter(filtered_text2) else False
    """

def is_blanagram(text1, text2):
    """
    >>> is_blanagram('Justin Timberlake', "I'm a berk but listen")
    True
    """
    pass
