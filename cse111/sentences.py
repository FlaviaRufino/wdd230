import random

def main():
    print(make_sentence(1))
    print(make_sentence(2))
    print(make_sentence(1))
    print(make_sentence(2))
    print(make_sentence(1))
    print(make_sentence(2))

def make_sentence(quantity):
    determiner = get_determiner(quantity)
    adjective = get_adjective()
    noun = get_noun(quantity)
    adverb = get_adverb()
    verb = get_verb(quantity)
    prepositional_phrase1 = get_prepositional_phrase(quantity)
    prepositional_phrase2 = get_prepositional_phrase(quantity)
    sentence = f"{determiner} {adjective} {noun} {adverb} {verb} {prepositional_phrase1} {prepositional_phrase2}."
    return sentence

def get_determiner(quantity):
    if quantity == 1:
        determiners = ["One", "A", "The"]
    else:
        determiners = ["Some", "Many", "The"]
    return random.choice(determiners)

def get_adjective():
    adjectives = ["beautiful", "happy", "brave", "smart", "friendly", "funny"]
    return random.choice(adjectives)

def get_noun(quantity):
    if quantity == 1:
        nouns = ["girl", "bird", "child", "cat", "car", "rabbit", "man"]
    else:
        nouns = ["dogs", "rabbits", "children"]
    return random.choice(nouns)

def get_verb(quantity):
    verbs = ["talked", "drank", "laughed"]
    if quantity == 1:
        return random.choice(verbs)
    else:
        return random.choice(verbs).replace("ed", "")

def get_adverb():
    adverbs = ["quickly", "happily", "silently", "carefully", "loudly", "eagerly"]
    return random.choice(adverbs)

def get_preposition():
    prepositions = ["for", "above", "off", "at", "on", "about"]
    return random.choice(prepositions)

def get_prepositional_phrase(quantity):
    determiner = get_determiner(quantity)
    adjective = get_adjective()
    noun = get_noun(quantity)
    preposition = get_preposition()
    return f"{preposition} {determiner.lower()} {adjective} {noun}"

if __name__ == "__main__":
    main()
