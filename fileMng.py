#File manager
import os.path
import urllib.request
from UrlLL import UrlList

ListPath = "url.list"
DLPath = "hlist/"
InstPath = "/etc/"

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
        urllib.request.urlretrieve(link, DLDest)
        print("Done")
