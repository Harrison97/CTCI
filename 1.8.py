import doctest

# Time complexity: O(MxN) - - Has to hit every element
# Space Complexity: O(N) - Works on preexisting matrix, may have to store N zero_cols
# This actually does not work because if 2 zeros are on the same row,
# the 2nd would never be found
def zero_out_1(mat: [[]]) -> [[]]:
    """ Missing failing test case...
    >>> zero_out_1([[1]])
    [[1]]
    >>> zero_out_1([[1, 0], [3, 4]])
    [[0, 0], [3, 0]]
    >>> zero_out_1([[0, 2, 3], [4, 5, 6], [7, 8, 0]])
    [[0, 0, 0], [0, 5, 0], [0, 0, 0]]
    >>> zero_out_1([[1, 2, 3, 4, 5], [6, 0, 8, 9, 10], [11, 5, 13, 14, 15], [16, 1, 18, 19, 20], [21, 0, 23, 24, 25]])
    [[1, 0, 3, 4, 5], [0, 0, 0, 0, 0], [11, 0, 13, 14, 15], [16, 0, 18, 19, 20], [0, 0, 0, 0, 0]]
    >>> zero_out_1([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 0, 16]])
    [[1, 2, 0, 4], [5, 6, 0, 8], [9, 10, 0, 12], [0, 0, 0, 0]]
    """

    zero_cols = set()
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if j in zero_cols and mat[i][j] != 0:
                mat[i][j] = 0
            elif mat[i][j] == 0:
                for k in range(i):
                    mat[k][j] = 0
                mat[i] = [0 for x in range(len(mat[0]))]
                zero_cols.add(j)
                break
    return mat


# Time complexity: O(MxN) - - Has to hit every element
# Space Complexity: O(N) - Works on preexisting matrix, may have to store M zero_cols
def zero_out_2(mat: [[]]) -> [[]]:
    """ Has all test cases passing.
    >>> zero_out_2([[1]])
    [[1]]
    >>> zero_out_2([[1, 0], [3, 4]])
    [[0, 0], [3, 0]]
    >>> zero_out_2([[0, 2, 3], [4, 5, 6], [7, 8, 0]])
    [[0, 0, 0], [0, 5, 0], [0, 0, 0]]
    >>> zero_out_2([[1, 2, 3, 4, 5], [6, 0, 8, 9, 10], [11, 5, 13, 14, 15], [16, 1, 18, 19, 20], [21, 0, 23, 24, 25]])
    [[1, 0, 3, 4, 5], [0, 0, 0, 0, 0], [11, 0, 13, 14, 15], [16, 0, 18, 19, 20], [0, 0, 0, 0, 0]]
    >>> zero_out_2([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 0, 16]])
    [[1, 2, 0, 4], [5, 6, 0, 8], [9, 10, 0, 12], [0, 0, 0, 0]]
    >>> zero_out_2([[1, 0, 0, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 1, 16]])
    [[0, 0, 0, 0], [5, 0, 0, 8], [9, 0, 0, 12], [13, 0, 0, 16]]
    """
    # Max O(M + N) Space
    zero_rows = set()
    zero_cols = set()
    # O(n^2) - O(MxN)
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 0:
                zero_rows.add(i)
                zero_cols.add(j)

    while zero_rows:
        mat[zero_rows.pop()] = [0 for x in range(len(mat[0]))]
    while zero_cols:
        col = zero_cols.pop()
        for row in range(len(mat)):
            mat[row][col] = 0

    return mat

# Time complexity: O(MxN) - - Has to hit every element
# Space Complexity: O(1) - No extra space needed, just a few(constant) more passes.
def zero_out_3(mat: [[]]) -> [[]]:
    """ Has all test cases passing.
    >>> zero_out_3([[1]])
    [[1]]
    >>> zero_out_3([[1, 0], [3, 4]])
    [[0, 0], [3, 0]]
    >>> zero_out_3([[0, 2, 3], [4, 5, 6], [7, 8, 0]])
    [[0, 0, 0], [0, 5, 0], [0, 0, 0]]
    >>> zero_out_3([[1, 2, 3, 4, 5], [6, 0, 8, 9, 10], [11, 5, 13, 14, 15], [16, 1, 18, 19, 20], [21, 0, 23, 24, 25]])
    [[1, 0, 3, 4, 5], [0, 0, 0, 0, 0], [11, 0, 13, 14, 15], [16, 0, 18, 19, 20], [0, 0, 0, 0, 0]]
    >>> zero_out_3([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 0, 16]])
    [[1, 2, 0, 4], [5, 6, 0, 8], [9, 10, 0, 12], [0, 0, 0, 0]]
    >>> zero_out_3([[1, 0, 0, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 1, 16]])
    [[0, 0, 0, 0], [5, 0, 0, 8], [9, 0, 0, 12], [13, 0, 0, 16]]
    """

    # O(n^2) - O(MxN) Time
    # O(1) Space
    rows = len(mat)
    cols = len(mat[0])
    row_0_has_0 = False
    col_0_has_0 = False

    for col in range(cols):
        if mat[0][col] == 0:
            row_0_has_0 = True
            break

    for row in range(rows):
        if mat[row][0] == 0:
            col_0_has_0 = True
            break

    for row in range(1, rows):
        for col in range(1, cols):
            if mat[row][col] == 0:
                mat[row][0] = 0
                mat[0][col] = 0
    # mat now has zeros on first col and row

    def nullify_row(row: int):
        for col in range(cols):
            mat[row][col] = 0

    def nullify_col(col: int):
        for row in range(rows):
            mat[row][col] = 0

    for row in range(1, rows):
        if mat[row][0] == 0:
            nullify_row(row)

    for col in range(1, cols):
        if mat[0][col] == 0:
            nullify_col(col)

    if col_0_has_0:
        nullify_col(0)

    if row_0_has_0:
        nullify_row(0)

    return mat

doctest.testmod()
