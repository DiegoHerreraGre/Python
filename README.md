# Estructura de juegos y otros pormenores con Python

## Juegos

### Ruleta

La ruleta es un juego de azar en el que se debe adivinar el número que saldrá en la ruleta.

```python
import random

def jugar_ruleta(): # Funcion para jugar la ruleta
    intentos = int(input("¿Cuántas veces quieres jugar? "))
    print(f"\n🎲 Comenzando juego con {intentos} intentos...\n")

    for intento in range(1, intentos + 1):
        ruleta = random.randint(1, 1000) # Genera un numero aleatorio entre 1 y 1000
        suerte = random.randint(1, 1000) # Genera un numero aleatorio entre 1 y 1000

        print(f"Intento #{intento}") # Muestra el numero de intento
        print(f"Ruleta: {ruleta} | Tu número: {suerte}") # Muestra el numero de la ruleta y el numero que eligio el usuario

        if ruleta == suerte:
            print("\n❌ ¡Perdiste! Los números coincidieron.") # Muestra un mensaje de perdedor
            jugar_ruleta() # Llama a la funcion para jugar nuevamente
            break
        else:
            print("✅ ¡Seguiste con suerte!\n") # Muestra un mensaje de ganador
            continue

if __name__ == "__main__": # Si el archivo se ejecuta directamente, se llama a la funcion jugar_ruleta
    jugar_ruleta() # Llama a la funcion para jugar la ruleta

```
