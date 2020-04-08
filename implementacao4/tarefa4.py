
def LerArquivo(Nome):
    arqui = open(Nome + ".txt", 'r')
    str_arqui = arqui.read()
    
    return str_arqui
    
def PreencherFrequencias():
    Frequencias = {}
    arquivo = LerArquivo("arquivo")
    
    for caracter in arquivo:
        if caracter in Frequencias:
            Frequencias[caracter] += 1
        else:
            Frequencias[caracter] = 1  
                     
    arqui = open("frequencia.txt", 'w')
        
    for item in sorted(Frequencias, key = Frequencias.get):
        texto = item + ': ' + str(Frequencias[item]) + '\n'
        arqui.write(texto)
    
    return Frequencias

if __name__ == "__main__":

    print(PreencherFrequencias())


