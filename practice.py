"""Dictionaries Practice

**IMPORTANT:** These problems are meant to be solved using
dictionaries and sets.
"""


def without_duplicates(words):
    """Given a list of words, return list with duplicates removed.

    For example:

        >>> no_dupes = without_duplicates(
        ...     ["rose", "is", "a", "rose", "is", "a", "rose"])

        >>> isinstance(no_dupes, list)
        True

        >>> sorted(without_duplicates(
        ...     ["rose", "is", "a", "rose", "is", "a", "rose"]))
        ['a', 'is', 'rose']

    You should treat differently-capitalized words as different:

        >>> sorted(without_duplicates(
        ...     ["Rose", "is", "a", "rose", "is", "a", "rose"]))
        ['Rose', 'a', 'is', 'rose']

        An empty list should return an empty list:

        >>> sorted(without_duplicates(
        ...     []))
        []

    The function should work for a list containing integers:

        >>> sorted(without_duplicates([111111, 2, 33333, 2]))
        [2, 33333, 111111]

    The function should return a variable of type list:
        >>> type(without_duplicates([111111, 2, 33333, 2]))
        <class 'list'>
    """

    unique_words = set()

    for word in words:
        unique_words.add(word)

    return list(unique_words)


def find_unique_common_items(items1, items2):
    """Produce the set of *unique* common items in two lists.

    Given two lists, return a set of the *unique* common items
    shared between the lists.

    **IMPORTANT**: you may not use `'if ___ in ___``
    or the method `list.index()`.

    This should return a set:

        >>> unique_common_items = find_unique_common_items([1, 2, 3, 4], [2, 1])
        >>> isinstance(unique_common_items, set)
        True

    This should find [1, 2]:

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [2, 1]))
        [1, 2]

    However, now we only want unique items, so for these lists,
    don't show more than 1 or 2 once:

        >>> sorted(find_unique_common_items([3, 2, 1], [1, 1, 2, 2]))
        [1, 2]

    The elements should not be treated as duplicates if they are
    different data types:

        >>> sorted(find_unique_common_items(["2", "1", 2], [2, 1]))
        [2]
    """
    item_list = []

    for item in items1:
        for compared_item in items2:
            if item == compared_item:
                item_list.append(item)

    return set(item_list)


def get_sum_zero_pairs(numbers):
    """Given list of numbers, return list of pairs summing to 0.

    Given a list of numbers, add up each individual pair of numbers.
    Return a list of each pair of numbers that adds up to 0.

    For example:

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1]) )
        [[-2, 2], [-1, 1]]

        >>> sort_pairs( get_sum_zero_pairs([3, -3, 2, 1, -2, -1]) )
        [[-3, 3], [-2, 2], [-1, 1]]

    This should always be a unique list, even if there are
    duplicates in the input list:

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1]) )
        [[-2, 2], [-1, 1]]

    Of course, if there are one or more zeros to pair together,
    that's fine, too (even a single zero can pair with itself):

        >>> sort_pairs( get_sum_zero_pairs([1, 3, -1, 1, 1, 0]) )
        [[-1, 1], [0, 0]]
    """

    sum_zero_pairs = []
    unique_zero_pairs = set()

    for number in numbers:
        i = 0
        while i < len(numbers):
            if (number + numbers[i]) == 0:
                zero_pair = ([number, numbers[i]])
                sum_zero_pairs.append(zero_pair)
                break
            i += 1

    for zero_pair in sum_zero_pairs:
        zero_pair = tuple(sorted(zero_pair))
        if zero_pair not in unique_zero_pairs:
            unique_zero_pairs.add(zero_pair)

    return unique_zero_pairs


def top_chars(phrase):
    """Find most common character(s) in string.

    Given an input string, return a list of character(s) which
    appear(s) the most in the input string.

    If there is a tie, the order of the characters in the returned
    list should be alphabetical.

    For example:

        >>> top_chars("The rain in spain stays mainly in the plain.")
        ['i', 'n']

    If there is not a tie, simply return a list with one item.

    For example:

        >>> top_chars("Shake it off, shake it off.")
        ['f']

    Do not count spaces, but count all other characters.

    """
    character_count = {}

    # create a dictionary where character is the key and how many times it appears is the value
    for character in phrase:
        if character != " ":
            character_count[character] = character_count.get(character, 0) + 1
    
    #search for the highest number of repeats
    highest_count = 0

    for value in character_count.values():
        if value > highest_count:
            highest_count = value

    #search for the character(s) that showed up the most times
    characters = []

    for key in character_count.keys():
        if character_count[key] == highest_count:
            characters.append(key)
    
    return characters

#####################################################################
# You can ignore everything below this.


def sort_pairs(l):
    """ Print sorted list of pairs where the pairs are sorted."""
    # NOTE: This is used only for documentation tests. You can ignore it.

    return sorted(sorted(pair) for pair in l)


if __name__ == "__main__":
    print()
    import doctest
    if doctest.testmod().failed == 0:
        print("*** ALL TESTS PASSED ***")
    print()
