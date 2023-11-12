# Category NP is assigned to tokens that have one of the UPOS tags: NOUN, NUM, PRON,
# PROPN, SYM, or non-noun tokens with accompanying determiners that act as nominal 
# subjects or objects, if they do not modify any other constituents. Otherwise,
# their categories are inferred through the category inference step.

UPOS = ["NOUN", "NUM", "PRON", "PROPN", "SYM"]

class NPRule:
    def apply(self, node):
        if node.upos in UPOS: return "NP"
        return None