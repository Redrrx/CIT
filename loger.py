import logging
from datetime import datetime
from requests import get
import socket
i = datetime.now()
IP = socket.gethostbyname(socket.gethostname())
vivox_ms=socket.gethostbyname('mpx5j.vivox.com')
r6s_vcs=socket.gethostbyname('disp-rbswp-5-1.vivox.com')
# This is just some dumb logging
# will improve in the future for more hardware/permission check incase Routing is not done proprely

def net_stuff():

    level = logging.INFO
    format = '  %(message)s'
    handlers = [logging.FileHandler('log.log'), logging.StreamHandler()]
    logging.basicConfig(level=level, format=format, handlers=handlers)
    logging.info("----------------------------------------------------------------------------")
    logging.info(i.strftime('%Y/%m/%d %H:%M'))
    logging.info("VVX MASTER SERVER IP IS:")
    logging.info(vivox_ms)
    logging.info("VVX R6S MASTER SERVER IP IS:")
    logging.info(r6s_vcs)
    public_ip = get('https://api.ipify.org').text
    logging.info("IP AFTER VPN CONNECTION IS:")
    logging.info(public_ip)
    logging.info("----------------------------------------------------------------------------")
def run_log():
    net_stuff()
    logging.shutdown()