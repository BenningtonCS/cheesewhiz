import os,socket,threading, sys, psutil
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
        toRestart = s.recv(2048).split"|")

        pList = psutil.get_pid_list()
        nList = []
        toKill = []
        toRun = ""

        for process in pList:
                nlist.append(psutil.Process(process).cmdline[-1])

        for item in toRestart:
                for name in nList:
                        if item in name[0]
                        toKill.append(pList[nList.index(name)])

        for item in toRestart:
                toRun += " " + item

        os.system("kill" + toKill)
        os.system("python "+ toRun)
