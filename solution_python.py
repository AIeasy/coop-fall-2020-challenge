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
        self.commandlist=[]
        self.node = 0;

    def add(self, num: int):
        self.value +=num;
        self.commandlist.append(num)
        self.node=len(self.commandlist)
        pass

    def subtract(self, num: int):
        self.value-=num;
        self.commandlist.append(-num)
        self.node=len(self.commandlist)
        pass

    def undo(self):
        self.value-=self.commandlist[len(self.commandlist)]
        self.node-=1
        pass

    def redo(self):
        self.value+=self.commandlist[self.node+1];
        pass

    def bulk_undo(self, steps: int):
        i=0
        while i<steps :
            self.value-=self.commandlist[self.node]
            self.node-=1
            i+=1
            
        pass

    def bulk_redo(self, steps: int):
        j=0
        while j<steps:
            self.value+=self.commandlist[self.node];
            self.node+=1
            j+=1

        pass
