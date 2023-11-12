# Importing Rules
from ccg_converter.rules.root import RootRule
from ccg_converter.rules.np import NPRule
from ccg_converter.rules.acl import AdnoClauseRule
from ccg_converter.rules.comp import ClausalCompRule

class CCGConverter:
    def __init__(self):
        self.root_rule = RootRule()
        self.rules = [NPRule(), AdnoClauseRule(), ClausalCompRule()]

    def convert(self, btree):
        if btree.root == None: return btree
        btree.root.category = self.root_rule.apply(btree.dtree)

        found = set()
        queue = [btree.root.children[0], btree.root.children[1]]
        while queue:
            node = queue.pop(0)
            if node == None: continue
            if node in found: continue

            # Assign to a node its correspondent rule.
            self.assign(node)

            # Make sure this node won't be visited again and add its
            # children to the queue.
            found.add(node)
            for child in node.children:
                queue.append(child)

        return btree
    
    def assign(self, node):
        for rule in self.rules:
            category = rule.apply(node) 
            if category != None:
                node.category = category
                break