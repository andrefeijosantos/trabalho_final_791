# An adnominal clause (acl) modifies a nominal, and thus generally has category
# NP|NP. If an adnominal clause is not marked by any markers (mark), we apply a 
# type-changing rule to change its original category to NP|NP (Figure 4). The 
# original category of an adnominal clause excluding markers is set to S if it
# has a clausal or a nominal subject, and S|NP otherwise.
#
# A relative clause is tagged as a subtype of an adnominal clause in UD (acl:relcl), 
# but it requires a separate rule to produce a correct CCG derivation:
# * The relative pronoun (identified through feature PronType=Rel) is assigned category
# (NP|NP)|(S|NP), as it takes a sentence missing a subject or an object as an argument, 
# and yields a nominal modifier.
# * If a relative clause does not have a relative pronoun, its original category is set 
# to S|NP, and is typechanged to NP|NP.
# * In the case of an interrogative pronoun, the constituent consisting of the interrogative 
# pronoun and its head is assigned category (NP|NP)|(S|NP).

class AdnoClauseRule:
    def acl_rule(self, node):
        if node.children[0] != None and "nsubj" in node.children[0].deprel: return "S"
        if node.children[1] != None and "nsubj" in node.children[1].deprel: return "S"

        if node.children[0] != None and "csubj" in node.children[0].deprel: return "S"
        if node.children[1] != None and "csubj" in node.children[1].deprel: return "S"
        return "S|NP"

    def acl_rel_rule(self, node):
        return None

    def apply(self, node):
        if node.deprel == "acl": return self.acl_rule(node)
        if node.deprel == "acl:relcl": return self.acl_rel_rule(node)
        return None