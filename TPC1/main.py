import matplotlib.pyplot as plt

data1 = []
keys = []

def leitura():
    f = open("TPC1\\myheart.csv","r",encoding = 'utf-8')
    line0 = f.readline();
    keys = line0.split("\n")[0].split(",")
    for line in f:
        r = line.split("\n")[0].split(",")
        data_tmp = []
        data_tmp.append(int(r[0]))
        data_tmp.append(r[1])
        data_tmp.append(int(r[2]))
        data_tmp.append(int(r[3]))
        data_tmp.append(int(r[4]))
        data_tmp.append(int(r[5]))
        data1.append(data_tmp)
    return;

def distribuicao_sexo():
    s = [[0,0],[0,0]]
    for case in data1:
        if case[1] == 'M':
            if case[5] == 1:
                s[0][0]+=1
            else: s[0][1]+=1
        else:
            if case[5] == 1:
                s[1][0]+=1
            else: s[1][1]+=1
    return ["\tSexo\t", "Casos Positivos", "Casos Negativos"], ["M", "F"], s;

def distribuicao_etarios():
    faixas = []
    intervalos = []
    i = 0#30
    while i < 10:
        faixas.append([0,0])
        intervalos.append( ""+ str((i*5)+30) + "-" + str((i*5)+34) )
        i+=1#i+=10
    for case in data1:
        ind =int((case[0]-30)/5)
        if case[5] == 1:
            faixas[ind][0]+=1
        else:
            faixas[ind][1]+=1
    return ["Intervalo de Idade","Casos Positivos", "Casos Negativos"], intervalos, faixas;

def distribuicao_colestrol():
    intervalo = []
    casos = []
    maior = data1[0][3]
    menor = data1[0][3]
    for case in data1:
        if maior < case[3] and case[3]!=0:
            maior = case[3]
        if menor > case[3] and case[3]!=0:
            menor = case[3]
    i=0
    num = (maior-menor)/10
    while i < num+1:
        intervalo.append( ""+ str((i*10)+menor) + "-" + str((i*10)+menor+9) )
        casos.append([0,0])
        i+=1
    for c in data1:
        ind =int((c[3]-menor)/10)
        if c[5] == 1:
            casos[ind][0]+=1
        else: casos[ind][1]+=1
    return ["Nivel de Colestrol","Casos Positivos", "Casos Negativos"], intervalo, casos;

def distribuicao_printTabela(keys):
    first_line, lista_esquerda, lista_dados = keys
    str1 = "|"
    for x in first_line:
        str1 = str1 + "  " + x + "  |"
    print(str1)
    i = 0
    for case in lista_dados:
        str2 = "|\t" + lista_esquerda[i] + "\t\t|" + "  \t" + str(case[0]) + "  \t|\t" + str(case[1]) + "  \t|"
        print(str2)
        i+=1
    return;

'''Programa'''
leitura()
distribuicao_printTabela(distribuicao_sexo())
distribuicao_printTabela(distribuicao_etarios())
distribuicao_printTabela(distribuicao_colestrol())

'''extra'''
'''def graph_(l0,l1,l2,l3):
    fig, ax = plt.subplots()
    ax.bar(l2, l3)
    ax.set_xlabel(l0[0])
    ax.set_title(l0[1])
    plt.show()'''

#graph_(["Sexo","Distribuição da Doença por Sexo"],distribuicao_sexo())
#graph_(["Intervalo de Idades","Distribuição da Doença por Escalões Etários"],distribuicao_etarios())
#graph_(["Intervalo de valores do colesterol","Distribuição da Doença por Níveis de Colesterol"],distribuicao_colestrol())
