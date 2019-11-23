import numpy as np
import re
import argparse
import os
import glob
from pathlib import Path
import time
import Indice_Invertido
import Consulta
import numpy as np

#Testes relacionados ao "Indice_Invertido"
#teste de "formataString"
s = ''
#função lower
strTest_lower = "ABDKdfkjOOk"
try:
    assert Indice_Invertido.Indice_Invertido.formataString(s, strTest_lower) == ['abdkdfkjook']
except AssertionError:
    print('''Erro na função "formataString":
s.lower() não está funcionando corretamente''')

#primeira substituição da função
strTest_sub1 = "aaaa:bbb ' b.cc aaa|b @ (cccd )?aa! # $bb&dda"
try:
    assert Indice_Invertido.Indice_Invertido.formataString(s, strTest_sub1) == ['aaaa', 'bbb', 'b',
                                                                                 'cc', 'aaa', 'b',
                                                                                 'cccd', 'aa', 'bb',
                                                                                 'dda']
except AssertionError:
    print('''Erro na função "formataString":
re.sub("[:,'|.@()?!#$&]"," ", s) não está funcionando corretamente''')

#substituição de parágrafos e split
strTest_parag = '''te
st7
a
ndo'''
try:
    assert Indice_Invertido.Indice_Invertido.formataString(s, strTest_parag) == ['te', 'st7', 'a', 'ndo']
except AssertionError:
    print('''Erro na função "formataString":
s.replace("\ n", " ") ou s.split() não está funcionando corretamente''')

#segunda substituição da função
strTest_sub2 = "têeéstüaâãndoò"
try:
    assert Indice_Invertido.Indice_Invertido.formataString(s, strTest_sub2) == ['testando']
except AssertionError:
    print('''Erro na função "formataString":
re.sub('[^A-Za-z0-9 ]+', '', s) não está funcionando corretamente''')


#conferindo a saída da função
strTest_formStr = '''ABC defs lmNOpQ áfdFDj íJFKjdêfddã 2gh3h4vgÁg~L 058 23848l9 9ÁSSD´8fd43
'!as!é379'] /d|gf\ #aaa#bbdd %sja &3kj3 (984jd )cc *akjs +JSA ds-KK .llLL :sks aa;LL <ee~e =ã>? @báe[
àaa] _è_HH_ { 323}7l
'''
try:
    assert Indice_Invertido.Indice_Invertido.formataString(s, strTest_formStr) == ['abc', 'defs', 'lmnopq',
                                                                                'fdfdj', 'jfkjdfdd',
                                                                                '2gh3h4vggl', '058',
                                                                                '23848l9', '9ssd8fd43',
                                                                                'as', '379', 'd', 'gf',
                                                                                'aaa', 'bbdd', 'sja',
                                                                                '3kj3', '984jd', 'cc',
                                                                                'akjs', 'jsa', 'dskk',
                                                                                'llll', 'sks', 'aall',
                                                                                'eee', 'be', 'aa', 'hh',
                                                                                '3237l']
except AssertionError:
    print('''Erro na saída da função "formataString"''')
	
#testando o construtor __init__
path = 'teste'
indiceInv = Indice_Invertido.Indice_Invertido(path)

try:
    assert indiceInv.indice == {}
except AssertionError:
    print('''Erro no __init__:
self.indice não está correto''')
    
try:
    assert indiceInv.numDocs == 0
except AssertionError:
    print('''Erro no __init__:
self.numDocs não está correto''')

try:
    assert indiceInv.numPalavras == 0
except AssertionError:
    print('''Erro no __init__:
self.numPalavras não está correto''')
    
try:
    assert indiceInv.arquivos == {}
except AssertionError:
    print('''Erro no __init__:
self.arquivos não está correto''')

#Testes relacionados à "Consulta"
#teste de "formataString"
s = ''
#função lower
strTest_lower = "ABDKdfkjOOk"
try:
    assert Consulta.Consulta.formataString(s, strTest_lower) == ['abdkdfkjook']
except AssertionError:
    print('''Erro na função "formataString":
s.lower() não está funcionando corretamente''')

#primeira substituição da função
strTest_sub1 = "aaaa:bbb ' b.cc aaa|b @ (cccd )?aa! # $bb&dda"
try:
    assert Consulta.Consulta.formataString(s, strTest_sub1) == ['aaaa', 'bbb', 'b',
                                                                                 'cc', 'aaa', 'b',
                                                                                 'cccd', 'aa', 'bb',
                                                                                 'dda']
