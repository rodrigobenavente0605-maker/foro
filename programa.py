"""Juego para adivinar una palabra letra por letra.

El programa elige una palabra al azar. El usuario tiene hasta 5 errores para
descubrir todas las letras que forman la palabra.
"""

import random


def pedir_un_caracter(mensaje, letras_registradas):
    while True:
        entrada = input(mensaje).lower()

        if len(entrada) != 1:
            print("Error: Por favor, ingresa solo un caracter.")
        elif entrada in letras_registradas:
            print("Error: Por favor, ingresa una letra no repetida.")
        else:
            return entrada


PALABRAS = [
    "uno",
    "dos",
    "tres",
    "cuatro",
    "cinco",
    "seis",
    "siete",
    "ocho",
    "nueve",
    "diez",
]

CLAVE = random.choice(PALABRAS)
letras_registradas = []
letras_correctas = []
intentos = 5
gana = False

while intentos > 0 and not gana:
    print(f"\n\t ..::  INTENTOS RESTANTES: {intentos}  ::..")

    letra = pedir_un_caracter("Introduce un solo caracter: ", letras_registradas)
    letras_registradas.append(letra)

    if letra in CLAVE:
        letras_correctas.append(letra)
        print(f" LA LETRA {letra} SI ESTA EN LA PALABRA CLAVE ✅ ")

        gana = True

        for letra_clave in CLAVE:
            if letra_clave not in letras_registradas:
                gana = False
                break
    else:
        intentos -= 1
        print(f" LA LETRA {letra} NO ESTA EN LA PALABRA CLAVE ❌ ")

    palabra_mostrada = ""
    for letra_clave in CLAVE:
        if letra_clave in letras_correctas:
            palabra_mostrada += letra_clave
        else:
            palabra_mostrada += "_"

    print(f"Palabra: {palabra_mostrada}")

print("=" * 50)

if gana:
    print(f"\n\t FELICIDADES: LA PALABRA ES -> {CLAVE}")
else:
    print(f"\n\t LA PALABRA ES -> {CLAVE}")

print("\n\t ..::   PROGRAMA FINALIZADO   ::..")