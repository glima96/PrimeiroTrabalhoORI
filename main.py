import os
import unidecode
import unicodedata
from unidecode import unidecode

def leitura_stopwords(caminho):
    stopwords = []
    stop = open(caminho, "r", encoding='utf-8')
    stopwords = stop.readlines()
    stop.close()
    for i in range(len(stopwords)):
        stopwords[i]= stopwords[i].lower()

    for i in range(len(stopwords)):
        stopwords[i] = unidecode(stopwords[i].replace("\n", ""))

    stopwords=sorted(stopwords)
    return stopwords

def leitura_cancao(caminho):
    # Le o documento canção dos tamanquinhos
    novo_conjunto = []
    novo = []
    vetor_palavras = []

    # Faz um split das linhas com as palavras pra nao ficar numa linha so
    # elimando pontos e virgular desnessarios
    with open(caminho, encoding='utf-8') as file:
        for line in file:
            line = line.replace(",", "")
            representation = line.split(' ')
            for word in representation:
                x = word.encode('utf-8')
                x = x.replace(b'\xe2\x80\xa6', b'')
                word = x.decode('utf-8')
                novo.append(word)
                novo_conjunto.extend(novo)

    final = novo_conjunto

    vetor_palavras = final
    for i in range(len(vetor_palavras)):
        vetor_palavras[i] = vetor_palavras[i].replace("\n", "")

    for i in range(len(vetor_palavras)):
        vetor_palavras[i] = vetor_palavras[i].replace("?", "")

    for i in range(len(vetor_palavras)):
        vetor_palavras[i] = vetor_palavras[i].replace("!", "")
    for i in range(len(vetor_palavras)):
        vetor_palavras[i] = vetor_palavras[i].replace(".", "")
    for i in range(len(vetor_palavras)):
        vetor_palavras[i] = vetor_palavras[i].replace(":", "")


    for i in range(len(vetor_palavras)):
      vetor_palavras[i]=unidecode(vetor_palavras[i].lower())

    vetor_palavras=sorted(vetor_palavras)
    return vetor_palavras


def remove_stopwords(doc,stopwords):

    vetor = []
    vetor = set(doc).difference(stopwords)
    lista_sem_stop = list(vetor)

    return lista_sem_stop

def remove_plural(doc):
    lista=[]
    lista=doc
    for i in range(len(lista)):

        if lista[i][-1]=="s" and lista[i][-2]=="i" and lista[i][-3]=="u":
            lista[i] = lista[i].replace("is", "l")
        elif lista[i][-1]=="s":
            lista[i]=lista[i][:-1]


    return sorted(lista)
