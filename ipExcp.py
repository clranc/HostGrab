#IP and Domain linked list handler
import os.path
import ipaddress
import textwrap
from IpDmLL import IpDmList

#IP Validator
def ipChk(ip):
    try:
        ipaddress.ip_address(str(ip))
        return True
    except:
        return False

def add(ip, domain):
    Path = "ip.list"
    if ipChk(ip) == False:
        print(ip + " is not a standard ipv4/ipv6 address")
        return
    #creates ip.list file if it doesn't exist
    if os.path.isfile(Path) == False:
        IpFile = open(Path,"w")
        List = IpDmList()
        List.add(ip,domain)
        List.fWrite(IpFile)
        return
    #if the file exists begin reading the file
    else:
        IpFile = open(Path,"r")
        List = IpDmList()
        #loads linked list 
        for line in IpFile:
            entries = line.strip().split()
            if len(entries) != 0:
                if domain == entries[1]:
                    print("The domain "  + domain +
                         " is already in use and won't be added\n"+
                          "to the exception list")
                    return
                List.add(entries[0],entries[1])
        #adds new exception to the end of the list
        List.add(ip,domain)
        IpFile = open(Path,"w")
        List.fWrite(IpFile)
        List.printList()
        return

def rm(NumId):
    Path = "ip.list"
    if os.path.isfile(Path) == False:
         IpFile = open(Path,"w")
         return
    else:
         try:
             NumId = int(NumId)
         except ValueError:
               print("Invalid id input")
               return
         IpFile = open(Path,"r")
         List = IpDmList()
         for line in IpFile:
             entries = line.strip().split()
             if len(entries) != 0:
                 List.add(entries[0],entries[1])
         List.rm(NumId)
         IpFile = open(Path,"w")
         List.fWrite(IpFile)
         List.printList()
         return

def printList():
    Path = "ip.list"
    #Creates file if it doesn't exist
    if os.path.isfile(Path) == False:
        IpFile = open(Path,"w")
        List = IpDmList()
        List.printList()
        return
    else:
        IpFile = open(Path,"r")
        List = IpDmList()
        #loads list
        for line in IpFile:
            entries = line.strip().split()
            if len(line) != 0:
                List.add(entries[0],entries[1])
        List.printList()
