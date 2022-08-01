from operator import truediv
import os as os
import random
import re

string_check = re.compile("[@_!#$%^&*()<>?/\|}{~:]")
words = []



clear = lambda:os.system("cls")



def words_ext():
    with open("./txt/words.txt", "r", encoding="utf-8") as f:
        for line in f:
            if (string_check.search(line) == None): 
                words.append(line.strip())
            else:
                continue

def setup():
    global word
    word = random.choice(words)
    




def run():
    clear()
    start = int(input("Bienvenido a el Ahorcado\nEscribe 1 para iniciar \n"))
    assert start ==1, "Solo puedes la opcion marcada"
    if start ==1 :
        clear()
        words_ext()
        setup()
        global inputword
        inputword = str()


if __name__ == "__main__":
    run()
