#Url linked list handler
import os.path
from UrlLL import UrlList

def add(Url):
    Path = "url.list"
    creates
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
            if len(line.strip().split())!=0:
                List.add((line.strip().split())[0])
        List.add(Url)
        UrlFile = open(Path,"w")
        List.fWrite(UrlFile)
        List.printList()
        return
    
def rm(NumId):
    Path = "url.list"
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
        List.rm(NumId)
        UrlFile = open(Path,"w")
        List.fWrite(UrlFile)
        List.printList()
        return

def printList():
    List = None
    Path = "url.list"
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
      
