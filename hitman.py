				 ######################################################
				# 	hitman.py 				     #
			       #       Torrent Glenn                 		    #
			      #        11/13/2013				   #
			     #	       CheeseWhiz revamped                        #
			    ######################################################
				
""" The hitman is exactly what the cheesewhiz family has been lacking all this time. Now the hitman
(essentially the opposite of cheesewhiz) simply kills all the processes you want dead. Another addition, listAdd.py 
is the new interface for managing the cheesewhiz family"""

import os, psutil

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


#Open the hitlist, get all the lines, and put them in a list
with open('hitlist.txt') as w:
        content = w.readlines()

# make a new list wherein all the newline characters have been stripped
programs = [elem.strip("\n") for elem in content]



# runs the unix script to output the results of ps-ef into ps.txt
#os.system("top -n 1 -b > top.txt")
names = []

# create an empty list to be populated with the results of parsing ps.txt
tst = psutil.get_pid_list()
for item in tst:
	p = psutil.Process(item)
	names.append(p.cmdline)
	
IDs = []

for i in range(len(tst)):
	IDs.append(tst[i],names[i])


# create an empty string to be populated by the subset of all processes which are running 
#that we want to kill
running = ""

# get the PIDs of the programs to kill and append them to IDs.txt
for item in programs:
	for thing in IDs:
		if item in thing[1]:
			psutil.Process(thing[0]).kill()
	
# the list of programs we want dead
#toKill = []



#get the intersection of processes that are running and processes we want to kill
#for item in toKill:
      #  if item in tst:
           #     running += " " + item


# kill the programs in the aforementioned intersection: programs we want to kill that
# are running
#os.system("kill -9 " + running)
#remove IDs.txt
#os.system("rm IDs.txt psh.txt")

