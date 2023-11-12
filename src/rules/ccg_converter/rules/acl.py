# An adnominal clause (acl) modifies a nominal, and thus generally has category
# NP|NP. If an adnominal clause is not marked by any markers (mark), we apply a 
# type-changing rule to change its original category to NP|NP (Figure 4). The 
# original category of an adnominal clause excluding markers is set to S if it
# has a clausal or a nominal subject, and S|NP otherwise.

class AdnoClauseRule:
    def acl_rule(self, node):
        if node.children[0] != None and "mark" in node.children[0].deprel: return "NP|NP"
        if node.children[1] != None and "mark" in node.children[1].deprel: return "NP|NP"

        if node.children[0] != None and "subj" in node.children[0].deprel: return "S"
        if node.children[1] != None and "subj" in node.children[1].deprel: return "S"

        return "S|NP"

    def apply(self, node):
        if node.deprel == "acl": return self.acl_rule(node)
        return None