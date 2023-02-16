import io
import re
from collections import OrderedDict
#import matplotlib

data = OrderedDict()
data1 = []

def leitura():
    f = open("TPC1\\myheart.csv","r",encoding = 'utf-8')
    #file = io.open("TPC1\\myheart.csv","r")
    line0 = f.readline();
    #print(line0)
    keys = re.split(r',',line0)
    #print(keys)
    num_attr = len(keys)
    #print(num_attr)
    pattern = re.compile(r'^[1-9][0-9]*\,(M|F)\,[0-9]+\,[0-9]+\,[0-9]+\,(0|1)$',re.UNICODE)
    #i=0
    for line in f:
        r = re.search(pattern,line)
        sep = re.split(r',',r.group(0))
        data_tmp = []
        data_tmp.append(int(sep[0]))
        data_tmp.append(sep[1])
        data_tmp.append(int(sep[2]))
        data_tmp.append(int(sep[3]))
        data_tmp.append(int(sep[4]))
        data_tmp.append(int(sep[5]))
        #data_tmp[0] = sep[0]
        #data_tmp[1] = sep[1]
        data1.append(data_tmp)
        #i+=1
    #print(data1)
    '''for line in f:
        print(line)'''
    '''for linha in f:
        print(linha)'''

leitura()

num_masculino_total = 0
num_feminino_total = 0
num_masculino_positivo = 0
num_feminino_positivo = 0
num_masculino_negativo = 0
num_feminino_negativo = 0

def distribuicao_sexo():
    for case in data1:
        '''if case[1] == 'M':
            num_masculino_total+=1
            if case[5] == 1:
                num_masculino_positivo+=1'''
        if case[1] == 'M' and case[5] == 1:
            num_masculino_positivo+=1
        elif case[1] == 'F' and case[5] == 1:
            num_feminino_positivo+=1
    print("Número de Casos Masculinos Positivos é: " + str(num_masculino_positivo))
    print("Número de Casos Femininos Positivos é: " + str(num_feminino_positivo))
    return;

#distribuicao_sexo()

''' Função auxiliar '''
def maior():
    maior=0
    for case in data1:
        if maior < case[0]:
            maior = case[0]
    print(maior)

#maior()

''' Função auxiliar '''
def menor():
    menor=data1[0][0]
    for case in data1:
        if menor > case[0]:
            menor = case[0]
    print(menor)

#menor()

'''Função auxiliar'''
def aux():
    lista = []
    lista.append(1)
    lista[0] += 4
    print(lista)

#aux()

def distribuicao_etarios():
    faixas = []
    i = 0
    while i < 10:
        faixas.append([0,0])
        i+=1
    for case in data1:
        ind =int((case[0]-30)/5)
        if case[5] == 1:
            faixas[ind][1]+=1
        else:
            faixas[ind][0]+=1
    #print(faixas)

    '''for case in data1:
        if case[0] >= 30 and case[0] <= 34:
            if case[5] == 1:
                faixa1_positivos+=1
            else: faixa1_negativos+=1
        if case[0] >= 35 and case[0] <= 39:
            if case[5] == 1:
                faixa2_positivos+=1
            else: faixa2_negativos+=1
        if case[0] >= 40 and case[0] <= 44:
            if case[5] == 1:
                faixa3_positivos+=1
            else: faixa3_negativos+=1
        if case[0] >= 45 and case[0] <= 49:
            if case[5] == 1:
                faixa4_positivos+=1
            else: faixa4_negativos+=1
        if case[0] >= 50 and case[0] <= 54:
            if case[5] == 1:
                faixa5_positivos+=1
            else: faixa5_negativos+=1
        if case[0] >= 55 and case[0] <= 59:
            if case[5] == 1:
                faixa3_positivos+=1
            else: faixa3_negativos+=1
        if case[0] >= 60 and case[0] <= 64:
            if case[5] == 1:
                faixa3_positivos+=1
            else: faixa3_negativos+=1
        if case[0] >= 65 and case[0] <= 69:
            if case[5] == 1:
                faixa3_positivos+=1
            else: faixa3_negativos+=1
        if case[0] >= 70 and case[0] <= 74:
            if case[5] == 1:
                faixa3_positivos+=1
            else: faixa3_negativos+=1
        if case[0] >= 75 and case[0] <= 79:
            if case[5] == 1:
                faixa3_positivos+=1
            else: faixa3_negativos+=1'''
    #faixas.append()
    #print("Entre 30 e 34 anos temos: " + str(faixa1_positivos) + " casos positivos e " + str(faixa1_negativos) + " casos negativos.")
    return "", faixas;

#distribuicao_etarios()

def distribuicao_colestrol():
    maior = data1[0][3]
    menor = data1[0][3]
    for case in data1:
        if maior < case[3]:
            maior = case[3]
        if menor > case[3]:
            menor = case[3]
    #print("Maior: " + str(maior) + " Menor: " + str(menor))
    faixas = []
    #while 
    #faixas.append((0,0))
    print(faixas)
    return;

#distribuicao_colestrol()

def distribuicao_printTabela(keys,lis):
    '''string = ""
    for case in keys:
        string.join(case + "\t")'''
    print(keys)#print(string)
    '''for case in lis:
        print(case)'''
    return;

distribuicao_printTabela(distribuicao_etarios())

#programa


#extra