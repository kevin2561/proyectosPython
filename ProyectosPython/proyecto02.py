import random
import os
def run():
    BD= [ "JAVASCRIPT", "PHP", "JAVA","ANGULAR","REACT","MATEMATICAS","COMUNICACION"]
    images = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
    word= random.choice(BD)
    spaces= ["_"] * len(word)
    attemps= 6
    while True:
        os.system("cls")
        for character in spaces:
            print(character,end=" ")
        print(images[attemps])
        lellter= input("Ingrese la letra" ).upper()
        found= False
        for idx,character in enumerate(word):
            if character == lellter:
                spaces[idx]= lellter
                found= True

        if not  found:
            attemps-= 1

        if "_" not in spaces:
            os.system("cls")    
            print("Has acertado")
            break
            input()

        if attemps == 0:
            os.system("cls")    
            print("Perdiste")
            break
            input()
            

    

if  __name__ == '__main__':
    run()