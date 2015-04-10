#URL linked list object
class Node(object):
     def __init__(self, url, next=None):
         self.url = url
         self.next = next

class UrlList(object):
     def __init__(self):
         self.head = None 
         self.tail = None
     
     def isEmpty(self):
         if self.head == None:
             return True
         else:
             return False

     def add(self, url):
         NewNode = Node(url)
         if self.head == None:
            self.head = NewNode
            self.tail = self.head
         else:
             self.tail.next = NewNode
             self.tail = NewNode

     def rm(self, num):
         TravNode = self.head
         PrevNode = TravNode
         count = 1
         if num == 1:
             #resets head node if the id is the first
             self.head = self.head.next
             #resets tail node
             if self.head.next == None
                 self.tail = self.head
             return
         while TravNode != None:
             if count == num:
                 PrevNode.next = TravNode.next
                 if PrevNode.next == None:
                     self.tail = PrevNode 
                 return

             else:
                  PrevNode = TravNode
                  TravNode = TravNode.next
                  count = count + 1

     def fWrite(self, UrlFile):
         TravNode = self.head
         while TravNode != None:
              String = TravNode.url
              String = String + "\n"
              UrlFile.write(String)
              TravNode = TravNode.next

     def printList(self): 
         TravNode = self.head
         count = 1
         print("ID\tDownload URL")
         print("--\t------------")
         while TravNode != None:
              String = TravNode.url
              print(str(count) + ")\t" +String.strip("\n"))
              count += 1
              TravNode = TravNode.next
