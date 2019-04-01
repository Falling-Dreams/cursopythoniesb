"""
Avaliado por: Rodrigo Guimarãeas
Nota: 10
Observações: 
    - Parabéns pelo ord!
    - Não precisa de parênteses no IF
"""

#4. Desenvolva um codigo onde e possivel verificar se uma letra informada e
#maiuscula ou minuscula.

#letra = int(input("Informe a letra: "))
letra = ord(input("Informe a letra: "))

if (letra >= 65 and letra <= 90): # if letra >= 65 and letra <= 90
	print("maiuscula")

else:
	print("minuscula")
