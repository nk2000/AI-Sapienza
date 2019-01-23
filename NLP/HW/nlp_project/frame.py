import pprint

class Frame:
    """ Frames """
    def __init__(self, name, slots, values, questions):
        self.name = name
        self.slots = dict(zip(slots, [None] * len(slots)))
        self.possiblevalues = dict(zip(slots, values))
        self.questions = dict(zip(slots, questions))
        #self.readable = dict(zip(slots, readable))

    def name(self):
        return self.name

    def reset(self):
        for key in self.slots.keys():
            self.slots[key] = None
        return

    def fillslot(self, slot, *values):
        assert(slot in self.slots)
        for value in values:
            #assert(value in self.possiblevalues[slot])
            if value in self.possiblevalues[slot]:
                if self.slots[slot]:
                  if value not in self.slots[slot]:  
                    self.slots[slot].append(value)
                else:
                    self.slots[slot] = [value]
        return

    def getslot(self, slot):
        assert(slot in self.slots)
        return self.slots[slot]

    def getquestion(self, slot):
        assert(slot in self.slots)
        return self.questions[slot]

    def listpossible(self, slot):
        assert(slot in self.slots)
        return self.possiblevalues[slot]        

    def listslots(self):
        return [slot for slot in self.slots.keys()]

    def isempty(self, slot):
        assert(slot in self.slots)
        if not self.slots[slot]: return True
        return False
    
    def pprint(self):
        print("Frame {}: ".format(self.name))
        pprint.pprint(self.slots, indent=4)


        
