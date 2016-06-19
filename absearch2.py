import os,time



def search(name,flag):
	
	if(os.path.exists(name)):
		if((flag==1) & os.path.isfile(name)==True):
			print "FILE:  ","\t\t\t",os.path.abspath(""),"\t",time.ctime(os.path.getmtime(name)),"\t",time.ctime(os.path.getctime(name))

		elif((flag==2) & os.path.isdir(name)==True):
			print "FOLDER:","\t\t\t",os.path.abspath(""),"\t",time.ctime(os.path.getmtime(name)),"\t",time.ctime(os.path.getctime(name))

		elif(flag==3):
			f=os.path.isfile(name)
			if(os.path.isfile(name)):
				print "FILE:  ","\t\t\t",os.path.abspath(""),"\t",time.ctime(os.path.getmtime(name)),"\t",time.ctime(os.path.getctime(name))

			elif(os.path.isdir(name)):
				print "FOLDER:","\t\t\t",os.path.abspath(""),"\t",time.ctime(os.path.getmtime(name)),"\t",time.ctime(os.path.getctime(name))

	list=os.listdir(".")
	for i in list:
		if(os.path.isdir(i)==True):
			os.chdir(i)
			search(name,flag)
			os.chdir("..")
def psearch(name,flag):
	list=os.listdir(".")
	for i in list:
		if((i.find(name)!=-1) & (i!=name)):
			if(os.path.isfile(i) & flag==1):
				print "FILE:  ",i,"\t\t",os.path.abspath(""),"\t",time.ctime(os.path.getmtime(i)),"\t",time.ctime(os.path.getctime(i))

			elif(os.path.isdir(i) & flag==2):
				print "FOLDER:",i,"\t\t",os.path.abspath(""),"\t",time.ctime(os.path.getmtime(i)),"\t",time.ctime(os.path.getctime(i))
			elif(flag==3):
				if(os.path.isfile(i)):
					print "FILE:  ",i,"\t\t",os.path.abspath(""),"\t",time.ctime(os.path.getmtime(i)),"\t",time.ctime(os.path.getctime(i))

				elif(os.path.isdir(i)):
					print "FOLDER:",i,"\t\t",os.path.abspath(""),"\t",time.ctime(os.path.getmtime(i)),"\t",time.ctime(os.path.getctime(i))

		if(os.path.isdir(i)==True):
			os.chdir(i)
			psearch(name,flag)
			os.chdir("..")

def main():
	clear = lambda: os.system('clear')
	clear()
	print "\n****************************************************AB SEARCH 1.1*****************************************************\n"
	print "What do you want to search for?"
	print "\t1.File"
	print "\t2.Directory"
	print "\t3.Both"
	flag=input("Enter 1, 2 or 3: ")

	if(flag==1):
		name=raw_input("Enter the name of file: ")
	elif(flag==2):
		name=raw_input("Enter the name of directory: ")
	elif(flag==3):
		name=raw_input("Enter the name: ")
	else:
		exit(0)

	print "\nSearching for exact matches...\n"
	print "TYPE  ","\t\t\t\t","LOCATION","\t\t\t","MODIFIED","\t\t\t","CREATED"
	print"---------------------------------------------------------------------------------------------------------------------------"
	search(name,flag)

	print "\nSearching for similar names...\n"
	print "TYPE   ","NAME","\t\t\t","LOCATION","\t\t\t","MODIFIED","\t\t\t","CREATED"
	print"---------------------------------------------------------------------------------------------------------------------------"
	psearch(name,flag)

	print "\n**********************************************************************************************************************\n"

if __name__ == "__main__": main()
