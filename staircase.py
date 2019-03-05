def number_of_ways_to_top(top, max_step):
    def compute_number_of_ways_to_h(h):
        print("compute", h)
        print(number_of_ways_to_h)
        if h<=1:
            return 1

        if number_of_ways_to_h[h] == 0:
            print(min(max_step,h))
            # a = [compute_number_of_ways_to_h(h-i) for i in range(1,min(max_step,h)+1)]
            # print("a")
            # print(a)
            number_of_ways_to_h[h] = sum(
                compute_number_of_ways_to_h(h-i)
                for i in range(1,
                               min(max_step,h)+1)
            )
        print(number_of_ways_to_h)
        return number_of_ways_to_h[h]


    number_of_ways_to_h = [0] * (top+1)
    return compute_number_of_ways_to_h(top)

# print(number_of_ways_to_top(4,2))


def countWays(n):
    res = [0] * (n + 1)
    res[0] = 1
    res[1] = 1
    res[2] = 2

    for i in range(3, n + 1):
        res[i] = res[i - 1] + res[i - 2] + res[i - 3]

    return res[n]


# # Driver code
# n = 4
# print(countWays(n))




def computeNumberOfWaysToH(n, maximumSteps, m):
    print(m)
    if n<=1:
        return 1
    if m[n] == 0:
        for i in range(1, maximumSteps+1):
            if n-i>=0:
                m[n] += computeNumberOfWaysToH(n-i, maximumSteps, m)
    return m[n]

m = [0] * (4+1)
x = computeNumberOfWaysToH(4, 2, [0,0,0,0,0])

print(x)

