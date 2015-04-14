#Ip and Domain linked list object
class Node(object):
     def __init__(self, ip, domain, next=None):
         self.ip = ip
         self.domain = domain
         self.next = next

class IpDmList(object):
     def __init__(self):
         self.head = None 
         self.tail = None

     def isEmpty(self):
         if self.head == None:
             return True
         else:
             return False

     def add(self, ip, domain):
         NewNode = Node(ip, domain)
         if self.head == None:
            self.head = NewNode
            self.tail = self.head
            return
         else:
             self.tail.next = NewNode
             self.tail = NewNode

     def rm(self, IdNum):
         TravNode = self.head
         PrevNode = TravNode
         count = 1

         if IdNum == 1:
             self.head = self.head.next
             if (self.head == None) or (self.head.next == None):
                 self.tail = self.head
             return
         while TravNode != None:
             if count == IdNum:
                  PrevNode.next = TravNode.next
                  if PrevNode.next == None:
                     self.tail = PrevNode
                  return

             else:
                  PrevNode = TravNode
                  TravNode = TravNode.next
                  count = count + 1

     def fWrite(self, IpDomainFile):
         TravNode = self.head
         while TravNode != None:
              TabString = self.tabCount(TravNode.ip)
              String = TravNode.ip + TabString + TravNode.domain +"\n"
              IpDomainFile.write(String)
              TravNode = TravNode.next

     def tabCount(self, IpString):
         length = len(IpString)
         count = 0
         if length <= 8:
            count = 6
         elif length > 8 and length <= 16:
            count = 5
         elif length > 16 and length <= 24:
            count = 4
         elif length > 24 and length <= 32:
            count = 3
         else:
            count = 2
         TabString = ""
         while count != 0:
            TabString = TabString + "\t"
            count = count - 1

         return str(TabString)

     def printList(self): 
         TravNode = self.head
         count = 1
         print("ID\tIP Address\t\t\t\t\tDomain Name")
         print("--\t----------\t\t\t\t\t-----------")
         while TravNode != None:
              TabString = self.tabCount(str(TravNode.ip))
              print(str(count) + ")\t" + TravNode.ip + TabString + TravNode.domain.strip("\n"))
              count = count + 1
              TravNode = TravNode.next
