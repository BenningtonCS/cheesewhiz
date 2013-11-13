import os,socket,threading, sys
import restartConfig as rConfig

lock = threading.lock()
toRestart = ""

for i in range(1,len(sys.argv)):
	if i > 1:
		toRestart += "|" + sys.argv[i]
	else:
		toRestart += sys.argv[i]

PORT = rConfig.port 
remoteHosts = rConfig.pis

class testThread(threading.Thread):
	daemon = True
	def __init__(self,port,remoteHost,lock):
		threading.Thread.__init__(self)
		self.port = port
		self.remoteHost = remoteAddr
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.lock = lock

	def run(self):
		self.socket.connect((remoteHost,PORT))
		self.socket.send(toRestart)
		ack = self.socket.recv(1024)
		if ack == "REFRESHED"
			self.lock.acquire()
			print "Processes successfully refreshed on "+self.remoteHost
			self.lock.release() 


