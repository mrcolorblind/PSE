#!/usr/bin/env python
# coding: utf-8

# In[2]:


import math
import numpy as np
import re
import argparse
import os
import glob
from pathlib import Path
import time


# In[105]:

# Atributos da classe:
#     indice: Um indice invertido. As chaves são o id de cada documento.
#     nome_arquivos: Uma lista. O id de cada documento é o índice da lista e o nome do documento o valor.

class Indice_Invertido:
    
    def formataString(self, s):
        s = s.lower()
        s = re.sub("[:,'|.@()?!#$&]"," ", s)
        s = s.replace("\n", " ")
        s = re.sub('[^A-Za-z0-9 ]+', '', s)
        strings = s.split()
        return strings
    
    #Construtor do índice.
    #__author__: João Antonio
    #__parameters: Caminho para o dataset
    #__output__: Um índice invertido do dataset
    def __init__(self, path):
        self.indice = {}
            
        #Guarda o endereço e o nome de todos os arquivos :D
        files = [f for f in glob.glob(path + "**/*", recursive=True)]
        self.nome_arquivos = [os.path.basename(file) for file in files]
        
        arquivos      = [self.formataString(open(file, encoding="latin-1").read()) for file in files]
        
        for i in range(len(arquivos)):
            for word in arquivos[i]:
                if word in self.indice:
                    if i in self.indice[word]:
                        self.indice[word][i] += 1
                    else:
                        self.indice[word][i] = 1
                else:
                    self.indice[word] = {i:1}
    
    def coordenadas(indInv, numDocs):
        coords = np.zeros((len(indInv), numDocs))
        indicePalavra = 0;

        for k, v in indInv.items():
            nx = len(v)
            idf = math.log(numDocs/nx)
            
            for dados in v:
                w = dados[1] * idf
                coords[indicePalavra][dados[0]] = w

            indicePalavra+=1

        return coords

    #essa função deu erro em relação ao k
    def formataQuery(indInv, indQ, numDocs):
        Q = np.zeros((len(indInv),1))
        indicePalavra = 0;
    
        for k, v in indInv.items():
            if k in indQ.keys():
                nx = len(v)
                idf = math.log(numDocs/nx)
                w = (indQ[k])[0][1] * idf
                Q[indicePalavra] = w
            indicePalavra+=1
        return Q

    
    def verificaConsulta(coords, Q):
        resultado = {}
        Q = Q.reshape((len(Q),1))

        for i in range(np.shape(coords)[1]):
            vec = coords[:, i]
            vec = vec.reshape((len(vec),1))
            similaridade = (vec.T @ Q)/(np.linalg.norm(vec) * np.linalg.norm(Q))
            resultado[i] = similaridade[0][0]
        return resultado


# In[106]:


a = Indice_Invertido("../data")

