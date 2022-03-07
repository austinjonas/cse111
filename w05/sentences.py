import random

from pyparsing import WordStart

def main():
    make_sentences('past')
    make_sentences('present')
    make_sentences('future')

def make_sentences(tense):
    for i in range(1,3):
        word = get_determiner(i)
        noun = get_noun(i)
        verb = get_verb(i, tense)
        preposition = get_preposition()

        print(f'{word.capitalize()} {noun} {verb} {preposition} {word}. ')

def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "two", "some", "many".
    If quantity == 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "two", "some", "many", or "the".

    Parameter
        quantity: an integer.
            If quantity == 1, this function will return
            a determiner for a single noun. Otherwise this
            function will return a determiner for a plural noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["two", "some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_noun(quantity):
    if quantity == 1:
        words = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    
    else:
        words = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]
    
    word = random.choice(words)
    return word
    
def get_verb(quantity, tense):
    
    if tense == "past":
        verbs = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    
    if tense == "present" and quantity == 1:   
        verbs = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    
    if tense is "present" and quantity != 1:
        # this function will return one of these ten verbs:
        verbs = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    
    if tense == "future":
        verbs = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]

    verb = random.choice(verbs)
    #     quantity: an integer that determines if the
    #         returned verb is single or plural.
    #     tense: a string that determines the verb conjugation,
    #         either "past", "present" or "future".
    return verb
    # """

def get_preposition():
    """Return a randomly chosen preposition
    from this list of prepositions:"""
    words = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    
    preposition = random.choice(words)
    return preposition

def get_prepositional_phrase(quantity):

    preposition = get_preposition()
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    prepositional_phrase = preposition + ' ' + noun
    return prepositional_phrase

def generate_sentence(quantity, tense):
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity)
    prepositional_prase = get_prepositional_phrase(quantity)

    print(f'{determiner.capitalize()} {noun} {verb} {prepositional_prase}.')

main()
