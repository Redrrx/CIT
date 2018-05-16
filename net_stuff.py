import socket
import os
IP = socket.gethostbyname(socket.gethostname())
vivox_ms=socket.gethostbyname('mpx5j.vivox.com')
r6s_vcs=socket.gethostbyname('disp-rbswp-5-1.vivox.com')
r6s_vcs1=socket.gethostbyname('mphpp-rbswp-5-1-1.vivox.com')
r6s_vcs2=socket.gethostbyname('mphpp-rbswp-5-1-2.vivox.com')
r6s_vcs3=socket.gethostbyname('mphpp-rbswp-5-1-3.vivox.com')
r6s_vcs4=socket.gethostbyname('mphpp-rbswp-5-1-4.vivox.com')
r6s_vcs5=socket.gethostbyname('mphpp-rbswp-5-1-5.vivox.com')
r6s_vcsp=socket.gethostbyname('disp-rbspsp-5-1.vivox.com')
r6s_vcsp1=socket.gethostbyname('mphpp-rbspsp-5-1-10.vivox.com')
r6s_vcsp2=socket.gethostbyname('mphpp-rbspsp-5-1-1.vivox.com')
r6s_vcsp3=socket.gethostbyname('mphpp-rbspsp-5-1-11.vivox.com')
r6s_vcsp4=socket.gethostbyname('mphpp-rbspsp-5-1-2.vivox.com')
r6s_vcsp5=socket.gethostbyname('mphpp-rbspsp-5-1-12.vivox.com')
r6s_vcsp6=socket.gethostbyname('mphpp-rbspsp-5-1-3.vivox.com')
r6s_vcsp7=socket.gethostbyname('mphpp-rbspsp-5-1-13.vivox.com')
r6s_vcsp8=socket.gethostbyname('mphpp-rbspsp-5-1-4.vivox.com')
r6s_vcsp9=socket.gethostbyname('mphpp-rbspsp-5-1-14.vivox.com')
r6s_vcsp10=socket.gethostbyname('mphpp-rbspsp-5-1-5.vivox.com')
r6s_vcsp11=socket.gethostbyname('mphpp-rbspsp-5-1-15.vivox.com')
r6s_vcsp12=socket.gethostbyname('mphpp-rbspsp-5-1-6.vivox.com')
r6s_vcsp13=socket.gethostbyname('mphpp-rbspsp-5-1-16.vivox.com')
r6s_vcsp14=socket.gethostbyname('mphpp-rbspsp-5-1-7.vivox.com')
r6s_vcsp15=socket.gethostbyname('mphpp-rbspsp-5-1-8.vivox.com')
r6s_vcsp16=socket.gethostbyname('mphpp-rbspsp-5-1-9.vivox.com')
r6s_vcsxb=socket.gethostbyname('disp-rbsxbp-5-1.vivox.com')
r6s_vcsxb1=socket.gethostbyname('mphpp-rbsxbp-5-1-2.vivox.com')
r6s_vcsxb2=socket.gethostbyname('mphpp-rbsxbp-5-1-3.vivox.com')
r6s_vcsxb3=socket.gethostbyname('mphpp-rbsxbp-5-1-4.vivox.com')
r6s_vcsxb4=socket.gethostbyname('mphpp-rbsxbp-5-1-5.vivox.com')
r6s_vcsxb5=socket.gethostbyname('mphpp-rbsxbp-5-1-6.vivox.com')
r6s_vcsxb6=socket.gethostbyname('mphpp-rbsxbp-5-1-7.vivox.com')
r6s_vcsxb7=socket.gethostbyname('mphpp-rbsxbp-5-1-8.vivox.com')
pubg_vcs=socket.gethostbyname('ec2-18-220-247-8.us-east-2.compute.amazonaws.com')
vxx1=socket.gethostbyname('mphpp-zmxbp-5-2-5.vivox.com')
vxx2=socket.gethostbyname('tst5a.vivox.com')
vxx3=socket.gethostbyname('vdisp-plabdev-5-1.vivox.com')
vxx4=socket.gethostbyname('nmap.vivox.com')
vxx5=socket.gethostbyname('sg-xbd-5-2.vivox.com')
vxx6=socket.gethostbyname('vmph-hrpd-5-1.vivox.com')
vxx7=socket.gethostbyname('74.201.99.77')  #why im i even trying to get the hostname of those ip's ?
vxx8=socket.gethostbyname('74.201.98.0')
vxx_fn=socket.gethostbyname('disp-fnwp-5-1.vivox.com')
vxx_fn2=socket.gethostbyname('mphpp-fnwp-5-1-10.vivox.com')
vxx_fn3=socket.gethostbyname('mphpp-fnwp-5-1-11.vivox.com')
vxx_fn4=socket.gethostbyname('mphpp-fnwp-5-1-2.vivox.com')
vxx_fn5=socket.gethostbyname('mphpp-fnwp-5-1-12.vivox.com')
vxx_fn6=socket.gethostbyname('mphpp-fnwp-5-1-3.vivox.com')
vxx_fn7=socket.gethostbyname('mphpp-fnwp-5-1-13.vivox.com')
vxx_fn8=socket.gethostbyname('mphpp-fnwp-5-1-4.vivox.com')
vxx_fn9=socket.gethostbyname('mphpp-fnwp-5-1-14.vivox.com')
vxx_fn10=socket.gethostbyname('mphpp-fnwp-5-1-15.vivox.com')
vxx_fn11=socket.gethostbyname('mphpp-fnwp-5-1-6.vivox.com')
vxx_fn12=socket.gethostbyname('mphpp-fnwp-5-1-7.vivox.com')
vxx_fn13=socket.gethostbyname('mphpp-fnwp-5-1-8.vivox.com')
vxx_fn14=socket.gethostbyname('mphpp-fnwp-5-1-9.vivox.com')
vxx_h1Z1=socket.gethostbyname('disp-h1zp-5-1.vivox.com')
vxx_h1Z12=socket.gethostbyname('mphpp-h1zp-5-1-1.vivox.com')
vxx_h1Z13=socket.gethostbyname('mphpp-h1zp-5-1-2.vivox.com')
vxx_h1Z14=socket.gethostbyname('mphpp-h1zp-5-1-3.vivox.com')
vxx_h1Z15=socket.gethostbyname('mphpp-h1zp-5-1-4.vivox.com')
vxx_h1Z16=socket.gethostbyname('mphpp-h1zp-5-1-5.vivox.com')
route_master = 'cmdp.exe route -p add' + vivox_ms + 'mask' + '255.255.255.255' + IP
route_r6s = 'cmdp.exe route -p add' + r6s_vcs + 'mask' + '255.255.255.255 ' + IP
route_r6s1 = 'cmdp.exe route -p add' + r6s_vcs1 + 'mask' + '255.255.255.255 ' + IP
route_r6s2 = 'cmdp.exe route -p add' + r6s_vcs2 + 'mask' + '255.255.255.255 ' + IP
route_r6s3 = 'cmdp.exe route -p add' + r6s_vcs3 + 'mask' + '255.255.255.255 ' + IP
route_r6s4 = 'cmdp.exe route -p add' + r6s_vcs4 + 'mask' + '255.255.255.255 ' + IP
route_r6s5 = 'cmdp.exe route -p add' + r6s_vcs5 + 'mask' + '255.255.255.255 ' + IP
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
route_r6s_vcsp = 'cmdp.exe route -p add' + r6s_vcsp + 'mask' + '255.255.255.255' + IP
route_r6s_vcsp1 = 'cmdp.exe route -p add' + r6s_vcsp1 + 'mask' + '255.255.255.255' + IP
route_r6s_vcsp2 = 'cmdp.exe route -p add' + r6s_vcsp2 + 'mask' + '255.255.255.255' + IP
route_r6s_vcsp3 = 'cmdp.exe route -p add' + r6s_vcsp3 + 'mask' + '255.255.255.255' + IP
route_r6s_vcsp4 = 'cmdp.exe route -p add' + r6s_vcsp4 + 'mask' + '255.255.255.255' + IP
route_r6s_vcsp5 = 'cmdp.exe route -p add' + r6s_vcsp5 + 'mask' + '255.255.255.255' + IP
route_r6s_vcsp6 = 'cmdp.exe route -p add' + r6s_vcsp6 + 'mask' + '255.255.255.255' + IP
route_r6s_vcsp7 = 'cmdp.exe route -p add' + r6s_vcsp7 + 'mask' + '255.255.255.255' + IP
route_r6s_vcsp8 = 'cmdp.exe route -p add' + r6s_vcsp8 + 'mask' + '255.255.255.255' + IP
route_r6s_vcsp9 = 'cmdp.exe route -p add' + r6s_vcsp9 + 'mask' + '255.255.255.255' + IP
route_r6s_vcsp10 = 'cmdp.exe route -p add' + r6s_vcsp10 + 'mask' + '255.255.255.255' + IP
route_r6s_vcsp11 = 'cmdp.exe route -p add' + r6s_vcsp11 + 'mask' + '255.255.255.255' + IP
route_r6s_vcsp12 = 'cmdp.exe route -p add' + r6s_vcsp12 + 'mask' + '255.255.255.255' + IP
route_r6s_vcsp13 = 'cmdp.exe route -p add' + r6s_vcsp13 + 'mask' + '255.255.255.255' + IP
route_r6s_vcsp14 = 'cmdp.exe route -p add' + r6s_vcsp14 + 'mask' + '255.255.255.255' + IP
route_r6s_vcsp15 = 'cmdp.exe route -p add' + r6s_vcsp15 + 'mask' + '255.255.255.255' + IP
route_r6s_vcsp16 = 'cmdp.exe route -p add' + r6s_vcsp16 + 'mask' + '255.255.255.255' + IP
route_r6s_vcxb = 'cmdp.exe route -p add' + r6s_vcsxb + 'mask' + '255.255.255.255' + IP
route_r6s_vcxb1 = 'cmdp.exe route -p add' + r6s_vcsxb1 + 'mask' + '255.255.255.255' + IP
route_r6s_vcxb2 = 'cmdp.exe route -p add' + r6s_vcsxb2 + 'mask' + '255.255.255.255' + IP
route_r6s_vcxb3 = 'cmdp.exe route -p add' + r6s_vcsxb3 + 'mask' + '255.255.255.255' + IP
route_r6s_vcxb4 = 'cmdp.exe route -p add' + r6s_vcsxb4 + 'mask' + '255.255.255.255' + IP
route_r6s_vcxb5 = 'cmdp.exe route -p add' + r6s_vcsxb5 + 'mask' + '255.255.255.255' + IP
route_r6s_vcxb6 = 'cmdp.exe route -p add' + r6s_vcsxb6 + 'mask' + '255.255.255.255' + IP
route_r6s_vcxb7 = 'cmdp.exe route -p add' + r6s_vcsxb7 + 'mask' + '255.255.255.255' + IP
route_fn = 'cmdp.exe route -p add' + vxx_fn + 'mask' + '255.255.255.255' + IP
route_fn2 = 'cmdp.exe route -p add' + vxx_fn2 + 'mask' + '255.255.255.255' + IP
route_fn3 = 'cmdp.exe route -p add' + vxx_fn3 + 'mask' + '255.255.255.255' + IP
route_fn4 = 'cmdp.exe route -p add' + vxx_fn4 + 'mask' + '255.255.255.255' + IP
route_fn5 = 'cmdp.exe route -p add' + vxx_fn5 + 'mask' + '255.255.255.255' + IP
route_fn6 = 'cmdp.exe route -p add' + vxx_fn6 + 'mask' + '255.255.255.255' + IP
route_fn7 = 'cmdp.exe route -p add' + vxx_fn7 + 'mask' + '255.255.255.255' + IP
route_fn8 = 'cmdp.exe route -p add' + vxx_fn8 + 'mask' + '255.255.255.255' + IP
route_fn9 = 'cmdp.exe route -p add' + vxx_fn9 + 'mask' + '255.255.255.255' + IP
route_fn10 = 'cmdp.exe route -p add' + vxx_fn10 + 'mask' + '255.255.255.255' + IP
route_fn11 = 'cmdp.exe route -p add' + vxx_fn11 + 'mask' + '255.255.255.255' + IP
route_fn12 = 'cmdp.exe route -p add' + vxx_fn12 + 'mask' + '255.255.255.255' + IP
route_fn13 = 'cmdp.exe route -p add' + vxx_fn13 + 'mask' + '255.255.255.255' + IP
route_fn14 = 'cmdp.exe route -p add' + vxx_fn14 + 'mask' + '255.255.255.255' + IP
route_h1z1 = 'cmdp.exe route -p add' + vxx_h1Z1 + 'mask' + '255.255.255.255' + IP
route_h1z12 = 'cmdp.exe route -p add' + vxx_h1Z12 + 'mask' + '255.255.255.255' + IP
route_h1z13 = 'cmdp.exe route -p add' + vxx_h1Z13 + 'mask' + '255.255.255.255' + IP
route_h1z14 = 'cmdp.exe route -p add' + vxx_h1Z14 + 'mask' + '255.255.255.255' + IP
route_h1z15 = 'cmdp.exe route -p add' + vxx_h1Z15 + 'mask' + '255.255.255.255' + IP
route_h1z16 = 'cmdp.exe route -p add' + vxx_h1Z16 + 'mask' + '255.255.255.255' + IP
unroute_master = 'cmdp.exe route delete ' + vivox_ms
unroute_r6s = 'cmdp.exe route delete ' + r6s_vcs
unroute_r6s1= 'cmdp.exe route delete ' + r6s_vcs1
unroute_r6s2= 'cmdp.exe route delete ' + r6s_vcs2
unroute_r6s3= 'cmdp.exe route delete ' + r6s_vcs3
unroute_r6s4= 'cmdp.exe route delete ' + r6s_vcs4
unroute_r6s5= 'cmdp.exe route delete ' + r6s_vcs5
unroute_pubg = 'cmdp.exe route delete ' + pubg_vcs
unroute_vxx1 = 'cmdp.exe route delete ' + vxx1
unroute_vxx2 = 'cmdp.exe route delete ' + vxx2
unroute_vxx3 = 'cmdp.exe route delete ' + vxx3
unroute_vxx4 = 'cmdp.exe route delete ' + vxx4
unroute_vxx5 = 'cmdp.exe route delete ' + vxx5
unroute_vxx6 = 'cmdp.exe route delete ' + vxx6
unroute_vxx7 = 'cmdp.exe route delete ' + vxx7
unroute_vxx8 = 'cmdp.exe route delete ' + vxx8
unroute_pubgx = 'cmdp.exe route delete  18.0.0.0/8'
unroute_fn = 'cmdp.exe route delete ' + vxx_fn
unroute_fn2= 'cmdp.exe route delete ' + vxx_fn2
unroute_fn3= 'cmdp.exe route delete ' + vxx_fn3
unroute_fn4= 'cmdp.exe route delete ' + vxx_fn4
unroute_fn5= 'cmdp.exe route delete ' + vxx_fn5
unroute_fn6= 'cmdp.exe route delete ' + vxx_fn6
unroute_fn7= 'cmdp.exe route delete ' + vxx_fn7
unroute_fn8= 'cmdp.exe route delete ' + vxx_fn8
unroute_fn9= 'cmdp.exe route delete ' + vxx_fn9
unroute_fn10= 'cmdp.exe route delete ' + vxx_fn10
unroute_fn11= 'cmdp.exe route delete ' + vxx_fn11
unroute_fn12= 'cmdp.exe route delete ' + vxx_fn12
unroute_fn13= 'cmdp.exe route delete ' + vxx_fn13
unroute_H1Z1 =  'cmdp.exe route delete ' + vxx_h1Z1
unroute_H1Z12 =  'cmdp.exe route delete ' + vxx_h1Z12
unroute_H1Z13 =  'cmdp.exe route delete ' + vxx_h1Z13
unroute_H1Z14 =  'cmdp.exe route delete ' + vxx_h1Z14
unroute_H1Z15 =  'cmdp.exe route delete ' + vxx_h1Z15
unroute_H1Z16 =  'cmdp.exe route delete ' + vxx_h1Z16
def un_routing():
    os.system(unroute_master + '>nul 2>&1')
    os.system(unroute_pubg + '>nul 2>&1')
    os.system(unroute_pubgx + '>nul 2>&1')
    os.system(unroute_r6s + '>nul 2>&1')
    os.system(unroute_r6s1 + '>nul 2>&1')
    os.system(unroute_r6s2 + '>nul 2>&1')
    os.system(unroute_r6s3 + '>nul 2>&1')
    os.system(unroute_r6s4 + '>nul 2>&1')
    os.system(unroute_r6s5 + '>nul 2>&1')
    os.system(unroute_vxx1 + '>nul 2>&1')
    os.system(unroute_vxx2 + '>nul 2>&1')
    os.system(unroute_vxx3 + '>nul 2>&1')
    os.system(unroute_vxx4 + '>nul 2>&1')
    os.system(unroute_vxx5 + '>nul 2>&1')
    os.system(unroute_vxx6 + '>nul 2>&1')
    os.system(unroute_vxx7 + '>nul 2>&1')
    os.system(unroute_vxx8 + '>nul 2>&1')
    os.system(unroute_fn + '>nul 2>&1')
    os.system(unroute_fn2 + '>nul 2>&1')
    os.system(unroute_fn3 + '>nul 2>&1')
    os.system(unroute_fn4 + '>nul 2>&1')
    os.system(unroute_fn5 + '>nul 2>&1')
    os.system(unroute_fn6 + '>nul 2>&1')
    os.system(unroute_fn7 + '>nul 2>&1')
    os.system(unroute_fn8 + '>nul 2>&1')
    os.system(unroute_fn9 + '>nul 2>&1')
    os.system(unroute_fn10 + '>nul 2>&1')
    os.system(unroute_fn11 + '>nul 2>&1')
    os.system(unroute_fn12 + '>nul 2>&1')
    os.system(unroute_fn13 + '>nul 2>&1')
    os.system(unroute_H1Z1 + '>nul 2>&1')
    os.system(unroute_H1Z12 + '>nul 2>&1')
    os.system(unroute_H1Z13 + '>nul 2>&1')
    os.system(unroute_H1Z14 + '>nul 2>&1')
    os.system(unroute_H1Z15 + '>nul 2>&1')
    os.system(unroute_H1Z16 + '>nul 2>&1')
