#4. Ao informar um numero, responda se o mesmo e primo.
x = 5
print(all(x % i for i in xrange(2, x)))