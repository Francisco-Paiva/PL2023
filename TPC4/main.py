import re
import json
import io

def create(name,lis):
    file = io.open(name, 'w')
    tam = len(lis)
    x = len(lis[0])
    file.write("[\n")
    z = 1
    y = 1   
    for i in lis:
        file.write("  {\n")
        for key, value in i.items():
            if(isinstance(value, list)):
                if(z==x):
                    #file.write("\t")
                    file.write("\t\t\"%s\":" % key)
                    file.write("[")
                    for i in range(len(value)):
                        if(i==len(value)-1):
                            file.write("%s" % str(value[i]))
                        else:
                            file.write("%s," % str(value[i]))
                    file.write("]\n") 
                    z=1    
                else:
                    file.write("\"%s\":" % key)
                    file.write("[")
                    for i in range(len(value)):
                        if(i==len(value)-1):
                            file.write("%s" % str(value[i]))
                        else:
                            file.write("%s," % str(value[i]))
                    file.write("],\n")            
                    z+=1
            else:        
                if(z==x):
                    file.write("\t\t\"%s\": \"%s\"\n" % (key, value))
                    z=1    
                else:
                    file.write("\t\t\"%s\": \"%s\",\n" % (key, value))
                    z+=1    
        if(y==tam):
            file.write("  }\n")
        else:
            file.write("  },\n")
            y+=1    
    file.write(']\n')

def fun_0():
    f = open("PL\\PL2023\\PL2023\\TPC4\\alunos.csv","r",encoding = 'utf-8')
    temp = f.read().splitlines()
    keys = re.split(r',(?![^\{]*[\}])',temp[0])
    
    arr = []
    for line in temp[1:]:
        val = re.split(r',',line)
        dic = dict()
        i = 0
        while i < len(keys):
            dic[keys[i]] = val[i]
            i+=1
        arr.append(dic)
    create("PL\\PL2023\\PL2023\\TPC4\\alunos.json",arr)
    #file_json=open("alunos.json","w+",encoding = 'utf-8')
    #json.dump(arr,file_json)

fun_0()

def fun_1():
    f = open("PL\\PL2023\\PL2023\\TPC4\\alunos1.csv","r",encoding = 'utf-8')
    temp = f.read().splitlines()
    keys = re.split(r',(?![^\{]*[\}])',temp[0])
    keys_v2 = []
    dicKeys = dict()
    for key in keys:
        if key == '':
            continue
        elif '{' in key and '}' in key :
            pattern = re.compile(r'(\w+)\{([0-9]+)\}',re.UNICODE)
            matche = re.search(pattern, key)
            str1 = matche.group(1)
            num = int(matche.group(2))
            dicKeys[str1] = num
            keys_v2.append(str1)
        else:
            dicKeys[key] = 1
            keys_v2.append(key)
    #print(keys_v2)
    #print(dicKeys)
    arr_values = []
    for line in temp[1:]:
        dic_values = dict()
        val = re.split(r',',line)
        i = 0
        j = 0
        while i < len(keys_v2):
            ind = keys_v2[i]
            if dicKeys[ind] > 1:
                num = dicKeys[ind]
                arr_tmp = []
                j_tmp=0
                while j_tmp < num:
                    #arr_tmp.append(val[j+j_tmp])
                    arr_tmp.append(int(val[j+j_tmp]))
                    j_tmp+=1
                dic_values[ind] = arr_tmp
                j+=num
            else:
                dic_values[ind] = val[i]
            i+=1
            j+=1
        arr_values.append(dic_values)
    #print(arr_values)
    create("PL\\PL2023\\PL2023\\TPC4\\alunos1.json",arr_values)
    #file_json=open("alunos1.json","w+",encoding = 'utf-8')
    #json.dump(arr_values,file_json)

fun_1()

