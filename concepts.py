l = list(range(256))
print(l)

l = [0] * 256
print(l)

l[10]=10
print(l)

print(ord('a'))
print(chr(97))

def print_freq(word):
    word = list(word)
    freq = [0] * 256
    for i in range(len(word)):
        freq[ord(word[i])] += 1
    for i in range(len(freq)):
        if freq[i] > 0:
            print ("[" + chr(i) + "] = " + str(freq[i]))

print_freq("Hello world")


def reverseWords(self, str):
    def reverse(s, start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1;
            end -= 1

    reverse(str, 0, len(str) - 1)
    i = left = 0
    while i < len(str):
        if str[i] == " ":
            reverse(str, left, i - 1)
            left = i + 1
        elif i == len(str) - 1:
            reverse(str, left, i)
        i += 1

l = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
reverseWords(l)
print(l)