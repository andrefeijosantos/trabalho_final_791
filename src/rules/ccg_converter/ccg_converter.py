# Importing Rules
from ccg_converter.rules.root import RootRule
from ccg_converter.rules.np import NPRule
from ccg_converter.rules.acl import AdnoClauseRule
from ccg_converter.rules.advcl import AdvClauseRule
from ccg_converter.rules.comp import ClausalCompRule
from ccg_converter.rules.csubj import ClausalSubjRule
from ccg_converter.rules.prataxis import PrataxisRule
from ccg_converter.rules.punct import PunctRule

class CCGConverter:
    def __init__(self):
        self.root_rule = RootRule()
        self.rules = [NPRule(), AdnoClauseRule(), ClausalCompRule(), ClausalSubjRule(), 
                      PrataxisRule(), PunctRule(), AdvClauseRule()]

    def convert(self, btree):
        if btree.root == None: return btree
        btree.root.category = self.root_rule.apply(btree.dtree)

        queue = [btree.root.children[0], btree.root.children[1]]
        while queue:
            node = queue.pop(0)
            if node == None: continue

            # Assign to a node its correspondent rule.
            self.assign(node)

            # Add the node's children to the queue.
            for child in node.children:
                queue.append(child)

        btree = self.category_inference(btree)

        return btree

    def category_inference(self, btree):
        if btree.root == None: return btree

        queue = [btree.root.children[0], btree.root.children[1]]
        while queue:
            node = queue.pop(0)
            if node == None: continue

            # Assign to a node its correspondent rule.
            if node.category == None:
                self.inference(node)

            # Add the node's children to the queue.
            for child in node.children:
                queue.append(child)

        return btree

    def assign(self, node):
        for rule in self.rules:
            category = rule.apply(node) 
            if category != None:
                node.category = category
                break

    def inference(self, node):
        return