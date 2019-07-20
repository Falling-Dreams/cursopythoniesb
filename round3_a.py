n,m,a = map(int,input().split())
#n,m,a = 6,6,4
if n % a != 0:
	coluna = n//a + 1
else:
	coluna = n//a
if m % a != 0:
	linha = m//a + 1
else:
	linha = m//a
ans = linha * coluna
print(ans)