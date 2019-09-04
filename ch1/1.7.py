import doctest

# Time Complexity: O(n^2) - Best, because we have to hit all the elements.
# Space Complexity: O(1) - No extra space needed other than the 1 temp variable
def rotate_matrix_1(mat: [[]]) -> [[]]:
    """
    >>> rotate_matrix_1([[1]])
    [[1]]
    >>> rotate_matrix_1([[1, 2], [3, 4]])
    [[3, 1], [4, 2]]
    >>> rotate_matrix_1([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    >>> rotate_matrix_1([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]])
    [[21, 16, 11, 6, 1], [22, 17, 12, 7, 2], [23, 18, 13, 8, 3], [24, 19, 14, 9, 4], [25, 20, 15, 10, 5]]
    >>> rotate_matrix_1([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
    [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]]
    """

    temp = 0
    n = len(mat)
    for i in range(int((len(mat))/2)):
        for j in range(i, len(mat)-i-1):
            temp = mat[i][j]
            mat[i][j] = mat[n-j-1][i]
            mat[n-j-1][i] = mat[n-i-1][n-j-1]
            mat[n-i-1][n-j-1] = mat[j][n-i-1]
            mat[j][n-i-1] = temp

    return mat

doctest.testmod()