def lematizar(doc):
    lista = []
    lista = doc
    for i in range(len(lista)):

        if lista[i][-1] == "o" and lista[i][-2]=="d" and lista[i][-3]=="n" and lista[i][-4]=="a" and lista[i][-5]=="t":
            lista[i]=lista[i].replace("ndo","r")

        elif lista[i][-1] == "o" and lista[i][-2]=="d" and lista[i][-3]=="n" and lista[i][-4]=="e":
            lista[i] = lista[i].replace("ndo", "r")

        elif lista[i][-1] == "m" and lista[i][-2] == "a":
            lista[i] = lista[i].replace("am", "ar")

        elif lista[i][-1] == "a" and lista[i][-2] == "c" and lista[i][-3] == "a" and lista[i][-4] == "n":
            lista[i] = lista[i].replace("ca", "car")

        elif lista[i][-1] == "a" and lista[i][-2] == "d" and lista[i][-3] == "n" and lista[i][-4] == "o" and lista[i][-5] == "p":
            lista[i] = lista[i].replace("onda", "onder")

        elif lista[i][-1] == "a" and lista[i][-2] == "c" and lista[i][-3] == "e" and lista[i][-4] == "u" and lista[i][-5] == "q":
            lista[i] = lista[i].replace("ca", "cer")

        elif lista[i][-1] == "e" and lista[i][-2] == "t" and lista[i][-3] == "s" and lista[i][-4] == "i":
            lista[i] = lista[i].replace("te", "tir")

        elif lista[i][-1] == "o" and lista[i][-2] == "r" and lista[i][-3] == "b":
            lista[i] = lista[i].replace("ro", "rir")

        elif lista[i][-1] == "o" and lista[i][-2] == "h" and lista[i][-3] == "c" and lista[i][-4]=="e":
            lista[i] = lista[i].replace("ho", "har")

        elif lista[i][-1] == "o" and lista[i][-2] == "d" and lista[i][-3] == "a" and lista[i][-4]=="t":
            lista[i] = lista[i].replace("do", "r")

        elif lista[i][-1] == "u" and lista[i][-2] == "i" and lista[i][-3] == "a":
            lista[i] = lista[i].replace("u", "r")

        elif lista[i][-1] == "o" and lista[i][-2] == "d" and lista[i][-3] == "n" and lista[i][-4]=="e":
            lista[i] = lista[i].replace("ndo", "r")

        elif lista[i][-1] == "o" and lista[i][-2] == "d" and lista[i][-3] == "a" and lista[i][-4]=="r":
            lista[i] = lista[i].replace("do", "r")

        elif lista[i][-1] == "o" and lista[i][-2] == "d" and lista[i][-3] == "n" and lista[i][-4]=="a":
            lista[i] = lista[i].replace("ndo", "r")

        elif lista[i][-1] == "e" and lista[i][-2] == "s" and lista[i][-3] == "s" and lista[i][-4]=="a":
            lista[i] = lista[i].replace("sse", "r")

        elif lista[i][-1] == "e" and lista[i][-2] == "s" and lista[i][-3] == "s" and lista[i][-4]=="i":
            lista[i] = lista[i].replace("isse", "er")

        elif lista[i][-1] == "m" and lista[i][-2] == "e" and lista[i][-3] == "z" and lista[i][-4] == "i":
            lista[i] = lista[i].replace("em", "er")

    return sorted(lista)

def aumentativo_diminutivo(doc):
    lista = []
    lista = doc

    for i in range(len(lista)):
        if lista[i][-1] == "o" and lista[i][-2] == "h" and lista[i][-3] == "n" and lista[i][-4] == "i" and lista[i][-5] == "r" and lista[i][-6] == "i":
            lista[i] = lista[i].replace("inho", "o")

        elif lista[i][-1] == "o" and lista[i][-2] == "h" and lista[i][-3] == "n" and lista[i][-4] == "i" and lista[i][-5] == "u" and lista[i][-6] == "q":
            lista[i] = lista[i].replace("quinho", "co")

        elif lista[i][-1] == "o" and lista[i][-2] == "h" and lista[i][-3] == "n" and lista[i][-4] == "i" and lista[i][-5] == "m" and lista[i][-6] == "r":
            lista[i] = lista[i].replace("nho", "no")

        elif lista[i][-1] == "a" and lista[i][-2] == "h" and lista[i][-3] == "n" and lista[i][-4] == "i" and lista[i][-5] == "h" and lista[i][-6] == "c":
            lista[i] = lista[i].replace("chinha", "cho")

        elif lista[i][-1] == "o" and lista[i][-2] == "h" and lista[i][-3] == "n" and lista[i][-4] == "i" and lista[i][-5] == "r" and lista[i][-6] == "a":
            lista[i] = lista[i].replace("inho", "")

        elif lista[i][-1] == "o" and lista[i][-2] == "h" and lista[i][-3] == "n" and lista[i][-4] == "i" and lista[i][-5] == "n" and lista[i][-6] == "i":
            lista[i] = lista[i].replace("inho", "o")

        elif lista[i][-1] == "a" and lista[i][-2] == "h" and lista[i][-3] == "n" and lista[i][-4] == "i" and lista[i][-5] == "t":
            lista[i] = lista[i].replace("tinha", "ta")

        elif lista[i][-1] == "a" and lista[i][-2] == "h" and lista[i][-3] == "n" and lista[i][-4] == "i" and lista[i][-5] == "l":
            lista[i] = lista[i].replace("linha", "la")

        elif lista[i][-1] == "o" and lista[i][-2] == "a" and lista[i][-3] == "d" and lista[i][-4] == "i":
            lista[i] = lista[i].replace("ridao", "ro")

        elif lista[i][-1] == "o" and lista[i][-2] == "a" and lista[i][-3] == "d" and lista[i][-4] == "n":
            lista[i] = lista[i].replace("dao", "de")



    return sorted(lista)

