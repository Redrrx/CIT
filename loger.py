import logging
from datetime import datetime
import requests
import time
from requests import get
import socket
from bs4 import BeautifulSoup
i = datetime.now()
IP = socket.gethostbyname(socket.gethostname())
vivox_ms=socket.gethostbyname('mpx5j.vivox.com')
r6s_vcs=socket.gethostbyname('disp-rbswp-5-1.vivox.com')
fn_vcs=socket.gethostbyname('disp-fnwp-5-1.vivox.com')



# This is just some dumb logging
# will improve in the future for more hardware/permission check incase Routing is not done proprely

#vpn disconnects due inactivity this is a temporary workaround will change in future version
def signal():
    response = requests.get('https://api.ipify.org', timeout=180)
    soup = BeautifulSoup(response.text, 'html.parser')
    print('Sending signal to vpn server every 60 seconds, current ip is: ' + soup.prettify() + "Response code: "+ str(response.status_code) + " " + time.ctime())
    time.sleep(60)

def net_stuff():

    level = logging.INFO
    format = '  %(message)s'
    handlers = [logging.FileHandler('log.txt'), logging.StreamHandler()]
    logging.basicConfig(level=level, format=format, handlers=handlers)
    logging.info("----------------------------------------------------------------------------")
    logging.info(i.strftime('%Y/%m/%d %H:%M'))
    logging.info("VVX MASTER SERVER IP IS:")
    logging.info(vivox_ms)
    logging.info("VVX R6S MASTER SERVER IP IS:")
    logging.info(r6s_vcs)
    logging.info("VVX FN MASTER SERVER IP IS:")
    logging.info(fn_vcs)


def run_log():
    net_stuff()
    time.sleep(3)
    while True:
        signal()
