import os
import sys
import random
import hashlib
import generate_clues as gc

def check_hint(clue, hint):
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
        return hint == os.popen2("which python")[1].read().strip()
    elif (clue == 8):
        return hint in ["acpi", "denied"]
    elif (clue == 9):
        return hint == os.popen2("wc -l /usr/share/dict/words")\
            [1].read().strip().split()[0]
    elif (clue == 10):
        return hint == os.popen2("grep -A 1 tactful /usr/share/dict/words")\
            [1].read().strip().split('\n')[1]
    elif (clue == 11):
        return hint in ("-k 5 -n -r", "-k 5 -r -n", "-r -k 5 -n", "-r -n -k 5",\
            "-n -r -k 5", "-n -k 5 -r")

    

if __name__ == "__main__":

    if (len(sys.argv) != 4):
        sys.exit("Need a secret number, clue number, and hint")
    secret_number = int(sys.argv[1])
    clue_number = int(sys.argv[2])
    hint = sys.argv[3]

    clue_indexes = gc.gen_clue_list(gc.START_CLUE, gc.LAST_CLUE,
                                    gc.CLUE_SPACE, secret_number)
    #print clue_indexes
    if (check_hint(clue_number, hint)):
        print gc.zero_pad(clue_indexes[clue_number - gc.START_CLUE])
    else:
        R = random.Random()
        if (type(hint) == str):
            md5 = hashlib.md5(hint)
            hint_number = int(md5.hexdigest(),16)
        R.seed(secret_number + clue_number + hint_number)
        print gc.zero_pad(R.randint(1, gc.CLUE_SPACE))



