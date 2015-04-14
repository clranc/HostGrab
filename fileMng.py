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
TmpPathA = "hosts.tmpA"
TmpPathB = "hosts.tmpB"
InstPath = "/etc/hosts"

def dl(IdNum):
    count = 1
    try:
        IdNum = int(IdNum)
    except ValueError:
        print("Invalid ID input")
        return

    if os.path.isfile(ListPath) == False:
        UrlFile = open(ListPath,"w")
        print("List is empty")
        return
    else:
        UrlFile = open(ListPath,"r")
        List = UrlList()
        for line in UrlFile:
            entry = line.strip().split()
            if len(entry) != 0:
                List.add(entry[0])
        link= List.search(IdNum)
        if not os.path.exists(HostPath):
            os.makedirs(HostPath)
        DLDest = DLPath + str(IdNum)
        print(link)
        print(DLDest)
        print("Downloading")
        try:
            urllib.request.urlretrieve(link, DLDest)
            print("Done")
        except:
            print("Broke yo")
            return
        scan(IdNum)

def hImport(IdNum):
    try:
        IdNum = int(IdNum)
    except ValueError:
        print("Invalid ID input")
        return
    HFPath = DLPath + str(IdNum)
    if os.path.isfile(HFPath) == False:
        print("File doesn't exist")
    else:
        shutil.copy2(IpListPath,TmpPathA)
    IpFile = open(HFPath,"r")
    TmpFile = open(TmpPathA,"a")
    TmpFile.write("#HostGrab IP & Domain inclusions\n\n")

    for line in IpFile:
        TmpFile.write(line)
    
    shutil.move(TmpPathA,InstPath)

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
