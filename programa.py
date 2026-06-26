"""11. Escribe un programa para adivinar una palabra, el programa escoger una palabra de una lista
aleatoria de palabras y el usuario tiene que escoger una letra hasta encontrar todas las letras
que conforman la palabra, el usuario tiene hasta 5 intentos para adivinar la palabra, si se
equivoca al escoger la letra se le debe reducir un intento, el juego acaba cuando el usuario
adivina todas las letras que conforma la palabra"""

import random

PALABRAS = ["uno","dos","tres"]

CLAVE = random.choice(PALABRAS)

intento = ""

for i in range(5):
    print(f"\n\t ..::  INTENTO N°{5-i}  :..")


    letra = input("Digite una letra de la palabra : ")
    if letra in CLAVE:
        intento+= letra
        print(f" LA LETRA {letra} SI ESTA EN LA PALABRA CLAVE  ✅")
        
        if len(intento) == len(CLAVE):
            print(f"FELICIDADES : LA PALABRA ES -> {CLAVE}   ")
            break
    
    else:
        print(f" LA LETRA {letra}  NO ESTA EN LA PALABRA CLAVE ❌ ")



print("\n\t ..::   PROGRAMA FINALIZADO   ::..")
    