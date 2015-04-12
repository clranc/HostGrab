#Url linked list handler
import os.path
from UrlLL import UrlList

Path = "url.list"
DLPath = "hlist/"
def add(Url):
    if os.path.isfile(Path) == False:
        UrlFile = open(Path,"w")
        List = UrlList()
        List.add(Url)
        List.fWrite(UrlFile)
        List.printList()
        return
    else:
        UrlFile = open(Path,"r")
        List = UrlList()
        for line in UrlFile:
            entry = line.strip().split()
            if len(entry) != 0:
                if Url == entry[0]:
                    print("This download url is already in use and will "+
                          "not be added")
                    return
                List.add(entry[0])
        List.add(Url)
        UrlFile = open(Path,"w")
        List.fWrite(UrlFile)
        List.printList()
        return
def rm(NumId):
    try:
        NumId = int(NumId)
    except ValueError:
        print("Invalid ID input")
        return

    if os.path.isfile(Path) == False:
        UrlFile = open(Path,"w")
        print("Your url list is empty")
        return

    else:
        UrlFile = open(Path,"r")
        List = UrlList()
        for line in UrlFile:
            if len(line.strip().split())!=0:
              List.add((line.strip().split())[0])

        if List.isEmpty() == True:
             print("The IP & Domain list is empty")
             return
        DLFPath = DLPath + "hosts.id" + str(NumId)
        if os.path.isfile(DLFPath) == True:
            os.remove(DLFPath) 
        List.rm(NumId)
        UrlFile = open(Path,"w")
        List.fWrite(UrlFile)
        List.printList()
        return

def printList():
    List = None
    if os.path.isfile(Path) == False:
        UrlFile = open(Path,"w")
        List = UrlList()
        List.printList()
        return
    else:
        UrlFile = open(Path,"r")
        List = UrlList()
        for line in UrlFile:
            if len(line.strip().split())!=0:
                List.add((line.strip().split())[0])
        List.printList()
      
