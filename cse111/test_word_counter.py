import pytest
from word_counter import count_words, read_file, remove_punctuation, calculate_word_frequency

def test_count_words():
    text = "This is a sample text file. This text file contains sample text."
    assert count_words(text) == 12

def test_read_file_existing():
    file_name = "sample_text.txt"
    expected_text = """This is a sample text file. This text file contains sample text."""
    assert read_file(file_name) == expected_text

def test_read_file_nonexistent():
    file_name = "nonexistent_file.txt"
    assert read_file(file_name) == ""

def test_remove_punctuation():
    text = "Hello, world! This is a sample text."
    expected_cleaned_text = "Hello world This is a sample text"
    assert remove_punctuation(text) == expected_cleaned_text

def test_calculate_word_frequency():
    text = "This is a sample text file. This text file contains sample text."
    expected_word_counts = {'this': 2, 'is': 1, 'a': 1, 'sample': 2, 'text': 3, 'file': 2, 'contains': 1}
    assert calculate_word_frequency(text) == expected_word_counts

if __name__ == "__main__":
    pytest.main()
