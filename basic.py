class Numbers:
    lst = []

    def __init__(self, lst):
        self.lst=lst
    
    def __len__(self):
        return len(self.lst)
    
d1 = Numbers([1,2,3])

print(len(d1))
