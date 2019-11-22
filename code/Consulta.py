import numpy as np
import re
import operator
from Indice_Invertido import Indice_Invertido

class Consulta:
    
    def formataString(self, s):
        s = s.lower()
        s = re.sub("[:,'|.@()?!#$&]"," ", s)
        s = s.replace("\n", " ")
        s = re.sub('[^A-Za-z0-9 ]+', '', s)
        strings = s.split()
        return strings
    
    def __init__(self, queryOriginal, indInv):
        self.queryOriginal = queryOriginal
        self.numPalavras = 0
        self.indiceDaConsulta = {}
        self.vetorDaConsulta = np.zeros((indInv.numPalavras,1))
        self.resultado = {}
        self.documentos = {}
        
        self.formataQuery()
        self.constroiIndiceConsulta(indInv)
        
    def formataQuery (self):
        palavrasNaConsulta = self.formataString(self.queryOriginal)
        for palavra in palavrasNaConsulta:
            if palavra in self.indiceDaConsulta:
                self.indiceDaConsulta[palavra] += 1
            else:
                self.indiceDaConsulta[palavra] = 1
                self.numPalavras += 1
                
                
    def constroiIndiceConsulta(self, indInv):
        palavrasCoincidentes = 0
        indicePalavra = 0;
        
        for palavra, docs in indInv.indice.items():
            if palavra in self.indiceDaConsulta.keys():
                nx = len(docs)
                idf = np.log(indInv.numDocs/nx)
                w = self.indiceDaConsulta[palavra] * idf
                self.vetorDaConsulta[indicePalavra,0] = w
                palavrasCoincidentes+=1
                
            indicePalavra+=1
        
        if palavrasCoincidentes != 0:
            self.verificaConsulta(indInv)
        else:
            print("Nada a fazer")

    def verificaConsulta(self, indInv):
        Q = self.vetorDaConsulta
        
        for i in range(np.shape(indInv.coordenadas)[1]):
            vec = indInv.coordenadas[:, i]
            vec = vec.reshape((len(vec),1))
            similaridade = (vec.T @ Q)/(np.linalg.norm(vec) * np.linalg.norm(Q))
            self.resultado[i] = similaridade[0][0]
        
        self.organizaResultado(indInv)
        
    def organizaResultado(self, indInv):
        for idDoc, similaridade in self.resultado.items():
            if similaridade != 0:
                for nomeDoc, idDocIndInv in indInv.arquivos.items():
                    if idDoc == idDocIndInv:
                        self.documentos[nomeDoc] = similaridade
        
        self.documentos = sorted(self.documentos.items(), key=operator.itemgetter(1))
        