def grava_doc(doc,stop,nome_arquivo):
    arquivo = open(nome_arquivo, "w")

    texto = "StopWords Encontradas"
    arquivo.writelines(texto)
    arquivo.writelines("\n")
    for items in stop:
        arquivo.write(items)
        arquivo.write(" | ")

    arquivo.writelines("\n")
    texto = "Palavras sem StopWords"
    arquivo.writelines(texto)
    arquivo.writelines("\n")


    doc_stop = remove_stopwords(doc, stop)

    for line in doc_stop:
        arquivo.write(line)
        arquivo.write(" | ")

    sem_plural = remove_plural(doc_stop)
    arquivo.writelines("\n")
    texto = "Palavras sem Plural"
    arquivo.write(texto)
    arquivo.writelines("\n")

    for line in sem_plural:
        arquivo.write(line)
        arquivo.write(" | ")

    lematizado = lematizar(sem_plural)

    arquivo.writelines("\n")
    texto = "Palavras Lematizadas"
    arquivo.writelines(texto)
    arquivo.writelines("\n")

    for line in lematizado:
        arquivo.write(line)
        arquivo.write(" | ")

    au = aumentativo_diminutivo(lematizado)
    arquivo.writelines("\n")
    texto = "Palavras sem Diminutivo e Aumentativo Estagio Final"
    arquivo.write(texto)
    arquivo.writelines("\n")
    for line in au:
        arquivo.write(line)
        arquivo.write(" | ")

    arquivo.close()

    return au

def gera_dicionario(doc1,stop1,doc2,stop2,doc3,stop3,doc4,stop4,doc5,stop5,doc6,stop6,doc7,stop7):


    doc_stop1 = remove_stopwords(doc1, stop1)
    sem_plural1 = remove_plural(doc_stop1)
    lematizado1 = lematizar(sem_plural1)
    DOC1 = aumentativo_diminutivo(lematizado1)


    doc_stop2 = remove_stopwords(doc2, stop2)
    sem_plural2 = remove_plural(doc_stop2)
    lematizado2 = lematizar(sem_plural2)
    DOC2 = aumentativo_diminutivo(lematizado2)


    doc_stop3 = remove_stopwords(doc3, stop3)
    sem_plural3 = remove_plural(doc_stop3)
    lematizado3 = lematizar(sem_plural3)
    DOC3 = aumentativo_diminutivo(lematizado3)


    doc_stop4 = remove_stopwords(doc4, stop4)
    sem_plural4 = remove_plural(doc_stop4)
    lematizado4 = lematizar(sem_plural4)
    DOC4 = aumentativo_diminutivo(lematizado4)


    doc_stop5 = remove_stopwords(doc5, stop5)
    sem_plural5 = remove_plural(doc_stop5)
    lematizado5 = lematizar(sem_plural5)
    DOC5 = aumentativo_diminutivo(lematizado5)


    doc_stop6 = remove_stopwords(doc6, stop6)
    sem_plural6 = remove_plural(doc_stop6)
    lematizado6 = lematizar(sem_plural6)
    DOC6 = aumentativo_diminutivo(lematizado6)


    doc_stop7 = remove_stopwords(doc7, stop7)
    sem_plural7 = remove_plural(doc_stop7)
    lematizado7 = lematizar(sem_plural7)
    DOC7 = aumentativo_diminutivo(lematizado7)

    PALAVRAS=[]

    for item in DOC1:
        if item not in PALAVRAS:
            PALAVRAS.append(item)

    for item2 in DOC2:
        if item2 not in PALAVRAS:
            PALAVRAS.append(item2)

    for item3 in DOC3:
        if item3 not in PALAVRAS:
            PALAVRAS.append(item3)

    for item4 in DOC4:
        if item4 not in PALAVRAS:
            PALAVRAS.append(item4)

    for item5 in DOC5:
        if item5 not in PALAVRAS:
            PALAVRAS.append(item5)

    for item6 in DOC6:
        if item6 not in PALAVRAS:
            PALAVRAS.append(item6)

    for item7 in DOC7:
        if item7 not in PALAVRAS:
            PALAVRAS.append(item7)

    PALAVRAS=sorted(PALAVRAS)

    return PALAVRAS

