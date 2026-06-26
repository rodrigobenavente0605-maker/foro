"""11. Escribe un programa para adivinar una palabra, el programa escoger una palabra de una lista
aleatoria de palabras y el usuario tiene que escoger una letra hasta encontrar todas las letras
que conforman la palabra, el usuario tiene hasta 5 intentos para adivinar la palabra, si se
equivoca al escoger la letra se le debe reducir un intento, el juego acaba cuando el usuario
adivina todas las letras que conforma la palabra"""

import random

def pedir_un_caracter(mensaje,letras_registradas):
    while True:
        entrada = input(mensaje)
        
        if len(entrada) == 1:
            return entrada  
        
        print("Error: Por favor, ingresa solo un carácter.")


PALABRAS = ["uno","dos","tres"]

CLAVE = random.choice(PALABRAS)

intento = ""

letras_registradas = []

ganó = 0

for i in range(5):
    print(f"\n\t ..::  INTENTO N°{i+1}  :..")


    letra = pedir_un_caracter("Introduce un solo carácter: ",letras_registradas)

    if letra in letras_registradas:
        print("\nERROR: ESA LETRA YA FUE REGISTRADA")

    elif letra in CLAVE:
        intento+= letra
        letras_registradas.append(letra)
        print(f" LA LETRA {letra} SI ESTA EN LA PALABRA CLAVE  ✅")
        
        if len(intento) == len(CLAVE):
            print(f"\n\t ¡¡¡¡¡   FELICIDADES : LA PALABRA ES -> {CLAVE}   !!!!!")
            gano=1
            break
    
    else:
        print(f" LA LETRA {letra}  NO ESTA EN LA PALABRA CLAVE ❌ ")
    



print("="*50)

if ganó == 0 :
    print(f"\n\t  LA PALABRA ES -> {CLAVE}   ")

print("\n\t ..::   PROGRAMA FINALIZADO   ::..")
    