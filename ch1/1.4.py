import doctest

# Time Complexity:  O(n) where n is the length of the string
# Space Complexity: O(1) because no more than the alphabet is stored in the map
def is_palindrome_permutation_1(s:str) -> bool:
    """
    >>> is_palindrome_permutation_1('a')
    True
    >>> is_palindrome_permutation_1('aya')
    True
    >>> is_palindrome_permutation_1('yyyayayyy')
    True
    >>> is_palindrome_permutation_1('asdffdsa')
    True
    >>> is_palindrome_permutation_1('asdfgfdsa')
    True
    >>> is_palindrome_permutation_1('asdfdsaer')
    False
    >>> is_palindrome_permutation_1('aassddffokijokijplplkmkmjsnxjsnxb')
    True
    """

    if len(s) == 1:
        return True
    my_map = {}
    for c in s:
        my_map.setdefault(c, 0)
        my_map[c] += 1

    oddCount = 0
    for key, value in my_map.items():
        if value % 2 == 1:
            oddCount += 1
        if oddCount > 1:
            return False
    return True

# Improved some minor things, same complexity
# Time Complexity:  O(n) where n is the length of the string
# Space Complexity: O(1) because no more than the alphabet is stored in the map
def is_palindrome_permutation_2(s:str) -> bool:
    """
    >>> is_palindrome_permutation_2('a')
    True
    >>> is_palindrome_permutation_2('aya')
    True
    >>> is_palindrome_permutation_2('yyyayayyy')
    True
    >>> is_palindrome_permutation_2('asdffdsa')
    True
    >>> is_palindrome_permutation_2('asdfgfdsa')
    True
    >>> is_palindrome_permutation_2('asdfdsaer')
    False
    >>> is_palindrome_permutation_2('aassddffokijokijplplkmkmjsnxjsnxb')
    True
    """

    if len(s) == 1:
        return True
    my_map = {}
    oddCount = 0
    for c in s:
        my_map.setdefault(c, 0)
        my_map[c] += 1
        if my_map[c] % 2 == 1:
            oddCount += 1
        else:
            oddCount -= 1
    return False if oddCount > 1 else True

doctest.testmod()

