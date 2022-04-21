from model.list_se import ListSE
from model.node import Node
from model.pet import Pet

class ListSeService:
    def __init__(self):
        self.list = ListSE()

    def get_all_linked(self):
        return self.list.head

    def invert(self):
        if self.list.head == None:
            return {"message":"La lista está vacía"}
        else:
            self.list.invert()
            return {"message": "Se ha invertido la lista"}


    def add(self,dict):
        self.list.add(Pet(dict))
        return {"message":"Adicionado con éxito"}

    def add_to_start(self,dict):
        self.list.add_to_start(Pet(dict))
        return {"message":"Adicionado con éxito"}

    def add_to_position(self,position,dict):
        try:
            self.list.add_to_position(position,Pet(dict))
            return {"message":"Adicionado con éxito"}
        except Exception as e:
            return {"message": str(e)}