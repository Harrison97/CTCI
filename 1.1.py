import unittest

chars = 128

def has_unique_chars(s: str) -> bool:
    memo = chars*[0]
    for c in s:
        memo[ord(c) % chars] += 1
        if memo[ord(c) % chars] > 1:
            return False
    return True

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(has_unique_chars('aAsSdDcCvVbBNnMmKkL'), True)
    def test_2(self):
        self.assertEqual(has_unique_chars('adasf'), False)
    def test_3(self):
        self.assertEqual(has_unique_chars('1!2#4$dDfFcCvG()'), True)
    def test_4(self):
        self.assertEqual(has_unique_chars('1!2#4$dDfFcCvG())'), False)

if __name__ == '__main__':
    unittest.main()

