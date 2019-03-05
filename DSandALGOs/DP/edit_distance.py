def minDistance(word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: int
    """

    if not word1:
        return len(word2) + 1
    if not word2:
        return len(word1) + 1
    buffer_array = [[0] * (len(word2)+1) for i in range(len(word1)+1)]
    for i in range(len(word1) + 1):
        for j in range(len(word2) + 1):
            if i is 0 and j is 0:
                buffer_array[i][j] = 0
            elif i is 0:
                buffer_array[i][j] = buffer_array[i][j - 1] + 1
            elif j is 0:
                buffer_array[i][j] = buffer_array[i - 1][j] + 1
            else:
                if word1[i - 1] == word2[j - 1]:
                    buffer_array[i][j] = buffer_array[i - 1][j - 1]
                else:
                    buffer_array[i][j] = min(buffer_array[i - 1][j - 1],
                                             buffer_array[i - 1][j],
                                             buffer_array[i][j - 1]) + 1
    return buffer_array[-1][-1]

ans = minDistance("abc","ab")
print(ans)