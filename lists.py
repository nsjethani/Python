def cellCompete(states, days):
    # WRITE YOUR CODE HERE
    temp = []
    n = 8
    for i in range(n + 1):
        temp.append(0)
    for i in range(n):
        temp[i] = states[i]

    while (days > 0):
        print(states)
        # Finding next values for corner cells
        temp[0] = 0 ^ states[1]
        temp[n - 1] = 0 ^ states[n - 2]

        # Compute values of intermediate cells
        # If both cells active or
        # inactive, then temp[i]=0
        # else temp[i] = 1.
        for i in range(1, n - 2 + 1):
            print(temp)
            temp[i] = states[i - 1] ^ states[i + 1]

            # Copy temp[] to cells[]
        # for next iteration
        for i in range(n):
            states[i] = temp[i]
        days -= 1
        print(states)
    return states
print(cellCompete([1,0,0,0,0,1,0,0],1))

