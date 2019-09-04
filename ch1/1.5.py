import doctest

# Time Complexity:  O(n)
# Space Complexity: O(n)
def one_edit_1(s1: str, s2: str) -> bool:
    """
    >>> one_edit_1('pale', 'ple')
    True
    >>> one_edit_1('pales', 'pale')
    True
    >>> one_edit_1('pale', 'bale')
    True
    >>> one_edit_1('pale', 'bake')
    False
    """

    if abs(len(s1) - len(s2)) > 1:
        return False
    set1, set2 = [], []
    for c in s1:
        set1.append(c)
    for c in s2:
        if c in set1:
            set1.remove(c)
        else:
            set2.append(c)
    return True if max(len(set1), len(set2)) <= 1 else False

# More optimal solution - The strings are only one edit away
# So, they are only one character off.
# Time Complexity:  O(n)
# Space Complexity: O(1)
def one_edit_2(s1: str, s2: str) -> bool:
    """
    >>> one_edit_2('pale', 'ple')
    True
    >>> one_edit_2('pales', 'pale')
    True
    >>> one_edit_2('pale', 'bale')
    True
    >>> one_edit_2('pale', 'bake')
    False
    """

    bigger=max([s1, s2], key=len)
    smaller=min([s1, s2], key=len)

    for i, _ in enumerate(smaller):
        if (s1[i] != s2[i]):
            # str copy in here is negligible because it will only happen one time.
            if(len(s1) == len(s2)):
                return True if s1[:i] + s1[i+1:] == s2[:i] + s2[i+1:] else False
            else:
                return True if smaller == bigger[:i] + bigger[i+1:] else False
    return True

doctest.testmod()
