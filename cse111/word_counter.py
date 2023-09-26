import os
import re
from collections import Counter

def count_words(text):
    words = text.split()
    return len(words)

def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            text = file.read()
        return text
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        return ""

def remove_punctuation(text):
    cleaned_text = re.sub(r'[^\w\s]', '', text)
    return cleaned_text

def calculate_word_frequency(text):
    words = text.lower().split()
    word_counts = Counter(words)
    return word_counts

def display_word_frequency(word_counts):
    for word, count in word_counts.items():
        print(f"{word}: {count}")

def main():
    file_name = input("Enter the name of the text file: ")
    text = read_file(file_name)
    if text:
        cleaned_text = remove_punctuation(text)
        word_counts = calculate_word_frequency(cleaned_text)
        display_word_frequency(word_counts)
        print(f"Total words: {count_words(text)}")

if __name__ == "__main__":
    main()
