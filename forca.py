def ChutarLetra(string letra):
    resposta = ""        

    for cont in range(len(palavra)):
        if letra == palavra[cont]:
            resposta += palavra[cont]
            
        else:
            resposta += solucao[cont]
            
    solucao = resposta
    

palavra = input("Digite a palavra a ser advinhada: ").upper()

cabeca = "O"
braco_direito = "/"
braco_esquerdo = "\ "
peito = braco_direito +"|"+ braco_esquerdo
tronco = "|"
pe_direito = "/"
pe_esquerdo = "\ "

forca = "     ______\n    |      |\n    |      "+cabeca+"\n    |     "+peito+"\n    |      "+tronco+"\n    |     "+pe_direito+" "+pe_esquerdo+"\n    |\n___/|\___       "
solucao = "" 

print(forca)

for cont in range(len(palavra)):
    solucao += "X"
    
resposta = ""
    
print("A palavra é:",solucao)

while not (solucao == palavra):
    letra = input("Digite uma letra: ").upper()
        
    resposta = ""        

    for cont in range(len(palavra)):
        if letra == palavra[cont]:
            resposta += palavra[cont]
            
        else:
            resposta += solucao[cont]
            
    solucao = resposta
print(solucao)