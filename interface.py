import sys
import os
import url
import ipExcp
import fileMng

if (os.getuid() != 0):
    print("You need SU access to use HostGrab")

elif (len(sys.argv)) == 1:
    print("welcome to hostgrab") 
#url command set
elif sys.argv[1] == "url":
    #add url to download list
    if sys.argv[2] == "add":
        url.add(sys.argv[3])
    #rm url and file
    elif sys.argv[2] == "rm":
        url.rm(sys.argv[3])
    #print url list
    elif sys.argv[2] == "print":
        url.printList()
    else:
        print("Enter proper argument")

#file command set
elif sys.argv[1] == "file":
    #download files that were added and then scan them
    if sys.argv[2] == "dl":
        fileMng.dl(sys.argv[3])
    elif sys.argv[1] == "import":
    #import host file based on its id
        if sys.argv[2] == "id":
           fileMng.hImport(sys.argv[3])  
    #import default host file 
        elif sys.argv[2] == "null":
            pass
        else:
            pass

    #A specific downloaded host file
    elif sys.argv[2] == "scan":
        pass
        #error message printed if the arguments are more then 4
        if len(sys.argv) > 4:
            print("Improper argument input")

        #Scans all files 
        elif sys.argv[3] == "all":
            pass
        #Scans a particular file
        #elif is_number(sys.argv[3]):

        #Prints error message
        else:
            print("Improper command input")
	
#ip exception command set
elif sys.argv[1] == "ipexc":
    #add menu for ip exceptions
    if sys.argv[2] == "add":
         #arg 3 is the ip to add and arg 4 is a correlating domain name
         ipExcp.add(sys.argv[3],sys.argv[4])
    #remove section for removing ip exceptions
    elif sys.argv[2] == "rm":
         #arg 3 is the id number from the list 
         ipExcp.rm(sys.argv[3])
    #print file list
    elif sys.argv[2] == "print":
         ipExcp.printList()
    else:
         print("improper arguments")
         pass
#prints help message discussing command functions
elif sys.argv[1] == "help":
    pass
else:
    print("Improper command input")
