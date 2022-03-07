from sentences import get_determiner, get_noun, get_verb, get_preposition
import random
import pytest


def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ["a", "one", "the"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["two", "some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Get a random number between 2 and 10 inclusive.
        quantity = random.randint(2, 11)

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(quantity)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners

def test_get_noun():
    singular_nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]

    for _ in range(4):
        word = get_noun(1)
        assert word in singular_nouns


    plural_nouns = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]

    for _ in range(4):  
        quantity = random.randint(2,11)
        word = get_noun(quantity)
        assert word in plural_nouns

def test_get_verb():
    past_verbs = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]

    for _ in range(4):
        tense = 'past'
        quantity = random.randint(2,11)
        word = get_verb(quantity, tense)
        assert word in past_verbs

    present_verbs = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]

    for _ in range(4):
        tense = 'present'
        quantity = 1
        word = get_verb(quantity, tense)
        assert word in present_verbs

    future_verbs = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]
    
    for _ in range(4):
        tense = 'future'
        quantity = random.randint(2,11)
        word = get_verb(quantity, tense)
        assert word in future_verbs

def test_get_preposition():
    prepositions = ["about", "above", "across", "after", "along",
    "around", "at", "before", "behind", "below",
    "beyond", "by", "despite", "except", "for",
    "from", "in", "into", "near", "of",
    "off", "on", "onto", "out", "over",
    "past", "to", "under", "with", "without"]

    for _ in range(4):
        
        quantity = random.randint(2,31)
        word = get_preposition(quantity)
        assert word in prepositions


pytest.main(["-v", "--tb=line", "-rN", __file__])