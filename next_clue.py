import os
import sys
import random
import hashlib
import generate_clues as gc
import subprocess as sp


def shell_out(comm):
    return sp.run(comm.split(), capture_output=True).stdout.decode()


def check_hint(clue, hint, dictionary):
    if (clue == 3):
        count = len(os.listdir("/usr"))
        return int(hint) == count
    elif (clue == 4):
        hostname = open("/etc/hostname", "r").read().strip()
        return hint == hostname
    elif (clue == 5):
        return hint in ["i","n","-i","-n"]
    elif (clue == 6):
        return hint == os.getenv("PATH").split(":")[0]
    elif (clue == 7):
        return hint == shell_out("which python").strip()
    elif (clue == 8):
        return hint in ["acpi", "denied"]
    elif (clue == 9):
        val = shell_out(f"wc -l {dictionary}").split()[0]
        print(val)
        return hint == val
    elif (clue == 10):
        return hint == shell_out(f"grep -A 1 tactful {dictionary}").strip().split('\n')[1]
    elif (clue == 11):
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
        sys.exit("Need a secret number, clue number, and hint")
    secret_number = int(sys.argv[1])
    clue_number = int(sys.argv[2])
    hint = sys.argv[3]

    clue_indexes = gc.gen_clue_list(gc.START_CLUE, gc.LAST_CLUE,
                                    gc.CLUE_SPACE, secret_number)
    dictionary = open("conf", "r").read().strip()
    
    if (check_hint(clue_number, hint, dictionary)):
        print(gc.zero_pad(clue_indexes[clue_number - gc.START_CLUE]))
    else:
        R = random.Random()
        if (type(hint) == str):
            md5 = hashlib.md5(hint.encode())
            hint_number = int(md5.hexdigest(),16)
        R.seed(secret_number + clue_number + hint_number)
        print(gc.zero_pad(R.randint(1, gc.CLUE_SPACE)))
