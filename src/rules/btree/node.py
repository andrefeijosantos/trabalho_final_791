class Node:
    def __init__(self, deprel=None, token=None, upos=None):
        self.children = [None, None]
        self.parent = None

        # UD specific stuff
        self.deprel = deprel
        self.upos = upos
        self.token = token

        # CCG specific stuff
        self.category = None