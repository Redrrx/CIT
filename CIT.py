import os
import socket
import loger
import time
import net_stuff as net
from requests import *
import subprocess
from art import *
import urllib.request
Art=text2art("    C I T", font='isometric4', chr_ignore=True)
url = 'https://raw.githubusercontent.com/Redrrx/CIT/master/vpn/data/config/server.ovpn'
public_ip = get('https://api.ipify.org').text
IP = socket.gethostbyname(socket.gethostname())
drivers_cleanup = 'tapinstall.exe remove tap0901'
drivers_install = 'tapinstall.exe install OemVista.inf tap0901'
run_vpn='vpn\openvpn.exe'
paragraph_stuff='''                      *CAN I TALK* AKA CIT IS A DUMMY SOLUTION TO BYPASS VIDEO GAMES VOIP RESTRICTIONS.       
                    |  BY ISOLATING THE VOICE CHAT RELAY TO A VPN CONNECTION WITHOUT AFFECTING IN-GAME PERFORMANCE AND LATENCY   |
                    |  KEEP IN MIND THE RESULT WILL VARY FROM MACHINE TO MACHINE DUE NUMEROUS FACTORS SUCH AS NETWORK STABILITY  |
                    |  AND THE TOTAL CONNECTIONS TO THE VPN SERVER.                                                              |
                    |                                                                                                            |
                    |                                                                                                            |
                    | AUTHOR: Yacine Sellami.                                                                                    |
                    | VERSION: RC-1.1                                                                                            |          '''
def presentation_k():
                     print()
                     print(Art)
                     print()
                     print(paragraph_stuff)
def run_main():
    print("[*]Killing previous OPENVPN sessions in case CIT was restarted.")
    os.system('taskkill /f /im openvpn.exe >nul 2>&1')
    os.system('taskkill /f /im openvpn-gui.exe >nul 2>&1')
    os.system('taskkill /f /im TinyOpenVPNGui >nul 2>&1')
    print("[*]Running CIT on " + socket.gethostname() )
    print("[*]The first condition of progress is the removal of censorship.")
    print("[*]Downloading openvpn configuration file from CIT repository.")
    urllib.request.urlretrieve(url,'vpn\data\config\server.ovpn')
    print("[*]Downloaded and applied.")
    time.sleep(2)
    print("[*]Your current local IP is :" +IP)
    print("[*]Refreshing TAP drivers.")
    os.system(drivers_cleanup)
    time.sleep(2)
    os.system(drivers_install)
    print("[*]Setting up DNS servers.")
    net.dns_setup()
    print("[*]Doing network stuff.")
    os.system('ipconfig /flushdns >nul 2>&1')
    os.system('ipconfig /registerdns >nul 2>&1')
    print("[*]Removing previous routes.")
    net.un_routing()
    print("[*]Fixing voice chat master-servers ")
    net.routing_vvx()
    time.sleep(2)
    print("[*]APPLYING R6S VOICE CHAT FIX")
    net.routing_r6()
    print("[*]TESTING EXPERIMENTAL FIX FOR R6S CONSOLES")
    net.routing_r6_console()
    print("[*]TESTING EXPERIMENTAL FIX FOR PUBG")
    net.routing_pubg()
    print("[*]TESTING EXPERIMENTAL FIX FOR FORTNITE")
    net.routing_fortnite()
    print("[*]TESTING EXPERIMENTAL FIX FOR H1Z1")
    net.routing_h1z1()
    print("[*]NOW ISOLATING VOICE CHAT SERVERS TO VPN LAYER")
    print("[*]YOUR CURRENT PUBLIC IP: "+public_ip)
    print("[*]ISOLATING VOICE CHAT TO VPN NETWORK ")
    subprocess.Popen(run_vpn)
    print("[*]Waiting 30 seconds for the vpn to connect do not close")
    time.sleep(25)
os.system('mode con: cols=150 lines=40')
presentation_k()
while True:
    print()
    print()
    a = input("[*]Enter yes to proceed/restart or Ctrl+C to exit: ")
    if a=="yes":
        run_main()
        time.sleep(1)
        print("[*]Running logging procedure for technical purposes, Bring a Pizza with some Coke and have Fun !")
        loger.run_log()
        continue
    elif a=="no": # JunkCode no time to fix this shit.
        print("Cya ! :)")
        break
