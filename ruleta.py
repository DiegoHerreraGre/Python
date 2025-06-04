import random

def jugar_ruleta():
    intentos = int(input("¿Cuántas veces quieres jugar? "))
    print(f"\n🎲 Comenzando juego con {intentos} intentos...\n")
    
    for intento in range(1, intentos + 1):
        ruleta = random.randint(1, 1000)
        suerte = random.randint(1, 1000)
        
        print(f"Intento #{intento}")
        print(f"Ruleta: {ruleta} | Tu número: {suerte}")
        
        if ruleta == suerte:
            print("\n❌ ¡Perdiste! Los números coincidieron.")
            jugar_ruleta()
            break
        else:
            print("✅ ¡Seguiste con suerte!\n")
            continue

if __name__ == "__main__":
    jugar_ruleta()

