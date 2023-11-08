# Importing Rules
from ccg_converter.rules.root import RootRules

class CCGConverter:
    def __init__(self):
        self.root_rules = RootRules()

    def convert(self, btree, dtree):
        sentence_cat = self.root_rules.apply(dtree)
        return ""