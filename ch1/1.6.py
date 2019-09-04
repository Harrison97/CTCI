import doctest

def compress_string(s: str) -> bool:
    """
    >>> compress_string('aabcccccaaa')
    'a2b1c5a3'
    >>> compress_string('aabcccccaaaq')
    'a2b1c5a3q1'
    >>> compress_string('a')
    'a'
    """

    if len(s) <= 2:
        return s

    curr = s[0]
    count = 0
    compressed = ''

    for c in s + ' ':
        if c == curr:
            count += 1
        else:
            compressed += curr + str(count)
            curr = c
            count = 1
        if len(compressed) > len(s):
            return s

    return compressed

doctest.testmod()
