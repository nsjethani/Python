def minPartition(A,n,S1,S2):
    if(n<0):
        return abs(S1-S2)
    inc = minPartition(A,n-1,S1+A[n],S2)
    exc = minPartition(A,n-1,S1,S2+A[n])
    return min(inc, exc)

A = [10,20,15,5,25]
A = [1,11,6,5]
print(minPartition(A,len(A)-1,0,0))

# Time complexity : 2^n
# space complexity : O(1)


# Dynamic programming
def minPartitionDynamic(A,n,S1,S2,lookup):
    if(n<0):
        return abs(S1-S2)
    key = str(n)+"|"+str(S1)
    print(str(key) + " " + str(key in lookup.keys()))
    if key not in lookup.keys():
        inc = minPartitionDynamic(A,n-1,S1+A[n],S2,lookup)
        exc = minPartitionDynamic(A,n-1,S1,S2+A[n],lookup)
        lookup[key] = min(inc,exc)
    return lookup[key]

lookup = {}
A = [10,20,15,5,25]

print(minPartitionDynamic(A,len(A)-1,0,0,lookup))
