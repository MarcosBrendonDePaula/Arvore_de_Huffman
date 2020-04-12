def Decode(Map):
    arqC=open("codificado.txt","r")
    arqD=open("descodificado.txt","w")
    linha=arqC.read()
    strTemp=""
    for i in range(0,len(linha)):
        strTemp+=linha[i]
        if(strTemp in Map):
            arqD.write(Map[strTemp])
            strTemp=""
    pass
    arqC.close()
    arqD.close()

def GenMap():
    arquivo = open("tabeladecodigos.txt")
    Map = {}
    linhas = arquivo.readlines()
    passar=False
    for i in range(0,len(linhas)):
        if (passar):
            passar=False
        else:
            if(linhas[i]=="\n"):
                passar=True
                i+=1
                inputs=linhas[i].split("-")
                Map[inputs[1].split("\n")[0]]="\n"
                pass
            else:
                inputs=linhas[i].split("-")
                Map[inputs[1].split("\n")[0]]=inputs[0]
    return Map
    
if __name__ == "__main__":
    Decode(GenMap())

