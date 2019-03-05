def max_profit(work_array):
    dp = [0 for _ in range(len(work_array))]
    dp[-1] = work_array[-1][0]
    for i in range(len(work_array)-2,-1,-1):
        a = work_array[i][0] + dp[ i + work_array[i][1]] if i+work_array[i][1]<len(work_array) else work_array[i][0]
        dp[i] = max(a, dp[i+1])
    print(dp)
    return dp[0]

work1 = [(1,2),(2,2),(3,3),(4,2)]
work2 = [(10,7),(1,1),(1,1),(10,5)]
work3 = [(13,7),(1,1),(1,1),(10,5)]
work4 = [(10,2),(1,2),(1,2),(10,2)]
ans = max_profit(work4)
print(ans)