def posting(lista,doc1,doc2,doc3,doc4,doc5,doc6,doc7):
    arquivo = open("Posting.txt", "w")

    contador=0
    flag1 = 0
    flag2 = 0
    flag3 = 0
    flag4 = 0
    flag5 = 0
    flag6 = 0
    flag7 = 0

    for linha in lista:
        contador=0
        flag1 = 0
        flag2 = 0
        flag3 = 0
        flag4 = 0
        flag5 = 0
        flag6 = 0
        flag7 = 0
        contador = 0
        for item1 in doc1:
            if linha in item1:
                contador=contador+1;
                flag1=1

        for item2 in doc2:
            if linha in item2:
                contador=contador+1;
                flag2=1

        for item3 in doc3:
            if linha in item3:
                contador=contador+1;
                flag3=1

        for item4 in doc4:
            if linha in item4:
                contador=contador+1;
                flag4=1

        for item5 in doc5:
            if linha in item5:
                contador=contador+1;
                flag5=1

        for item6 in doc6:
            if linha in item6:
                contador=contador+1;
                flag6=1

        for item7 in doc7:
            if linha in item7:
                contador=contador+1;
                flag7=1

        if contador>0:
            arquivo.write(linha)
            arquivo.write("/")
            cont=str(contador)
            arquivo.write(cont)
            arquivo.write("- > ")
            if flag1==1:
                arquivo.write("1/1, ")
            if flag2==1:
                arquivo.write("2/1, ")
            if flag3==1:
                arquivo.write("3/1, ")
            if flag4==1:
                arquivo.write("4/1, ")
            if flag5==1:
                arquivo.write("5/1, ")
            if flag6==1:
                arquivo.write("6/1, ")
            if flag7==1:
                arquivo.write("7/1, ")
            arquivo.writelines("\n")

    return

def dicionario(lista,doc1,doc2,doc3,doc4,doc5,doc6,doc7):
    arquivo = open("Dicionario.txt", "w")

    contador=0
    flag1 = 0
    flag2 = 0
    flag3 = 0
    flag4 = 0
    flag5 = 0
    flag6 = 0
    flag7 = 0
    arquivo.write("                     \t" + "DOC1\t"+ "DOC2\t"+ "DOC3\t"+ "DOC4\t"+ "DOC5\t"+ "DOC6\t" + "DOC7\t")
    arquivo.writelines("\n")
    for linha in lista:
        contador=0
        flag1 = "0"
        flag2 = "0"
        flag3 = "0"
        flag4 = "0"
        flag5 = "0"
        flag6 = "0"
        flag7 = "0"

        for item1 in doc1:
            if linha in item1:
                flag1="1"

        for item2 in doc2:
            if linha in item2:
                flag2="1"

        for item3 in doc3:
            if linha in item3:
                flag3="1"

        for item4 in doc4:
            if linha in item4:
                flag4="1"

        for item5 in doc5:
            if linha in item5:
                flag5="1"

        for item6 in doc6:
            if linha in item6:
                flag6="1"

        for item7 in doc7:
            if linha in item7:
                flag7="1"
        t=len(linha)
        if t>=8:
           arquivo.write(linha +"\t"+"       " + flag1 + "\t" + flag2 + "\t" + flag3 + "\t" + flag4 + "\t" + flag5 + "\t" + flag6 + "\t" + flag7 + "\t")
        elif t<8:
             arquivo.write(linha + "\t" + "       "+"\t" + "       " + flag1 + "\t" + flag2 + "\t" + flag3 + "\t" + flag4 + "\t" + flag5 + "\t" + flag6 + "\t" + flag7 + "\t")

        arquivo.writelines("\n")

    return

