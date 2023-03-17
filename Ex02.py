valorInformado = int(input("digite o valor: "))
valorAtualSeq = 0
valorAntigoSeq = 1
stringRes = "valor nao esta na sequencia fibonacci"

while valorAtualSeq <= valorInformado:
    if valorInformado == valorAtualSeq:
        stringRes = "o valor esta na sequencia fibonacci"
    valorAtualSeq += valorAntigoSeq
    if valorAtualSeq == 1:
        valorAntigoSeq = 1
    else:
        valorAntigoSeq = valorAtualSeq - valorAntigoSeq
    
print(stringRes)