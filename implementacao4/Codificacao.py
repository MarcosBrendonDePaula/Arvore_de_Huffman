import copy
Arvore = {}

#Pegar a raiz da árvore
def PegaRaiz():
    count = 0
    for pegaraiz in Arvore:
        if len(Arvore)-1 == count:
            return pegaraiz
        count+=1
            
#Atribuir codigo para cara caracter
def CriaCodigo(caracter, codigo):

    for x in Arvore:
        if caracter in Arvore[x]:
            if Arvore[x][0] == caracter:
                codigo += '0'
            elif Arvore[x][1] == caracter:
                codigo += '1'

            if x == PegaRaiz():
                print(codigo)
                return codigo

            return CriaCodigo(x, codigo)
            break
            
#Preencher a frequencia que cada caracter aparece                 
def PreencherFrequencias():
    Frequencias = {}
    arqui = open("textocomum.txt", 'r')
    arquivo = arqui.read()
    
    for caracter in arquivo:
        if caracter in Frequencias:
            Frequencias[caracter] += 1
        else:
            Frequencias[caracter] = 1  
                     
    arqui = open("frequencia.txt", 'w')
        
    for item in sorted(Frequencias, key = Frequencias.get):
        texto = item + '-' + str(Frequencias[item]) + '\n'
        arqui.write(texto)

#Criar a árvore que irá ser usada para dar os codigos aos caracteres
def CriaArvore(Lista, name, Arvore):
    
    count = 1
    soma = 0
    for x in sorted(Lista, key = Lista.get):
        if count == 2:
            soma = int(Lista[y]) + int(Lista[x])
            Arvore[str(name) + '_' + str(soma)] = []
            Arvore[str(name) + '_' + str(soma)].append(y)
            Arvore[str(name) + '_' + str(soma)].append(x)
            del Lista[y]
            del Lista[x]
            break
        
        y = x
        count+=1
    
    Lista[str(name) + '_' + str(soma)] = soma
    #print(Lista)
    
    if len(Lista) == 1:
        #print(Arvore)
        return Arvore
    else:
        return CriaArvore(Lista, name+1, Arvore)

#Preencher os codigos de cada caracter no arquivo tabeladecodigos  
def PreencherTabelaCodigos():
    Lista = {}
    ################Salvar a frenquencia###############
    arqui = open("frequencia.txt", 'r')
    arquivo = arqui.readlines()
    
    flag = False
    for x in arquivo:
        save = x.split('-')
        if flag == True:#Flag True, então linha anterior tinha o \n
            Lista['\n'] = int(save[1])
            flag = False
        else:
            if save[0] == '\n':
                flag = True
            else:
                Lista[save[0]] = int(save[1])
    
    ListaCaracters = copy.deepcopy(Lista)#Copia as entradas do arquivo Frequencias
    CriaArvore(Lista, 1, Arvore)
    
    arqui = open("tabeladecodigos.txt", 'w')
    for x in ListaCaracters.items():
        arqui.write(x[0] + '-' + CriaCodigo(x[0], '')[::-1] + '\n')

#Criar o arquivo codificado de acordo com a tabeladecodigos e textocomum        
def Codificar():
    TabeladeCodigos = {}
    
    arqui = open("tabeladecodigos.txt", 'r')
    arquivo = arqui.readlines()
    
    flag = False
    for x in arquivo:
        save = x.split('-')
        if flag == True:#Flag True, então linha anterior tinha o \n
            save[1] = save[1].split('\n')
            TabeladeCodigos['\n'] = save[1][0]
            flag = False
        else:
            if save[0] == '\n':
                flag = True
            else:
                save[1] = save[1].split('\n')
                TabeladeCodigos[save[0]] = save[1][0]
    
    arqui = open("textocomum.txt", 'r')
    arquivo = arqui.read()
    
    arqui = open("codificado.txt", 'w')
    for x in arquivo:
        if x in TabeladeCodigos:
            arqui.write(TabeladeCodigos[x])
        else:
            print('Teste')
                  
if __name__ == "__main__":

    PreencherFrequencias()
    PreencherTabelaCodigos()
    Codificar()