def routing_vvx():
    os.system(route_vxx1 + '>nul 2>&1')
    os.system(route_vxx2 + '>nul 2>&1')
    os.system(route_vxx3 + '>nul 2>&1')
    os.system(route_vxx4 + '>nul 2>&1')
    os.system(route_vxx5 + '>nul 2>&1')
    os.system(route_vxx6 + '>nul 2>&1')
    os.system(route_vxx7 + '>nul 2>&1')
    os.system(route_vxx8 + '>nul 2>&1')
    os.system(route_master + '>nul 2>&1')
def routing_r6():
    os.system(route_r6s + '>nul 2>&1')
    os.system(route_r6s1 + '>nul 2>&1')
    os.system(route_r6s2 + '>nul 2>&1')
    os.system(route_r6s3 + '>nul 2>&1')
    os.system(route_r6s4 + '>nul 2>&1')
    os.system(route_r6s5 + '>nul 2>&1')
def routing_r6_console():
    os.system(route_r6s_vcsp + '>nul 2>&1')
    os.system(route_r6s_vcsp1 + '>nul 2>&1')
    os.system(route_r6s_vcsp2 + '>nul 2>&1')
    os.system(route_r6s_vcsp3 + '>nul 2>&1')
    os.system(route_r6s_vcsp4 + '>nul 2>&1')
    os.system(route_r6s_vcsp5 + '>nul 2>&1')
    os.system(route_r6s_vcsp6 + '>nul 2>&1')
    os.system(route_r6s_vcsp7 + '>nul 2>&1')
    os.system(route_r6s_vcsp8 + '>nul 2>&1')
    os.system(route_r6s_vcsp10 + '>nul 2>&1')
    os.system(route_r6s_vcsp11 + '>nul 2>&1 ')
    os.system(route_r6s_vcsp12 + '>nul 2>&1')
    os.system(route_r6s_vcsp13 + '>nul 2>&1')
    os.system(route_r6s_vcsp14 + '>nul 2>&1')
    os.system(route_r6s_vcsp15 + '>nul 2>&1')
    os.system(route_r6s_vcsp16 + '>nul 2>&1')
    os.system(route_r6s_vcxb + '>nul 2>&1')
    os.system(route_r6s_vcxb1 + '>nul 2>&1')
    os.system(route_r6s_vcxb2 + '>nul 2>&1')
    os.system(route_r6s_vcxb3 + '>nul 2>&1')
    os.system(route_r6s_vcxb4 + '>nul 2>&1')
    os.system(route_r6s_vcxb5 + '>nul 2>&1')
    os.system(route_r6s_vcxb6 + '>nul 2>&1')
    os.system(route_r6s_vcxb7 + '>nul 2>&1')
