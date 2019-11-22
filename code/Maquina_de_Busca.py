#!/usr/bin/env python
# coding: utf-8

# In[1]:

try:
    import re
    import argparse
    import os
    import glob
    from pathlib import Path
    import time
    from Indice_Invertido import Indice_Invertido
    from Consulta import Consulta
    import numpy as np
except ImportError:
    print("""Você não possui os requisitos necessários para rodar o programa!
    Para rodar a máquina de busca você precisa dos seguintes módulos Python:
    -> re
    -> argparse
    -> os
    -> glob
    -> pathlib
    -> time
    -> numpy
    
    Para instalar qualquer um dos módulo, basta rodar em seu terminal o comando:
    'pip install nomeDoModulo'""")
    exit()

# In[2]:


#Recebendo e atribuindo os argumentos

#Argumentos funcionam apenas em executáveis .py, portanto o código deve ser descomentado quando o código for exportado.

parser = argparse.ArgumentParser()
parser.add_argument("dataset", help="O banco de dados no qual será realizada a pesquisa. Deve ser uma pasta.")
args   = parser.parse_args()


# In[44]:


def consultar():
    queryOriginal = input("Digite o que deseja buscar: \n")
    numeroPesquisa = int(input("Digite quantos resultados você deseja: "))

    start_time = time.time()

    consulta  = Consulta(queryOriginal, indInv)
    resultado = consulta.documentos
    resultado = sorted(resultado, key=lambda x: x[1], reverse = True)
    resultado = resultado[:numeroPesquisa]

    end_time = time.time()

    #Demonstração dos resultados e interação com o usuário
    print("\nBusca realizada em ", indInv.numDocs," documentos em ", end_time - start_time," segundos!")
    print("\nResultados: \n")
    for i in range(len(resultado)):
        nomeArquivo = resultado[i][0].split("/")[-1]
        print(i+1," - ", nomeArquivo)
    print("\n")
    opcao = input("Deseja abrir um dos arquivos?(s/n)")
    if (opcao == "s" or opcao == "S"):
        while(opcao == "s" or opcao == "S"):
            numArquivo = int(input("Digite o numero do arquivo que você deseja abrir:")) - 1
            if (numArquivo >= len(resultado) or numArquivo < 0):
                print("Esse arquivo não foi listado!")
            else:
                arquivo = open(resultado[numArquivo][0], encoding="latin-1").read()
                print("\n\n", arquivo, "\n\n")
                opcao = input("Deseja abrir outro arquivo?(s/n)")
    opcao = input("Deseja fazer outra busca?(s/n)")
    if (opcao == "s" or opcao == "S"):
        consultar()


# In[45]:


# path = "../data"
path = args.dataset
# Uma linha para o executável, a outra para o ipynb

print("Tratando arquivos...")
indInv = Indice_Invertido(path)
print("Arquivos tratados!")
print("\n\n")


# In[46]:


consultar()

