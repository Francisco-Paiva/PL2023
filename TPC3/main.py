import re

f = open("PL\\PL2023\\PL2023\\TPC3\\processos.txt","r",encoding = 'utf-8')
pattern = re.compile(r'(\s)*(?P<pasta>[1-9][0-9]*)::(?P<ano>[1-9][0-9]*)-(?P<mes>[0-9]*)-(?P<dia>[0-9]*)::(?P<nome>[A-Za-z ]*)::(?P<pai>[A-Za-z ]*)?::(?P<mae>[A-Za-z ]*)?::(?P<obs>.*)?',re.UNICODE)
arr = []
for line in f:
    match = re.search(pattern,line)
    if match:
        r = match.groupdict()

        arr.append(r)
'''
> a) Calcula a frequência de processos por ano (primeiro elemento da data);
> b) Calcula a frequência de nomes próprios (o primeiro em cada nome) e apelidos (o ultimo em cada nome) por séculos e apresenta os 5 mais usados;
> c) Calcula a frequência dos vários tipos de relação: irmão, sobrinho, etc.;
> d) Converta os 20 primeiros registos num novo ficheiro de output mas em formato **Json**.
'''

def al_a():
    freq_ano = dict()
    for ele in arr:
        if ele['ano'] not in freq_ano:
            freq_ano[ele['ano']] = 1
        else:
            freq_ano[ele['ano']] += 1
    print(freq_ano)

#al_a()

def maior_dic(dic):
    maior = 0
    chave = ''#dic.keys()[0]
    for key in dic.keys():
        value = dic[key]
        if value > maior:
            maior = value
            chave = key
    return maior, chave;

def al_b():
    freq_nome_prop = dict()
    freq_nome_apelido = dict()
    er = re.compile(r'(?P<proprio>[A-Za-z]*)\s+([A-Za-z]*)\s+(?P<apelido>[A-Za-z]*)',re.UNICODE);

    for ele in arr:
        match = er.search(ele['nome']);
        if match:
            r = match.groupdict()
            if r['proprio'] not in freq_nome_prop:
                freq_nome_prop[r['proprio']] = 1
            else:
                freq_nome_prop[r['proprio']] += 1
            if r['apelido'] not in freq_nome_apelido:
                freq_nome_apelido[r['apelido']] = 1
            else:
                freq_nome_apelido[r['apelido']] += 1
    print(maior_dic(freq_nome_prop))
    print(maior_dic(freq_nome_apelido))
    return;
#al_b()

def al_c():
    pattern_obs = re.compile(r'(?P<tio>[\w\s]*,Tio (?:Paterno|Materno))*(?P<primo>[\w\s]*,Primo (?:Paterno|Materno))*(?P<irmao>[\w\s]*,Irmao)*(?P<sobrinho>[\w\s]*,Sobrinho (?:Paterno|Materno))*',re.UNICODE)
    #pattern_obs = re.compile(r'(?P<tio>[\w\s]*,Tio (?:Paterno|Materno))*.*(?P<primo>[A-Za-z ]*,Primo [A-Za-z]*)*.*(?P<irmao>[A-Za-z ]*,Irmao)*.*(?P<sobrinho>[A-Za-z ]*,Sobrinho [A-Za-z]*)*',re.UNICODE)
    #pattern_obs = re.compile(r'([\w\s]*),\s*(?:Tio|Tia|Primo|Prima) (?:Paterno|Materno)')
    #([\w\s]+),(?:Tio|Tia|Primo|Prima) (?:Paterno|Materno)
    dic = dict()
    dic['tio'] = 0
    dic['primo'] = 0
    dic['irmao'] = 0
    dic['sobrinho'] = 0
    for ele in arr:
        match = pattern_obs.search(ele['obs'])
        if match:
            r = match.groupdict()
            if r['tio']:
                dic['tio'] +=1
            if r['irmao']:
                dic['irmao'] +=1
            if r['primo']:
                dic['primo'] +=1
            if r['sobrinho']:
                dic['sobrinho'] +=1
    print("Tios -> " + str(dic['tio']))
    print("Primos -> " + str(dic['primo']))
    print("Irmaos -> " + str(dic['irmao']))
    print("Sobrinhos -> " + str(dic['sobrinho']))
    return;

al_c()

import json

def al_d():
    file_json=open("PL\\PL2023\\PL2023\\TPC3\\processos.json","w+")
    dic = dict()
    dic['processos']= [arr[x] for x in range(0, 20)]
    json.dump(dic,file_json)

#al_d()