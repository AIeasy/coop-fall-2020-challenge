"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Zhongxin Hu
ID:180896440
Email:  huxx6440@mylaurier.ca    
__updated__ =  "2020-07-10"
------------------------------------------------------------------------
"""
class EventSourcer():
    # Do not change the signature of any functions
   

    def __init__(self):
        self.value = 0
        self.redo_list=[]
        self.undo_list=[]

    def add(self, num: int):
        self.value +=num
        self.redo_list.append(num)
        pass

    def subtract(self, num: int):
        self.value-=num
        self.redo_list.append(-num)
        pass

    def undo(self):
        if len(self.undo_list)>0:
            value =self.undo_list.pop()
            self.value-=value
            self.undo_list.append(value)
        else:
            print("Can not undo when there is nothing to undo")
        pass

    def redo(self):
        if len(self.redo_list)>0:
            self.value+= self.redo_list.pop()
        else:
            
            print("Can not redo when there is nothing to redo")
        pass

    def bulk_undo(self, steps: int):
        
        while steps>0 :
            self.undo()
            steps-=1
        pass

    def bulk_redo(self, steps: int):
    
        while steps>0:
            self.redo()
            steps-=1

        pass
