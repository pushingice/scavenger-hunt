import os
import sys
import random
import hashlib
import generar_pistas as gc
import subprocess as sp


def shell_out(comm):
    return sp.run(comm.split(), capture_output=True).stdout.decode()


def check_hint(pista, hint, dictionary):
    if (pista == 3):
        count = len(os.listdir("/usr"))
        return int(hint) == count
    elif (pista == 4):
        hostname = open("/etc/hostname", "r").read().strip()
        return hint == hostname
    elif (pista == 5):
        return hint in ["i","n","-i","-n"]
    elif (pista == 6):
        return hint == os.getenv("PATH").split(":")[0]
    elif (pista == 7):
        return hint == shell_out("which touch").strip()
    elif (pista == 8):
        return hint in ["acpi", "denegado"]
    elif (pista == 9):
        val = shell_out(f"wc -l {dictionary}").split()[0]
        print(val)
        return hint == val
    elif (pista == 10):
        return hint == shell_out(f"grep -A 1 tactful {dictionary}").strip().split('\n')[1]
    elif (pista == 11):
        if not hint.startswith("-"):
            return False
        if not ("k 5" in hint or "k5" in hint):
            return False
        if not "r" in hint:
            return False
        if not ("n" in hint or "g" in hint):
            return False
        return True

    
if __name__ == "__main__":

    if (len(sys.argv) != 4):
        sys.exit("Se requiere un número secreto, el número de pista, y la respuesta")
    secret_number = int(sys.argv[1])
    pista_number = int(sys.argv[2])
    hint = sys.argv[3]

    pista_indexes = gc.gen_pista_list(gc.START_pista, gc.LAST_pista,
                                    gc.pista_SPACE, secret_number)
    dictionary = open("conf", "r").read().strip()
    
    if (check_hint(pista_number, hint, dictionary)):
        print(gc.zero_pad(pista_indexes[pista_number - gc.START_pista]))
    else:
        R = random.Random()
        if (type(hint) == str):
            md5 = hashlib.md5(hint.encode())
            hint_number = int(md5.hexdigest(),16)
        R.seed(secret_number + pista_number + hint_number)
        print(gc.zero_pad(R.randint(1, gc.pista_SPACE)))
