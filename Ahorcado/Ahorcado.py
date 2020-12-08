import random
import os 
AHORCADO = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
          
      O   ||
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

palabras = 'pera manzana uva guineo banana bipolar genio gracias saludo importante anillo comida computadora adios economico adolorido comun salir beber villalona faltar ahorcado ensalda brocoli python gustar maravilloso fabuloso divino rico sabroso interesante enigmatico problematico perro gato loro toro caballo pintura navidad telefono vino romo'.split () 
posicion = random.randint(0, len(palabras) - 1)
list = palabras[posicion]
num = len(list)
arreglo = ["_" for x in range(num)] 
suc = 0
error = 0 
letrasIncorrectas = []

while (suc == 0):
    os.system('cls') 
    print (arreglo)
    print (AHORCADO[error]) 
    print ('Letras incorrectas', letrasIncorrectas)
    print ('Introduzca una letra ')
    letra = input().lower()
    if (letra in list and letra !=""):
        for x in range (num):
            if (list[x] == letra):
                arreglo[x] = letra 
                pass
        pass
    else:
        letrasIncorrectas.append (letra)
        error += 1
        pass 
    if ("_" not in arreglo and error != 6):
        os.system('cls')
        print (arreglo)
        print("YOU WON BRO")
        print   ("  _____")
        print  (" |^   ^|")
        print ("|   *   |")
        print ("---------")
        print ('Quieres jugar de nuevo? S/N?')
        lola = input().upper() 
        if (lola == "S"):
            os.system('cls')
            posicion = random.randint(0, len(palabras) - 1)
            list = palabras[posicion]
            num = len(list)
            arreglo = ["_" for x in range(num)] 
            suc = 0
            error = 0 
            letrasIncorrectas = []
        else:
            suc = 1 
            pass
            
    if ("_" in arreglo and error == 6):
        os.system('cls')
        print (arreglo)
        print (AHORCADO[error])
        print("YOU LOSE BRO, La palabra era: " + palabras[posicion])
        print   ("  _____")
        print  (" |X   X|")
        print ("|   O   |")
        print ("---------")
        print ('Quieres jugar de nuevo? S/N?')
        lola = input().upper() 
        if (lola == "S"):
            os.system('cls')
            posicion = random.randint(0, len(palabras) - 1)
            list = palabras[posicion]
            num = len(list)
            arreglo = ["_" for x in range(num)] 
            suc = 0
            error = 0 
            letrasIncorrectas = []
        else:
            suc = 1 
            pass

input()
    
