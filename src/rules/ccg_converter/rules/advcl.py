# Similarly, an adverbial clause advcl usually has category (S|NP)|(S|NP), as
# it modifies a verb or a predicate. If an adverbial clause does not have any 
# markers (mark), we apply a type-changing rule to change its original category
# to (S|NP)|(S|NP). We set the original category of an adverbial clause excluding 
# markers to S if it has a clausal or a nominal subject, and S|NP otherwise. An
# adverbial clause can also appear in sentential modifier locations, in which 
# case its category would be S|S.

class AdvClauseRule:
    def apply(self, node):
        if node.children[0] != None and "nsubj" in node.children[0].deprel: return "S"
        if node.children[1] != None and "nsubj" in node.children[1].deprel: return "S"

        if node.children[0] != None and "csubj" in node.children[0].deprel: return "S"
        if node.children[1] != None and "csubj" in node.children[1].deprel: return "S"
        return "S|NP"