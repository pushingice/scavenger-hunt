import os
import sys
import random

START_CLUE = 2
LAST_CLUE = 10
#CLUE_SPACE = 1000000
CLUE_SPACE = 100
FIRST_CLUE = 12

def gen_clue_list(first, last, space, secret):
    R = random.Random()
    R.seed(secret)
    clue_indexes = []
    for i in range(first, last+1):
        clue_indexes.append(R.randint(1, space))
    clue_indexes[0] = FIRST_CLUE
    return clue_indexes

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

    clue_indexes = gen_clue_list(START_CLUE, LAST_CLUE,
                                 CLUE_SPACE, secret_number)

    template_names = os.listdir(".clue-templates")
    template_names.sort()
    template_data = []

    for t in template_names:
        data = open(".clue-templates/" + t, "r").read()
        template_data.append(data)

    for i in range(0, CLUE_SPACE):
        dir_name = "clues/" + \
            "0"*(len(str(CLUE_SPACE))-1 - len(str(i))) + str(i)
        os.mkdir(dir_name)
        file_name = open(dir_name + "/clue", "w")
        if (i not in clue_indexes):
            file_name.write("Nothing to see here.\n")
        else:

            template_index = clue_indexes.index(i)

            if (template_index < len(template_data)):
                file_name.write(template_data[template_index])
            else:
                file_name.write("Clue: \n")