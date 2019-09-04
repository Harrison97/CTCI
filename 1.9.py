import doctest

def is_substring(s1: str, s2:str) -> bool:
    """Returns True if s1 is a substring of s2
    >>> is_substring('as', 'asdf')
    True
    >>> is_substring('o', 'asdf')
    False
    """
    return bool(s2.find(s1)+1)

# Time Complexity: O(n)
# Space Complexity: O(1)
def is_rotation_1(s1: str, s2: str) -> bool:
    """
    >>> is_rotation_1('waterbottle', 'erbottlewat')
    True
    >>> is_rotation_1('waterbottleq', 'erbottlewat')
    False
    >>> is_rotation_1('qwerty', 'wertyq')
    True
    >>> is_rotation_1('qwerty', 'qwerty')
    True
    >>> is_rotation_1('qw', 'wq')
    True
    >>> is_rotation_1('q', 'q')
    True
    """

    if len(s1) != len(s2):
        return False
    if len(s1) == 1:
        return True

    rot_index = None
    s1_index = 0
    for i, c in enumerate(s2):
        if c == s1[s1_index]:
            s1_index += 1

            if not rot_index:
                rot_index = i

        else:
            s1_index = 0
            rot_index = None

    return True if rot_index and is_substring(s2[:rot_index], s1) else False

# Takes slightly more space (still O(1)), way less comparisions
# Time Complexity: O(n)
# Space Complexity: O(1)
def is_rotation_2(s1: str, s2: str) -> bool:
    """
    >>> is_rotation_2('waterbottle', 'erbottlewat')
    True
    >>> is_rotation_2('waterbottleq', 'erbottlewat')
    False
    >>> is_rotation_2('qwerty', 'wertyq')
    True
    >>> is_rotation_2('qwerty', 'qwerty')
    True
    >>> is_rotation_2('qw', 'wq')
    True
    >>> is_rotation_2('q', 'q')
    True
    """

    s1s1 = s1+s1
    return is_substring(s2, s1s1)
doctest.testmod()
