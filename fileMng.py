#File manager
import os.path
import shutil
import urllib.request
import urllib.error
from UrlLL import UrlList

#File paths
ListPath = "url.list"
DLPath = "hlist/"
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
        if not os.path.exists(DLPath):
            os.makedirs(DLPath)
        DLDest = DLPath + "hosts.id"+str(IdNum)
        print(link)
        print(DLDest)
        print("Downloading")
        try:
            urllib.request.urlretrieve(link, DLDest)
            print("Done")
        except:
            print("Broke yo")

def hImport(IdNum):
    try:
        IdNum = int(IdNum)
    except ValueError:
        print("Invalid ID input")
        return
    HFPath = DLPath + "hosts.id" + str(IdNum)
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
