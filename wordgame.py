class Node:

   def __init__(self, data=None, next=None):
      self.data = data
      self.next = next


class LinkedList:
   def __init__(self):
      self.head = None

   def insert(self, data):
      newNode = Node(data)
      if (self.head):
         current = self.head
         while (current.next):
            current = current.next
         current.next = newNode
      else:
         self.head = newNode

   def del_ll(self):
      if (self.head != None):
         self.head = None

   def printLL(self):
      current = self.head
      while (current):
         print(current.data,end='')
         current = current.next
   def check_ll(self,lis2):
      current = self.head
      i=0
      while (current):
         if current.data==lis2[i]:
            current = current.next
            i+=1
      if i==len(lis2):
         return True


ll = LinkedList()
lis=['obse_sive','as_ound','euphonio_s','sau_ter','supi_e','pluv_ophile','co_undrum','ea_arville']
lis2=['s','t','u','n','n','i','n','g']
print("__________________________________KNOCK YOUR KNOWLEDGE____________________________________")
while(1):
   choice=int(input('1.START 2.EXIT '))

   if choice==1:
      ll.del_ll()

      for i in range(len(lis)):
         print(lis[i])
         data=input('enter the missing letter ')
         data=data.lower()

         if lis2[i]==data:
            ll.insert(data)
         else:
            print('xxx____MISMATCHING LETTER____xxx')
            flag=1
            if flag==1:
               break
   else:
      break




