import os

def rmSpace(spaceList):
	if '' in spaceList:
		spaceList.remove('')
		rmSpace(spaceList)
	else: 
		return spaceList

# open the whizzifest.txt file that has been manually generated. This 
# puts the file into a list named content, each line being its own item.
os.system("rm IDs.txt")
with open('hitlist.txt') as w:
        content = w.readlines()

# take each element from the list 'content' and split it where the 
# character '|' appears. This is part of a new list called 'programs'. 
# Each item in the list is a list of two items. [x][0] is the location 
# of the file and [x][1] is the name of the program.
programs = [elem.strip("\n") for elem in content]



# runs the unix script to output the results of top into top.txt
#os.system("top -n 1 -b > top.txt")
os.system("ps -ef > ps.txt")

# create an empty list to be populated with the results of parsing top.txt
tst = []

# from top.txt, parse each line to get the name of the process and append it to the e$
with open('ps.txt', 'r') as input:
        for line in input:
                newline = line.split(' ')
		rmSpace(newline)
                tst.append(newline[1].strip())

# create an empty list to be populated by the subset of all processes which are not r$
running = ""

# check to see if the processes from the input match the processes running. Output th$
for item in programs:
	os.system("ps -ef | grep "+ item +" >> IDs.txt")

toKill = []

with open ("IDs.txt","r") as input:
	for line in input:
		newline = line.split(" ")
		rmSpace(newline)
		toKill.append(newline[1].strip())
print toKill

for item in toKill:

        if item in tst:
                running += " " + item









# run script that initiates programs that are not running, but should be
print "these are running: ", running
os.system("kill -9 " + running)

