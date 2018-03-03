import socket
from threading import Thread
class socks:
	counter = 0
	def __init__(self):
		self.sockdb = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	def cc(self):
		self.counter += 1
	def send(self, data, ip, port):
		th = Thread(target=self.cc, name='horse')
		th.start()
		th.join()
		try:
			th = Thread(target=self.sockdb.sendto, args=(data.encode('utf-8'), (ip, port)))
			th.start()
			th.join()
		except:
			return False
		else:
			return True
	def gethostip(self, hostname):
		return socket.gethostbyname(hostname)
	def __del__(self):
		self.sockdb.close()