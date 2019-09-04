import doctest

# First implementation.
# Time Complexity:  O(N)
# Space Complexity: O(N)
def is_permutation_1(s1: str, s2: str) -> bool:

    """ Checks to see if s1 and s2 are permutations of each other.
    >>> is_permutation_1('asdf', 'dfsa')
    True
    >>> is_permutation_1('asdfe', 'vdfsa')
    False
    >>> is_permutation_1('asdfghjklasdfgqwert', 'asdgfqwtrelkjhagsfd')
    True
    """

    if len(s1) is not len(s2):
        return False
    my_map = {}
    for i, _ in enumerate(s1):
        if s1[i] not in my_map:
            my_map[s1[i]] = 0
        if s2[i] not in my_map:
            my_map[s2[i]] = 0
        my_map[s1[i]] += 1
        my_map[s2[i]] -= 1

    return my_map[max(my_map)] is 0 and my_map[min(my_map)] is 0


# Second implementation
# Time Complexity:  O(n log n)
# Space complexity: O(1)
def is_permutation_2(s1: str, s2: str) -> bool:

    """ Checks to see if s1 and s2 are permutations of each other.
    >>> is_permutation_2('asdf', 'dfsa')
    True
    >>> is_permutation_2('asdfe', 'vdfsa')
    False
    >>> is_permutation_2('asdfghjklasdfgqwert', 'asdgfqwtrelkjhagsfd')
    True
    """

    s1 = sorted(s1)
    s2 = sorted(s2)
    if s1 == s2:
        return True
    return False

doctest.testmod()
