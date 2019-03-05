import collections
def is_palindrome(s1):
    low, high = 0, len(s1)-1
    while low < high:
        if s1[low] != s1[high]:
            return False
        low+=1
        high-=1
    return True

def make_palindrome(str):
    low, high = 0, len(str)-1
    while low<high:
        if str[low]==str[high]:
            low+=1
            high-=1
        else:
            if(is_palindrome(str[low+1:high+1])):
                return low
            elif(is_palindrome(str[low:high])):
                return high
            return -1
    return -2

def main():
    # value = "abcbea"
    # value = "abcba"
    value = "abcd"
    idx = make_palindrome(value)
    if idx == -1:
        print("Not possible")
    elif idx == -2:
        print("already palindorome")
    else:
        print("remove char at "+str(idx))

def can_make_palindrome(s):
    return sum(v %2 for v in collections.Counter(s).values()) <= 1

main()

print(collections.Counter("Neha").values())
print(can_make_palindrome("nneehhaaa "))