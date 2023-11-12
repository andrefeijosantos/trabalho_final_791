# We assign category S to a clausal complement (ccomp) if it has a subject, 
# and category S|NP if it does not. An open clausal complement (xcomp) is 
# assigned category NP if its head element has one of the following UPOS tags: 
# NOUN, NUM, PRON, PROPN, SYM. Otherwise, it is also assigned category S|NP.

UPOS = ["NOUN", "NUM", "PRON", "PROPN", "SYM"]

class ClausalCompRule:
    def ccomp(self, node):
        if node.children[0] != None and "subj" in node.children[0].deprel: return "S"
        if node.children[1] != None and "subj" in node.children[1].deprel: return "S"
        return "S|NP"

    def xcomp(self, node):
        if node.upos in UPOS: return "NP"
        return "S|NP"

    def apply(self, node):
        if node.deprel == "ccomp": return self.ccomp(node)
        if node.deprel == "xcomp": return self.xcomp(node)
        return None