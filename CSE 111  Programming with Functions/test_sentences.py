from sentenses import get_determiner, get_noun, get_verb, get_prepositional_phrase, get_preposition
import pytest

def test_get_determiner():
    # 1. test the single determiners.
     
    single_determiners = ["the", "one"]

    for _ in range(4):
        word = get_determiner(1).lower()

        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["some", "many"]
    # this loop will repeat the statements inside it 4 times

    for _ in range(4):
        word = get_determiner(2).lower()

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners
#--------------------------------------------------------------------------------------------------
# test_get_noun
def test_get_noun():
    single_nouns = ["adult", "bird", "boy", "car", "cat", "child", "dog", "girl", "man", "woman"]
    plural_nouns = ["adults", "birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "women"]

    assert get_noun(1) in single_nouns
    assert get_noun() in plural_nouns
#----------------------------------------------------------------------------------------------------
#test get_verb
def test_get_verb():
    past = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    single_present = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]
    plural_present = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]
    future = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]

    assert get_verb(1, "past") in past
    assert get_verb(0, "past") in past
    assert get_verb(0, "present") in single_present
    assert get_verb(1, "present") in plural_present
    assert get_verb(0, "future") in future
    assert get_verb(1, "future") in future
#--------------------------------------------------------------------------------------------------------------
# test_get_preposition
def test_get_preposition():
    preposition = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    assert get_preposition() in preposition
#----------------------------------------------------------------
# test_get_preposition_phrase
def test_get_preposition_phrase():
    single_determiners = ["the", "one"]
    plural_determiners = ["some", "many"]

    single_nouns = ["adult", "bird", "boy", "car", "cat",  "child", "dog", "girl", "man", "woman"]
    plural_nouns = ["adults", "birds", "boys", "cars", "cats","children", "dogs", "girls", "men", "women"]

    past = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    single_present = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]
    plural_present = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]
    future = ["will"]

    preposition = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    single_past = get_prepositional_phrase(1, get_verb(1, "past")).split(" ")
    assert single_past[0].lower() in single_determiners
    assert single_past[1] in single_nouns
    assert single_past[2] in past
    assert single_past[3] in preposition

    plural_past = get_prepositional_phrase(0, get_verb(0, "past")).split(" ")
    assert plural_past[0].lower() in plural_determiners
    assert plural_past[1] in plural_nouns
    assert plural_past[2] in past
    assert plural_past[3] in preposition

    single_present = get_prepositional_phrase(1, get_verb(1, "present")).split(" ")
    assert single_present[0].lower() in single_determiners
    assert single_present[1] in single_nouns
    assert single_present[2] in single_present
    assert single_present[3] in preposition

    plural_present = get_prepositional_phrase(0, get_verb(0, "present")).split(" ")
    assert plural_present[0].lower() in plural_determiners
    assert plural_present[1] in plural_nouns
    assert plural_present[2] in plural_present
    assert plural_present[3] in preposition

    single_future = get_prepositional_phrase(1, get_verb(1, "future")).split(" ")
    assert single_past[0].lower() in single_determiners
    assert single_past[1] in single_nouns
    assert single_past[2] in future
    assert single_past[4] in preposition

    plural_future = get_prepositional_phrase(0, get_verb(0, "future")).split(" ")
    assert plural_past[0].lower() in plural_determiners
    assert plural_past[1] in plural_nouns
    assert plural_past[2] in future
    assert plural_past[4] in preposition
#--------------------------------------------------------------------------------
pytest.main(["-v", "--tb=line", "-rn", "test_sentenses.py"])
