import os
import socket
import loger
import time
from requests import *
import subprocess
from art import *

#  current CIT directory for possible future use such as using current openvpn client ( version mismatch between server/client)
#main_dir = os.path.dirname(os.path.realpath('__file__'))


# variable for the logo, a e s t h e t h i c c s
Art=text2art("    C I T", font='isometric4', chr_ignore=True)



# getting the ip over ipify
public_ip = get('https://api.ipify.org').text
# getting the local IPV4 of your host
IP = socket.gethostbyname(socket.gethostname())

# drivers cleaning variables
drivers_cleanup = 'tapinstall.exe remove tap0901'
drivers_install = 'tapinstall.exe install OemVista.inf tap0901'


# The boring network stuff part 1
vivox_ms=socket.gethostbyname('mpx5j.vivox.com')
r6s_vcs=socket.gethostbyname('disp-rbswp-5-1.vivox.com')
pubg_vcs=socket.gethostbyname('ec2-18-220-247-8.us-east-2.compute.amazonaws.com')
vxx1=socket.gethostbyname('mphpp-zmxbp-5-2-5.vivox.com')
vxx2=socket.gethostbyname('tst5a.vivox.com')
vxx3=socket.gethostbyname('vdisp-plabdev-5-1.vivox.com')
vxx4=socket.gethostbyname('nmap.vivox.com')
vxx5=socket.gethostbyname('sg-xbd-5-2.vivox.com')
vxx6=socket.gethostbyname('vmph-hrpd-5-1.vivox.com')
vxx7=socket.gethostbyname('74.201.99.77')  #why im i even trying to get the hostname of those ip's ?
vxx8=socket.gethostbyname('74.201.98.0')



# The boring network stuff part 2
route_master = 'cmdp.exe route -p add' + vivox_ms + 'mask' + '255.255.255.255' + IP
route_r6s = 'cmdp.exe route -p add' + r6s_vcs + 'mask' + '255.255.255.255 ' + IP
route_pubg ='cmdp.exe route -p add' + pubg_vcs +'mask' + '255.255.255.255' + IP
route_vxx1 = 'cmdp.exe route -p add' + vxx1 + 'mask' + '255.255.255.255' + IP
route_vxx2 = 'cmdp.exe route -p add' + vxx2 + 'mask' + '255.255.255.255' + IP
route_vxx3 = 'cmdp.exe route -p add' + vxx3 + 'mask' + '255.255.255.255' + IP
route_vxx4 = 'cmdp.exe route -p add' + vxx4 + 'mask' + '255.255.255.255' + IP
route_vxx5 = 'cmdp.exe route -p add' + vxx5 + 'mask' + '255.255.255.255' + IP
route_vxx6 = 'cmdp.exe route -p add' + vxx6 + 'mask' + '255.255.255.255' + IP
route_vxx7 = 'cmdp.exe route -p add' + vxx7 + 'mask' + '255.255.255.255' + IP
route_vxx8 = 'cmdp.exe route -p add' + vxx8 + 'mask' + '255.255.255.255' + IP
route_pubgx = 'cmdp.exe route -p add 18.0.0.0/8 '+ IP


#Detection of openvpn installation
#openvpn_check = os.path.isdir('C:\Program Files\OpenVPN')

paragraph_stuff='''                      *CAN I TALK* AKA CIT IS A DUMMY SOLUTION TO BYPASS VIDEO GAMES VOIP RESTRICTIONS.       
                    |  BY ISOLATING THE VOICE CHAT RELAY TO A VPN CONNECTION WITHOUT AFFECTING IN-GAME PERFORMANCE AND LATENCY   |
                    |  KEEP IN MIND THE RESULT WILL VARY FROM MACHINE TO MACHINE DUE NUMEROUS FACTORS SUCH AS NETWORK STABILITY  |
                    |  AND THE TOTAL CONNECTIONS TO THE VPN SERVER.                                                              |
                    |                                                                                                            |
                    |  PLEASE KEEP IN MIND THAT THIS VERSION IS EXPERIMENTAL YOU MIGHT ENCOUNTER SOME UNSTABILITY.               |
                    |                                                                                                            |
                    | AUTHOR: Yacine Sellami.                                                                                    |
                    | VERSION: EXP-RELEASE-V2                                                                                    |          '''

