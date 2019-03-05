def build_matrix(input1, input2):

    mat = [ [0 for i in range(len(input2)+1)] for j in range(len(input1)+1) ]

    answer = []
    for i in range(1,len(input1)+1):
        for j in range(1, len(input2)+1):
            if input1[i-1] == input2[j-1]:
                mat[i][j] = 1 + mat[i-1][j-1]
            else:
                mat[i][j] = max(mat[i-1][j],mat[i][j-1])

    i=len(input1)
    j=len(input2)
    while i!=0 or j!=0:
        if mat[i][j] == mat[i-1][j-1] + 1:
            answer.append(input1[i-1])
            i-=1
            j-=1
        elif mat[i][j] == mat[i-1][j]:
            i-=1
        else:
            j-=1

    return mat[len(input1)][len(input2)],answer



n,s = (build_matrix("abcdef","abcneha"))

print(n)
s.reverse()
print(''.join(s))