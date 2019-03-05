def fib_tab(n):
    tab = [0] * (n+1)
    for i in range(n+1):
        if i<=1:
            tab[i] = i
        if not tab[i]:
            tab[i] = tab[i-1] + tab[i-2]
    return tab[n]

print(fib_tab(9))

def fib_mem(n):
    tab = [0] * (n+1)
    if not tab[n]:
        if n<=1:
            tab[n] = n
        else:
            tab[n] = fib_mem(n-1) + fib_mem(n-2)
    return tab[n]
 
print(fib_mem(9))
