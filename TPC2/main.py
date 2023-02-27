import sys

soma = 0
boo = True
separadores = ['_', ' ', '-', ';', ',']
separador = ""

for line in sys.stdin:
    elements = []
    if separador == "" or separador in separadores:
        for x in separadores:
            if x in line:
                separador = x
        elements = line.split(separador)
    else :
        elements = [line]
    elements[len(elements)-1] = elements[len(elements)-1].split("\n")[0]
    for elem in elements:
        if   "off" == elem.lower() and boo:
            boo = False
        elif "on" == elem.lower() and (not boo):
            boo = True
            continue
        elif "=" == elem:
            print(soma)
            sys.exit()
        if boo and elem.isdigit():
            soma += float(elem)
