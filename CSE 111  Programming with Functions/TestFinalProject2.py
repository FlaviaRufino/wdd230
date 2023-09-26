import pytest
import collections 
from my_program2 import main, print_counted_words, print_certain_words, list_keys

# tests the main function
def test_main():
    sample_list = ['Blueberry', 'mango', 'orange', 'guava', 'mango', 
    'grapes', 'watermelon', 'orange', 'guava', 'bluebarry', 'mango', 
    'Kiwi', 'orange', 'blueberry', 'watermelon']
    # assert that passing the argument "sample.txt" into main() outputs sample_list 
    assert main("sample.txt") == sample_list

# tests the print_counted_words function
def test_print_counted_words():
    sample_list = ['Blueberry', 'mango', 'orange', 'guava', 'mango', 
    'grapes', 'watermelon', 'orange', 'guava', 'bluebarry', 'mango', 
    'Kiwi', 'orange', 'blueberry', 'watermelon']
    occurrence_count = collections.Counter(sample_list)
    assert print_counted_words(occurrence_count) == occurrence_count

# tests the print_certain_words function
def test_print_certain_words():
    sample_list = ['Blueberry', 'mango', 'orange', 'guava', 'mango', 
    'grapes', 'watermelon', 'orange', 'guava', 'bluebarry', 'mango', 
    'Kiwi', 'orange', 'blueberry', 'watermelon']
    occurrence_count = collections.Counter(sample_list)
    assert print_certain_words("blueberry", occurrence_count) == 3
    assert print_certain_words("mango", occurrence_count) == 3
    assert print_certain_words("orange", occurrence_count) == 3
    assert print_certain_words("guava", occurrence_count) == 2
    assert print_certain_words("grapes", occurrence_count) == 2
    assert print_certain_words("watermelon", occurrence_count) == 1
    assert print_certain_words("kiwi", occurrence_count) == 1

# tests the list_keys function
def test_list_keys():
    sample_list2 = ["Blueberry", "mango", "orange", "guava", "grapes", "watermelon", "Kiwi"]
    occurrence_count = collections.Counter(sample_list2)
    assert list_keys(occurrence_count) == sample_list2


pytest.main(["-v", "--tb=line", "-rN", "test_my_program2.py"])