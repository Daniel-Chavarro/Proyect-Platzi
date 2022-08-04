from operator import truediv
import os as os
import random
import re

string_check = re.compile("[@_!#$%^&*()<>?/\|}{~:]")
words = []
liveCounter = 3
validate = []

clear = lambda:os.system("cls")



def words_ext():
    with open("./txt/words.txt", "r", encoding="utf-8") as f:
        for line in f:
            if (string_check.search(line) == None): 
                words.append(line.strip())
            else:
                continue

def setup():
    global word, wordAnonym
    word = random.choice(words)
    word = "abecedario"
    wordAnonym = word
    for i in word:
        wordAnonym = wordAnonym.replace(i, "_")
        




def game():
    wordScreen = wordAnonym
    liveCounterScreen = liveCounter
    for i in range(2000):
        if wordScreen != word:
            letter = str(input("Ingrese la letra \n"))
            global pos
            pos = [n for n,char in enumerate(word) if char == letter]
            if pos != []:
                for p in pos:
                    wordScreen = wordScreen[:p]+letter+wordScreen[p+1:]
                pos = None
                print(wordScreen)
            else:
                print("No hay palabra")
                liveCounterScreen = liveCounterScreen - 1
        elif liveCounterScreen == 0:
            print("Perdiste")
            break

        else:
            print("Ganaste")
            break






def run():
    clear()
    start = int(input("Bienvenido a el Ahorcado\nEscribe 1 para iniciar \n"))
    assert start ==1, "Solo puedes la opcion marcada"
    if start ==1 :
        clear()
        words_ext()
        setup()
        game()



if __name__ == "__main__":
    run()
