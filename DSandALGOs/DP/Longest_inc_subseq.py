from sys import maxsize
def llis(nums):
    def lis(nums,prev,curpos):
        if curpos == len(nums):
            return 0
        taken = 0
        if nums[curpos] > prev:
            taken = 1 + lis(nums, nums[curpos], curpos+1)
        nottaken  = lis(nums, prev, curpos+1)
        return max(taken, nottaken)
    return lis(nums,-maxsize ,0)

ans = llis([10,9,2,5,3,7,101,18])
print(ans)