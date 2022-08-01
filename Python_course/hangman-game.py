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
    global word, wordScreen
    word = random.choice(words)
    wordScreen = word
    for i in word:
        wordScreen = wordScreen.replace(i, "_ ")


def game():
    for i in range(2000):
        word = "abecedario"
        letter = str(input("Ingrese la letra \n"))
        global pos
        pos = [n for n,char in enumerate(word) if char == letter]






def run():
    clear()
    start = int(input("Bienvenido a el Ahorcado\nEscribe 1 para iniciar \n"))
    assert start ==1, "Solo puedes la opcion marcada"
    if start ==1 :
        clear()
        words_ext()
        setup()
        game()
        print(pos)




if __name__ == "__main__":
    run()
