class Dependency:
    """ Dependencies """
    def __init__(self, sentence, dependency, tokens):
        # Internal (fixed) parameters
        self.relation = 0
        self.origin = 1
        self.dest = 2
        self.sentence = ""
        self.dependency = []
        self.tokens = []
        self.update(sentence, dependency, tokens)

    def update(self, sentence, dependency, tokens):
        self.sentence = sentence
        self.tokens = tokens
        self.setdependency(dependency)

    def setdependency(self, dependency):
        # Fix indices.
        self.dependency = [(item[self.relation], item[self.origin]-1, item[self.dest]-1) for item in dependency]
        return

    def getsentence(self):
        return self.sentence

    def getdependency(self):
        return self.dependency
    
    def gettokens(self):
        return self.tokens

    def gettoken(self, index):
        assert(index in range(len(self.tokens)))
        return self.tokens[index]



