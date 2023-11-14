#  We only apply rules for a clausal subject (csubj) if it has another 
# subject within. In this case, if a clausal subject is marked by a marker 
# (mark), it is assigned category S. Otherwise, it is assigned category NP 
# (Figure 6). In other cases, clausal subjects are treated like normal core 
# arguments, and their categories are inferred through the category inference 
# step.

class ClausalSubjRule:
    def apply(self, node):
        if node.children[0] != None and "subj" in node.children[0].deprel: return "NP"
        if node.children[1] != None and "subj" in node.children[1].deprel: return "NP"

        if node.children[0] != None and "mark" in node.children[0].deprel: return "S"
        if node.children[1] != None and "mark" in node.children[1].deprel: return "S"

        return None