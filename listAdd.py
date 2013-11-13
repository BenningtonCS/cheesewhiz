import os
import sys 
import whizconfig

del sys.argv[0]
options = ""

def getList(listToGet):
	newList = []
	with open(whizconfig.path+listToGet,"r") as whizFile:
		for line in whizFile:
			newList.append(line.strip("\n"))
		return newList

for item in sys.argv:
	if item[0] == "-":
		sys.argv.remove(item)
		options += item


if "r" in options and "k" in options:
	print "You need to choose whether to 'run' or 'kill'."
	exit(0)


for process in sys.argv:
	sys.argv[sys.argv.index(process)] = whizconfig.path + sys.argv[sys.argv.index(process)]
print "sys.argv : ", sys.argv

toRun = []
toKill = []
toRun += getList("whizzifest.txt")
toKill += getList("hitlist.txt")


if "r" in options:
	for process in sys.argv:
		if process in toKill:
			toKill.remove(process)
		if process not in toRun:
			toRun.append(process)

elif "k" in options:
	for process in sys.argv:
		if process in toRun:
			toRun.remove(process)
		if process not in toKill:
			toKill.append(process)

with open(whizconfig.path+"whizzifest.txt", "w") as whiz:
	for item in toRun:
		whiz.write(item+"\n")

with open(whizconfig.path+"hitlist.txt","w") as hit:
	for item in toKill:
		hit.write(item+"\n")



