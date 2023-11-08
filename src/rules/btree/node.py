class Node:
    def __init__(self):
        self.children = [None, None]

        self.parent = None
    
class DepRelNode(Node):
    def __init__(self, deprel=None):
        super().__init__()

        self.deprel = deprel

class WordNode(Node):
    def __init__(self, word=None, upos=None):
        super().__init__()

        self.word = word
        self.upos = upos