#openvpn portable run autostart set

run_vpn='vpn\openvpn.exe'

#def openvpnk():
#             if openvpn_check == True:
#                    print("Openvpn install detected, skipping install")
#             else:
#                 print("[*]Openvpn not detect installing . . .")
#                  os.system("openvpn_setup.exe")

def presentation_k():
                     print()
                     print(Art)
                     print()
                     print(paragraph_stuff)



def run_main():
    print("[*]GO AND DO WHAT YOU'RE BUILT TO DO !")
    print("")
    # Screw the paragraph formatting im hungry and thirsty rn.
    print("[*]Killing previous OPENVPN sessions in case CIT was restarted")
    #os.system('taskkill /f /im TinyOpenVPNGui >nul 2>&1')
    os.system('taskkill /f /im openvpn.exe >nul 2>&1')
    os.system('taskkill /f /im openvpn-gui.exe >nul 2>&1')
    os.system('taskkill /f /im TinyOpenVPNGui >nul 2>&1')

    # show the local ip for no reason honestly i did this to check if its using the TAP driver ip
    print("[*]Your current Local IP is :" +IP)

    # Uninstalling TAP drivers and reinstalling them because that shit is broken and a pain in the ass to handle externally
    print("[*]Refreshing TAP drivers")
    os.system(drivers_cleanup)
    time.sleep(2)
    os.system(drivers_install)
    print("[*]Doing network stuff")

    # basically taking all the vivox servers i was able to find them and route them then isolating them through a vpn connection
    print("[*]Fixing voice chat masterservers ")
    os.system(route_vxx1)
    os.system(route_vxx2)
    os.system(route_vxx3)
    os.system(route_vxx4)
    os.system(route_vxx5)
    os.system(route_vxx6)
    os.system(route_vxx7)
    os.system(route_vxx8)
    os.system(route_master)

    time.sleep(2)

    # Ubisoft with their terrible servers, thank god they use a hostname for their vivox server so its easy and stable
    print("[*]Fixing connectivity between your host and Rainbow six voice chat server")
    os.system(route_r6s)

    # Im not sure if i can blame them due the number of players but they do have a loadton of voice chat servers so i had to catch an entire ip range /8 around 22K ip
    print("[*]TESTING EXPERIMENTAL FIX FOR PUBG")
    os.system(route_pubgx)

    #print("[*]SETTING OPENVPN CFG") metro didn't trust me on this
    print("[*]Done now isolating voice chat layer over VPN")

    time.sleep(2)
    print("[*]CURRENT PUBLIC IP: "+public_ip)

    time.sleep(1)
    print("[*]ISOLATING VOICE CHAT TO VPN NETWORK ")

    subprocess.Popen(run_vpn)
    print("[*]Waiting 45 seconds for the vpn to connect do not close")

    time.sleep(45)


# sometimes openvpn process will stay stuck and refuses to close like a bitch so i had to add another taskkill at the very beginning
os.system('mode con: cols=150 lines=40') # resizing the console window so it won't look like shit with my terrific text formatting skills
presentation_k() # Running that ASCII art diplaying the software name like a Logo

while True:
    print()
    print()
    a = input("[*]Enter yes to proceed/restart or Ctrl+C to exit: ")
    if a=="yes":
        run_main()
        time.sleep(1)
        print("[*]Running logging procedure for technical purposes, Bring a Pizza with some Coke and have Fun !")
        time.sleep(1)
        loger.run_log()
        continue
    elif a=="no": # JunkCode no time to fix this shit.
        print("Cya ! :)")
        break