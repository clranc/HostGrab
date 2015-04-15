#File manager
import ipExcp
import os.path
import re
import shutil
import urllib.request
import urllib.error
from UrlLL import UrlList

#File paths
ListPath = "url.list"
HostPath = "hlist/"
DLPath = "hlist/hosts.id"
IpListPath = "ip.list"
InstPath = "/etc/hosts"
#Temporary Files
TmpPathA = "hosts.tmpA"
TmpPathB = "hosts.tmpB"

#Download Function
def dl(IdNum):
   
    #Id Check 
    try:
        IdNum = int(IdNum)
    except ValueError:
        print("Invalid ID input")
        return
    
    #Checks if url.list exists and creates it if it doesn't
    if os.path.isfile(ListPath) == False:
        UrlFile = open(ListPath,"w")
        print("List is empty")
        return

    else:
        UrlFile = open(ListPath,"r")
        #Creates Linkd List Object for filtering thorugh download
        #URL's 
        List = UrlList()
        for line in UrlFile:
            entry = line.strip().split()
            if len(entry) != 0:
                List.add(entry[0])

        #Pulls URL from list
        link= List.search(IdNum)

        #If the Download Directory doesn't exist it is created
        if not os.path.exists(HostPath):
            os.makedirs(HostPath)

        #Sets file path and name for host file being downloaded
        DLDest = DLPath + str(IdNum)

        #Message to show that the download is in progress
        print("Downloading from " + link)

        #Try catch is used for downloading the file to the specified
	#directory
        try:
            urllib.request.urlretrieve(link, DLDest)
            print("Done")

        #If interrupted a failure message is printed and returns
        except:
            print("The download was interrupted")
            return

        #If the download passes the file is scanned to check for 
        #improper or suspicious IPs
        scan(IdNum)

#Import Function for creating and importing the host file to the 
#root directory
def hImport(IdNum):

    #Checks if ID number entered is a valid integer
    try:
        IdNum = int(IdNum)

    #If the the entered value isn't an integer an error message 
    #is printed and the function returns 
    except ValueError:
        print("Invalid ID input")
        return

    #Creates the path for the new host file to be created
    HFPath = DLPath + str(IdNum)
    
    #File path is checked to see if it exists.
    #If it doesn't the an error message is printed 
    if os.path.isfile(HFPath) == False:
        print("File doesn't exist")
        return

    #ip.list is copied to act as
    shutil.copy2(IpListPath,TmpPathA)
    
    #File for host file being read
    IpFile = open(HFPath,"r")
    #
    TmpFile = open(TmpPathA,"a")
    TmpFile.write("#HostGrab IP & Domain inclusions\n\n")

    print("Importing....")

    for line in IpFile:
        TmpFile.write(line)

    try:
        shutil.move(TmpPathA,InstPath)
        print("Import was successful")
    except:
        print("Import failed")
    
def nullSwap():
    if os.path.isfile(TmpPathA) == False:
        TmpFile = open(TmpPathA,"w")
        TmpFile.write("127.0.0.1\t\tlocalhost\n")
        TmpFile.write("::1\t\t\tlocalhost\n")
        TmpFile.close()

    shutil.copy2(InstPath,TmpPathB)
    shutil.move(TmpPathA,InstPath)
    os.rename(TmpPathB,TmpPathA)

def scan(IdNum):
    ApprovedIps = (r"(127.0.0.1)|(0.0.0.0)|(^::1$)|(^::$)")
    File = open(DLPath + str(IdNum),"r")

    BadIpLog = open(HostPath + "BadIpLog.id"+str(IdNum) ,"w")
    BadIpLog.write("#Bad Ip list\n\n")

    SketchLog = open(HostPath +"SketchIpLog.id" + str(IdNum),"w")
    SketchLog.write("#Sketchy Ip list\n\n")

    BadIpCount = 0
    SketchCount = 0
    LineCount = 0

    try:
        IdNum = int(IdNum)
    except ValueError:

        print("Invalid ID input")
        return
    
    print("\nScanning File...")    

    for line in File:
        possible = line.strip().split()
        LineCount += 1
        if not  line.strip().startswith("#") and len(possible)!=0:
            if ipExcp.ipChk(possible[0]) == False:
               BadIpLog.write("Line "+str(LineCount)+": "+possible[0]+ "\n")
               BadIpCount += 1

            if re.search(ApprovedIps, possible[0]) is None:
               SketchLog.write("Line "+str(LineCount)+": "+possible[0]+"\n")
               SketchCount += 1
    
    print("Finished")

    BadIpLog.write("\n\n**Total bad IPs : " + str(BadIpCount))
    SketchLog.write("\n\n**Total sketchy IPs : " +str(SketchCount))

    if SketchCount != 0:
        os.rename(DLPath + str(IdNum), DLPath + str(IdNum) + ".bad")
        print("This host file was found to be suspicious and was renamed"
           +"\nto prevent use. It is advisable to remove this host file and"
           +"\nit's  url.\n")

    elif BadIpCount != 0:
        print("This host file has improper ip addresses in it. This doesn't"
           +"\nprevent The file from being usable but it's advisable to "
           +"\nremove this host file and replace it with a better one.\n")

    else:
        print("No suspicious or bad IPs were found so this file is"
             +" good to import to root\n")

    print(str(SketchCount) + " Suspicous IPs were found and logged "
                                           +"to SketchLog.id"+str(IdNum))
    print(str(BadIpCount) + " Bad IPs were found and logged to "
                                            +" BadIpLog.id" + str(IdNum))
    print("\nLog file path:\n" + os.path.abspath(HostPath))
