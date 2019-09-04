import doctest

# Time Complexity: O(n)
# Space complexity: O(1)
def URLify_1(s: str, n: int) -> str:
    """
    >>> URLify_1('Mr John Smith', 13)
    'Mr%20John%20Smith'
    """
    space = '%20'

    for i in range(n):
        if s[i] == ' ':
            s = s[:i] + space + s[i+1:]
            i += 2
    return s

# Time Complexity: O(n)
# Space complexity: O(1)
def URLify_2(s:str) -> str:
    """
    >>> URLify_2('Mr John Smith')
    'Mr%20John%20Smith'
    """
    s = s.split(' ') # O(n)
    s = '%20'.join(s) # O(s) how many spaces - amortized
    return s

doctest.testmod()
