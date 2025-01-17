import os
import sys
import random

START_pista = 2
LAST_pista = 12
pista_SPACE = 100000
FIRST_pista = 12345

def zero_pad(pista):
    l = len(str(pista))
    m = len(str(pista_SPACE)) - 1
    if l < m:
        return "0"*(m-l) + str(pista)
    else:
        return str(pista)

def gen_pista_list(first, last, space, secret):
    R = random.Random()
    R.seed(secret)
    pista_indexes = []
    for i in range(first, last+1):
        pista_indexes.append(R.randint(1, space))
    pista_indexes[0] = FIRST_pista
    return pista_indexes

if __name__ == "__main__":

    if (len(sys.argv) != 2):
        sys.exit("Se necesita un único número, sin espacios, porfavor")
    try:
        secret_number = int(sys.argv[1])
        print("tu número secreto es: ", secret_number)
    except ValueError:
        print(sys.argv[1], "no es un número")

    try:
       val = open("conf", "r").read().strip()
       words = open(val, "r").read().strip()
    except FileNotFoundError:
       sys.exit("No se ha podido localizar el directorio. Por favor, revisa el README.md")

    try:
        os.stat("pistas")
        sys.exit("El directorio pistas ya existe.")
    except FileNotFoundError:
        os.mkdir("pistas")

    pista_indexes = gen_pista_list(START_pista, LAST_pista,
                                 pista_SPACE, secret_number)
    
    try:
       val = open("conf", "r").read().strip()
       words = open(val, "r").read().strip()
    except FileNotFoundError:
       sys.exit("No se ha podido localizar el directorio. Por favor, revisa el README.md")

    template_names = os.listdir(".pista-templates")
    template_names.sort()
    template_data = []

    for t in template_names:
        data = open(".pista-templates/" + t, "r").read()
        template_data.append(data)

    print("escondiendo pista...")
    for i in range(0, pista_SPACE):
        dir_name = "pistas/" + \
            "0"*(len(str(pista_SPACE))-1 - len(str(i))) + str(i)
        os.mkdir(dir_name)
        file_name = open(dir_name + "/pista", "w")
        if (i not in pista_indexes):
            file_name.write("Nada que ver aquí.\n")
        else:

            template_index = pista_indexes.index(i)

            if (template_index < len(template_data)):
                if (template_index == 2):
                    #print template_index, pista_indexes[1]
                    file_name.write(template_data[template_index]
                                    .format(zero_pad(pista_indexes[1]),
                                            zero_pad(pista_indexes[0])))
                else:
                    file_name.write(template_data[template_index])
            else:
                file_name.write("pista: \n")
    print("Pistas escondidas.")
