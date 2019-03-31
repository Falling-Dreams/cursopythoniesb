#5. Receba varios numeros enquanto nao for informado um numero negativo, 
#apos, informe a media dos numeros recebidos.
x = ''
soma = 0
while x != 0:
	x = int(input('Informe um numero: '))
	soma += x
print("A soma dos numeros e:", soma)