def routing_pubg():
    os.system(route_pubgx + '>nul 2>&1')
def routing_fortnite():
    os.system(route_fn + '>nul 2>&1')
    os.system(route_fn2 + '>nul 2>&1')
    os.system(route_fn3 + '>nul 2>&1')
    os.system(route_fn4 + '>nul 2>&1')
    os.system(route_fn5 + '>nul 2>&1')
    os.system(route_fn6 + '>nul 2>&1')
    os.system(route_fn7 + '>nul 2>&1')
    os.system(route_fn8 + '>nul 2>&1')
    os.system(route_fn9 + '>nul 2>&1')
    os.system(route_fn10 + '>nul 2>&1')
    os.system(route_fn11 + '>nul 2>&1')
    os.system(route_fn12 + '>nul 2>&1 ')
    os.system(route_fn13 + '>nul 2>&1')
def routing_h1z1():
    os.system(route_h1z1 + '>nul 2>&1')
    os.system(route_h1z12 + '>nul 2>&1')
    os.system(route_h1z13 + '>nul 2>&1')
    os.system(route_h1z14 + '>nul 2>&1')
    os.system(route_h1z15 + '>nul 2>&1')
    os.system(route_h1z16 + '>nul 2>&1')
def dns_setup():
    os.system('netsh interface ip set dns name="Ethernet 2" source=static addr=none >nul 2>&1')
    os.system('netsh interface ip add dns name="Ethernet 2" addr=8.8.8.8 index=1 >nul 2>&1')
    os.system('netsh interface ip add dns name="Ethernet 2" addr=8.8.4.4 index=2 >nul 2>&1')
    os.system('netsh interface ip set dns name="Ethernet 1" source=static addr=none >nul 2>&1')
    os.system('netsh interface ip add dns name="Ethernet 1" addr=8.8.8.8 index=1 >nul 2>&1')
    os.system('netsh interface ip add dns name="Ethernet 1" addr=8.8.4.4 index=2  >nul 2>&1')
    os.system('netsh interface ip set dns name="Ethernet" source=static addr=none >nul 2>&1')
    os.system('netsh interface ip add dns name="Ethernet" addr=8.8.8.8 index=1 >nul 2>&1')
    os.system('netsh interface ip add dns name="Ethernet" addr=8.8.4.4 index=2 >nul 2>&1')
    os.system('netsh interface ip set dns name="Wi-Fi" source=static addr=none >nul 2>&1')
    os.system('netsh interface ip add dns name="Wi-Fi" addr=8.8.8.8 index=1 >nul 2>&1')
    os.system('netsh interface ip add dns name="Wi-Fi" addr=8.8.4.4 index=2 >nul 2>&1')
    os.system('netsh interface ip set dns name="Local Area Connection" source=static addr=none >nul 2>&1')
    os.system('netsh interface ip add dns name="Local Area Connection" addr=8.8.8.8 index=1 >nul 2>&1')
    os.system('netsh interface ip add dns name="Local Area Connection" addr=8.8.4.4 index=2 >nul 2>&1')
    os.system('netsh interface ip set dns name="Wireless Network Connection" source=static addr=none >nul 2>&1')
    os.system('netsh interface ip add dns name="Wireless Network Connection" addr=8.8.8.8 index=1 >nul 2>&1')
    os.system('netsh interface ip add dns name="Wireless Network Connection" addr=8.8.4.4 index=2 >nul 2>&1')
    os.system('netsh interface ip set dns name="Wi-Fi" source=static addr=none >nul 2>&1')
    os.system('netsh interface ip add dns name="Wi-Fi" addr=8.8.8.8 index=1 >nul 2>&1')
    os.system('netsh interface ip add dns name="Wi-Fi" addr=8.8.4.4 index=2 >nul 2>&1')
