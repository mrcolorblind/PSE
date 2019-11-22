#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import re
import argparse
import os
import glob
from pathlib import Path
import time


# In[3]:


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
        print("1/2")
        self.indice = {}
        self.numDocs = 0
        self.numPalavras = 0
        self.arquivos = {}
        
        for f in glob.glob(path + "**/*", recursive=True):
            words = self.formataString(open(f, encoding="latin-1").read())
            
            self.arquivos[f] = self.numDocs
            self.numDocs += 1
            
            for word in words:
                if word in self.indice:
                    if f in self.indice[word]:
                        self.indice[word][f] += 1
                    else:
                        self.indice[word][f] = 1
                else:
                    self.indice[word] = {f:1}
                    self.numPalavras += 1
                    
        """for k, v in self.indice.items():
            print(k, " -> ", v)"""
        self.encontraCoordenadas()


    def encontraCoordenadas(self):
        print("2/2")
        coords = np.zeros((self.numPalavras, self.numDocs))
        indicePalavra = 0

        for palavra, item in self.indice.items():
            nx  = len(item)
            idf = np.log(self.numDocs/nx)

            for nomeArq, valor in item.items():
                w = valor * idf
                coords[indicePalavra][self.arquivos[nomeArq]] = w

            indicePalavra+=1
        
        self.coordenadas = coords