import os
import sys
import random

START_CLUE = 2
LAST_CLUE = 10
#CLUE_SPACE = 1000000
CLUE_SPACE = 100

if __name__ == "__main__":

    if (len(sys.argv) != 2):
        sys.exit("Need a secret number")
    secret_number = int(sys.argv[1])

    result = ""
    try:
        result = os.stat("clues")
    except:
        pass

    if (result):
        sys.exit("Clues folder already exists.")

    if (not result):
        os.mkdir("clues")

    R = random.Random()
    R.seed(secret_number)
    clue_indexes = []
    for i in range(START_CLUE, LAST_CLUE+1):
        clue_indexes.append(R.randint(1, CLUE_SPACE))

    print clue_indexes
    for i in range(0, CLUE_SPACE):
        dir_name = "clues/" + \
            "0"*(len(str(CLUE_SPACE))-1 - len(str(i))) + str(i)
        os.mkdir(dir_name)
        file_name = open(dir_name + "/clue", "w")
        if (i not in clue_indexes):
            file_name.write("Nothing to see here.\n")
        else:
            clue_no = START_CLUE + clue_indexes.index(i);
            file_name.write("Clue: " + str(clue_no) + '\n')