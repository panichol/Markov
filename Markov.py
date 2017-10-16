import random

class MarkovMap:    
    def __init__(self,source, order = 3):
        self.source = source
        self.order = order
        self.map = {}
        self.BuildMap()
        return

    ## The easiest way to do this is just bring the entire text document into memory
    ## In future, if this is a bottleneck, should be able to reformat
    ## to do this on a line-by-line basis
    ## It ain't pretty, but it works
    def BuildMap(self):
        text = []
        ## Read in book
        with open(self.source,'r') as infile:
            for line in infile:
                text.append(" %s "%(line.strip()))
        ## Create list like string for easy mapping
        text = list("".join(text))
        text.append(text[:self.order])
        ## Populate our map
        for i in range(len(text)-self.order):
            key = text[i:i+self.order]
            if "".join(key) in self.map:
                self.map["".join(key)].append(text[(i+self.order)])
            else:
                self.map["".join(key)] = [text[(i+self.order)]]
        self.startPositions = (x for x in self.map)

    ## Possibly replace this with a __next__ incantation?    
    def GetNext(self,key):
        randint = random.randint(0,len(self.map[key])-1)
        
        return self.map[key][randint]

    def Generate(self,number = 1000, start = ""):
        ret = []
        if not start:
            start = next(self.startPositions)
        key = start
        for i in range(number):
            newChar = self.GetNext("".join(key))
            key = "".join(key[1:]+newChar)
            ret.append(newChar)
        return "".join(ret)
