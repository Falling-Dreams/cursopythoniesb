#5. Dada uma frase, informa o termo mais recorrente
#Fonte: https://www.sanfoundry.com/python-program-count-frequency-word-string/
texto = 'Space: the final frontier. These are the voyages of the \
starship Enterprise. Its continuing mission: to explore strange \
new worlds. To seek out new life and new civilizations. To boldly \
go where no one has gone before! '
palavras = []
palavras = texto.split()
#print(palavras)
wordfreq = [palavras.count(p) for p in palavras]
print(dict(zip(palavras,wordfreq)))