import os,socket,threading, sys
import restartConfig as rConfig

PORT = rConfig.port 
ADDRESS = "" 
refreshList = []

def rmSpace(spaceList):
        #Later in the code when the information returned by ps-ef
        #needs to be parsed this function removed the empty strings
        #in the list in order to make it easier to retrieve 
        #information via indexes
        #rmSpace() recursively removes the first empty string in the 
        #given list until there are no more empty strings
        if '' in spaceList:
                spaceList.remove('')
                rmSpace(spaceList) 
        else: 
                return spaceList

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind((ADDRESS,PORT))

while 1:
	s.listen(1)
	conn, addr = s.accept()
	toRestart = s.recv(2048).split("|")

	os.system("ps -ef > processes.txt")

	tList = []

	with open('processes.txt', 'r') as input:
        for line in input:
                newline = line.split(' ')
                tList.append(newline[1].strip())

    for item in toRestart:
        os.system("ps -ef | grep "+ item +" >> PIDs.txt")

    restartable = ""

    with open ("PIDs.txt","r") as input:
        for line in input:
                newline = line.split(" ")
                rmSpace(newline)
                refreshList.append(newline[1].strip())

    for item in refreshList:
        if item in tList:
                restartable += " " + item

    os.system("kill " + running)
    os.system("rm processes.txt PIDs.txt")
    os.system("python "+ restartable)

