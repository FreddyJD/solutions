def longestCommonSubsequence(text1, text2):
    tl_1 = len(text1)
    tl_2 = len(text2)
    dp_matrix = [[0 for _ in range(tl_2 + 1)] for _ in range(tl_1 + 1)]
    response = 0
    for row in range(1, tl_1 + 1):
        for col in range(1, tl_2 + 1):
            if text1[row - 1] == text2[col - 1]:
                dp_matrix[row][col] = dp_matrix[row - 1][col - 1] + 1
                response = max(dp_matrix[row][col], response)
            else:
                dp_matrix[row][col] = max(dp_matrix[row - 1][col], dp_matrix[row][col - 1])
    return response
