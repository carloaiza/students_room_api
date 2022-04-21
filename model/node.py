from .pet import Pet

class Node:
    def __init__(self,data:Pet):
        self.data = data
        self.next = None