except AssertionError:
    print('''Erro na função "formataString":
re.sub("[:,'|.@()?!#$&]"," ", s) não está funcionando corretamente''')

#substituição de parágrafos e split
strTest_parag = '''te
st7
a
ndo'''
try:
    assert Consulta.Consulta.formataString(s, strTest_parag) == ['te', 'st7', 'a', 'ndo']
except AssertionError:
    print('''Erro na função "formataString":
s.replace("\ n", " ") ou s.split() não está funcionando corretamente''')

#segunda substituição da função
strTest_sub2 = "têeéstüaâãndoò"
try:
    assert Consulta.Consulta.formataString(s, strTest_sub2) == ['testando']
except AssertionError:
    print('''Erro na função "formataString":
re.sub('[^A-Za-z0-9 ]+', '', s) não está funcionando corretamente''')


#conferindo a saída da função
strTest_formStr = '''ABC defs lmNOpQ áfdFDj íJFKjdêfddã 2gh3h4vgÁg~L 058 23848l9 9ÁSSD´8fd43
'!as!é379'] /d|gf\ #aaa#bbdd %sja &3kj3 (984jd )cc *akjs +JSA ds-KK .llLL :sks aa;LL <ee~e =ã>? @báe[
àaa] _è_HH_ { 323}7l
'''
try:
    assert Consulta.Consulta.formataString(s, strTest_formStr) == ['abc', 'defs', 'lmnopq',
                                                                                'fdfdj', 'jfkjdfdd',
                                                                                '2gh3h4vggl', '058',
                                                                                '23848l9', '9ssd8fd43',
                                                                                'as', '379', 'd', 'gf',
                                                                                'aaa', 'bbdd', 'sja',
                                                                                '3kj3', '984jd', 'cc',
                                                                                'akjs', 'jsa', 'dskk',
                                                                                'llll', 'sks', 'aall',
                                                                                'eee', 'be', 'aa', 'hh',
                                                                                '3237l']
except AssertionError:
    print('''Erro na saída da função "formataString"''')
	
#testando o construtor __init__
path = 'teste'
indiceInv = Indice_Invertido.Indice_Invertido(path)
queryOriginal = ''
consulta = Consulta.Consulta(queryOriginal, indiceInv)
try:
    assert consulta.queryOriginal == queryOriginal
except AssertionError:
    print('''Erro no __init__:
self.indice não está correto''')

try:
    assert consulta.numPalavras == 0
except AssertionError:
    print('''Erro no __init__:
self.numPalavras não está correto''')

try:
    assert consulta.indiceDaConsulta == {}
except AssertionError:
    print('''Erro no __init__:
self.indiceDaConsulta não está correto''')
    
try:
    assert consulta.resultado == {}
except AssertionError:
    print('''Erro no __init__:
self.resultado não está correto''')
    
try:
    assert consulta.documentos == {}
except AssertionError:
    print('''Erro no __init__:
self.documentos não está correto''')

#testando "organizaResultado"

Consulta.Consulta.organizaResultado(consulta, indiceInv)
try:
    assert consulta.documentos == []
except AssertionError:
    print('''Erro na função "organizaResultado":
self.documentos não foi alterado corretamente''')

#testando "verificaConsulta"

Consulta.Consulta.verificaConsulta(consulta, indiceInv)
try:
    assert consulta.resultado == {}
except AssertionError:
    print('''Erro na função "verificaConsulta":
self.resultado não foi alterado corretamente''')

#testando "constroiIndiceConsulta"

Consulta.Consulta.constroiIndiceConsulta(consulta, indiceInv)
#como o valor verdade de um array vazio é ambíguo, a alternativa desse caso é fazer um print da resposta
#e conferir se é igual a [], se não, temos um erro.
print(consulta.vetorDaConsulta)

#testando "formataQuery"

Consulta.Consulta.formataQuery(consulta)
try:
    assert consulta.numPalavras == 0
except AssertionError:
    print('''Erro na função "formataQuery":
self.numPalavras não foi alterado corretamente''')
    
try:
    assert consulta.indiceDaConsulta == {}
except AssertionError:
    print('''Erro na função "formataQuery":
self.indiceDaConsulta não foi alterado corretamente''')