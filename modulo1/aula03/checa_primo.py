def eh_primo(a):
    return all(a % i for i in xrange(2, a))

print(eh_primo(7))