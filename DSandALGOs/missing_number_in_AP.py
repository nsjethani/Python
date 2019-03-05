def missingNumUtil(arr, low, high, d):
    #there should be at least 2 elements in the array
    if high <= low:
        return None
    # find index of middle element
    mid = low + (high-low)//2

    # find if element just after mid is missing or not
    if arr[mid+1] != arr[mid]+d:
        return arr[mid] + d

    # find if the element before the mid element is missing or not
    if mid > 0 and arr[mid-1] != arr[mid] - d:
        return arr[mid] - d

    if arr[mid] == arr[0] + mid*d:
        return missingNumUtil(arr, mid+1, high, d)

    return missingNumUtil(arr, low, mid-1, d)

def findMissing(arr, n):
    d = (arr[n-1] - arr[0])/n
    return missingNumUtil(arr, 0, n-1, d)

arr = [2,4,6,10]
n = len(arr)
print(findMissing(arr, n))