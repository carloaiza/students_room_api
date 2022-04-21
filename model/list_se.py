from .pet import Pet
from.node import Node

class ListSE:
    def __init__(self):
        self.head = None
        self.count= 0

    def add(self,pet:Pet):
        if self.head == None:
            self.head= Node(pet)
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            #Ubicado en el último
            temp.next = Node(pet)
        self.count=+1


    def add_to_start(self,pet:Pet):
        if self.head == None:
            self.head = Node(pet)
        else:
            temp = Node(pet)
            temp.next= self.head
            self.head = temp
        self.count=+1

    def add_to_position(self,position:int, pet:Pet):
        if position >0 and position <= (self.count+1):
            if position == 1:
                new_node = Node(pet)
                new_node.next = self.head
                self.head = new_node
            else:
                temp = self.head
                count = 1
                while temp !=None:
                    if count == position -1:
                        new_node = Node(pet)
                        new_node.next = temp.next
                        temp.next = new_node
                        self.count =+1
                        break
                    temp = temp.next
                    count =+1

            self.count=+1
        else:
            raise Exception("La posición no es válida")


    def invert(self):
        if self.head != None:
            list_cp = ListSE()
            temp = self.head
            while temp != None:
                list_cp.add_to_start(temp.data)
                temp = temp.next
            self.head = list_cp.head