doc1 = leitura_cancao("./textos/A_Canção_dos_tamanquinhos_Cecília_Meireles.txt")
stop1 = leitura_stopwords("./stopwords/stopwords_A_cancao_dos_tamanquinhos.txt")
caminho_doc1="DOC1-A_Canção_dos_tamanquinhos_Cecília_Meireles.txt"

doc2 = leitura_cancao("./textos/A_Centopeia_Marina_Colasanti.txt")
stop2 = leitura_stopwords("./stopwords/stopwords_a_centopeia.txt")
caminho_doc2="DOC2-A_Centopeia_Marina_Colasanti.txt"

doc3 = leitura_cancao("./textos/A_porta_Vinicius_de_Moraes.txt")
stop3 = leitura_stopwords("./stopwords/stopwords_a_porta_.txt")
caminho_doc3="DOC3-A_porta_Vinicius_de_Moraes.txt"

doc4 = leitura_cancao("./textos/Ao_pé_de_sua_criança_Pablo_Neruda.txt")
stop4 = leitura_stopwords("./stopwords/stopwords_ao_pe_de_sua_crianca.txt")
caminho_doc4="DOC4-Ao_pé_de_sua_criança_Pablo_Neruda.txt"

doc5 = leitura_cancao("./textos/As_borboletas_Vinicius_de_Moraes.txt")
stop5 = leitura_stopwords("./stopwords/stopwords_as_borboletas.txt")
caminho_doc5="DOC5-As_borboletas_Vinicius_de_Moraes.txt"

doc6 = leitura_cancao("./textos/Convite_José_Paulo_Paes.txt")
stop6 = leitura_stopwords("./stopwords/stopwords_convite.txt")
caminho_doc6="DOC6-Convite_José_Paulo_Paes.txt"

doc7 = leitura_cancao("./textos/Pontinho_de_Vista_Pedro_Bandeira.txt")
stop7 = leitura_stopwords("./stopwords/stopwords_pontinho_de_vista.txt")
caminho_doc7="DOC7-Pontinho_de_Vista_Pedro_Bandeira.txt"

doc1=grava_doc(doc1,stop1,caminho_doc1)
doc2=grava_doc(doc2,stop2,caminho_doc2)
doc3=grava_doc(doc3,stop3,caminho_doc3)
doc4=grava_doc(doc4,stop4,caminho_doc4)
doc5=grava_doc(doc5,stop5,caminho_doc5)
doc6=grava_doc(doc6,stop6,caminho_doc6)
doc7=grava_doc(doc7,stop7,caminho_doc7)
lista=[]
lista=gera_dicionario(doc1,stop1,doc2,stop2,doc3,stop3,doc4,stop4,doc5,stop5,doc6,stop6,doc7,stop7)
posting(lista,doc1,doc2,doc3,doc4,doc5,doc6,doc7)
dicionario(lista,doc1,doc2,doc3,doc4,doc5,doc6,doc7)
print("Arquivos gerados com sucesso!")

