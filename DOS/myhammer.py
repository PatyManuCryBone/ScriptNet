import subprocess
import pyfiglet

def print_ascii():
    ascii_art = pyfiglet.figlet_format("HAMMER")
    print(ascii_art)
# Chiediamo all'utente il target, la porta e il numero di pacchetti
print_ascii()
target = input("Inserisci il target (IP o dominio): ")
porta = input("Inserisci la porta: ")
pacchetti = input("Inserisci il numero di pacchetti: ")

# Verifica che il numero di pacchetti sia un intero
try:
    pacchetti = int(pacchetti)
except ValueError:
    print("Errore: devi inserire un numero valido per i pacchetti!")
    exit(1)

# Comando per eseguire Hammer
comando = f"sudo python3 /home/kali/DOS/hammer/hammer.py -s {target} -p {porta} -t {pacchetti}"

# Esegui il comando
subprocess.run(comando, shell=True)
