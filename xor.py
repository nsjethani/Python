
n1 = 9
n2 = 14
x = n1 ^ n2
setBits = 0

while (x > 0):
    setBits += x & 1
    x >>= 1

print(setBits)