def fun_2():
    f = open("PL\\PL2023\\PL2023\\TPC4\\alunos2.csv","r",encoding = 'utf-8')
    temp = f.read().splitlines()
    keys = re.split(r',(?![^\{]*[\}])',temp[0])
    keys_v2 = []
    dicKeys = dict()
    for key in keys:
        if key == '':
            continue
        elif '{' in key and '}' in key :
            pattern = re.compile(r'(\w+)\{([0-9]+),([0-9]+)\}',re.UNICODE)
            matche = re.search(pattern, key)
            str1 = matche.group(1)
            num_min = int(matche.group(2))
            num_max = int(matche.group(3))
            dic_min_max=dict()
            dic_min_max['min'] = num_min
            dic_min_max['max'] = num_max
            dicKeys[str1] = dic_min_max
            keys_v2.append(str1)
        else:
            dicKeys[key] = 1
            keys_v2.append(key)
    #print(keys_v2)
    #print(dicKeys)
    arr_values = []
    for line in temp[1:]:
        val = re.split(r',',line)
        dic_values = dict()
        i = 0
        j = 0
        while i < len(keys_v2):
            ind = keys_v2[i]
            num = -1
            num_min = num_max = -1
            if type(dicKeys[ind]) == type(1):
                num = dicKeys[ind]
            else:
                num = dicKeys[ind]['min']
                num_min = dicKeys[ind]['min']
                num_max = dicKeys[ind]['max']
            if num > 1:
                arr_tmp = []
                j_tmp=0
                while j_tmp < num:
                    arr_tmp.append(int(val[j+j_tmp]))
                    j_tmp+=1
                while j_tmp < num_max:
                    if val[j+j_tmp] == '':
                        j_tmp+=1
                        continue
                    else:
                        arr_tmp.append(int(val[j+j_tmp]))
                        j_tmp+=1
                dic_values[ind] = arr_tmp
                j+=j_tmp
            else:
                dic_values[ind] = val[i]
            i+=1
            j+=1
        arr_values.append(dic_values)
    #print(arr_values)
    create("PL\\PL2023\\PL2023\\TPC4\\alunos2.json",arr_values)
    #file_json=open("alunos2.json","w+",encoding = 'utf-8')
    #json.dump(arr_values,file_json)

fun_2()

def soma(lista):
    ret = 0
    for i in lista:
        ret+=i
    return ret

def media(lista):
    return soma(lista)/len(lista)

def fun_3(nome):
    name_path = "PL\\PL2023\\PL2023\\TPC4\\" + nome
    name = name_path + ".csv"
    f = open(name,"r",encoding = 'utf-8')
    temp = f.read().splitlines()
    keys = re.split(r',(?![^\{]*[\}])',temp[0])
    keys_v2 = []
    dicKeys = dict()
    for key in keys:
        if key == '':
            continue
        elif '{' in key and '}' in key :
            pattern = re.compile(r'(\w+)\{([0-9]+),([0-9]+)\}::([A-Za-z]+)',re.UNICODE)
            matche = re.search(pattern, key)
            str1 = matche.group(1)
            num_min = int(matche.group(2))
            num_max = int(matche.group(3))
            dic_min_max=dict()
            dic_min_max['min'] = num_min
            dic_min_max['max'] = num_max
            dicKeys[str1] = dic_min_max
            keys_v2.append(str1)
            op = str1 + "_"
            op += matche.group(4)
            dicKeys[op] = -1
            keys_v2.append(op)
        else:
            dicKeys[key] = 1
            keys_v2.append(key)
    #print(keys_v2)
    #print(dicKeys)
    arr_values = []
    for line in temp[1:]:
        lista_prev = []
        val = re.split(r',',line)
        dic_values = dict()
        i = 0
        j = 0
        while i < len(keys_v2):
            ind = keys_v2[i]
            num = -1
            num_min = num_max = -1
            if type(dicKeys[ind]) == type(1):
                num = dicKeys[ind]
            else:
                num = dicKeys[ind]['min']
                num_min = dicKeys[ind]['min']
                num_max = dicKeys[ind]['max']
            if num > 1:
                arr_tmp = []
                j_tmp=0
                while j_tmp < num:
                    arr_tmp.append(int(val[j+j_tmp]))
                    j_tmp+=1
                while j_tmp < num_max:
                    if val[j+j_tmp] == '':
                        j_tmp+=1
                        continue
                    else:
                        arr_tmp.append(int(val[j+j_tmp]))
                        j_tmp+=1
                lista_prev = arr_tmp.copy()
                j+=j_tmp
            elif num == -1:
                if "_sum" in ind:
                    dic_values[ind] = soma(lista_prev)
                elif "_media" in ind:
                    dic_values[ind] = media(lista_prev)
            else:
                dic_values[ind] = val[i]
            i+=1
            j+=1
        arr_values.append(dic_values)
    #print(arr_values)
    name = name_path + ".json"
    create(name,arr_values)
    #file_json=open(name,"w+",encoding = 'utf-8')
    #json.dump(arr_values,file_json)

fun_3("alunos3")
fun_3("alunos4")
