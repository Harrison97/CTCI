def subsequence_indicies(s, t):
  indices = []

  i = j = 0
  while i < len(s) and j < len(t):
    if s[i] == t[j]:
      indices.append(i + 1)
      j += 1
    i += 1
  return indices

y = 'ACGTACGTGACG'
x = 'GTA'
result = subsequence_indicies(y, x)
print(result)
