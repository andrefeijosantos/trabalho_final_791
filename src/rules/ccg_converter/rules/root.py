# We determine the category of a whole sentencec through the root of the DEPENDECY TREE. A sentence
# is assigned category NP if: 
#   * The root has one of the following UPOS tags: NOUN, NUM, PRON, PROPN, SYM
#   * The root does not have any nominal subject, clausal subject or expleitive children.
# A sentence is assigned category S|NP if: 
#   * The root does not have one of the following UPOS tags: NOUN, NUM, PRON, PROPN, SYM
#   * The root has any nominal subject, clausal subject or expleitive children.
# Otherwise, the sentence is assigned category S.

UPOS = ["NOUN", "NUM", "PRON", "PROPN", "SYM"]
CHLD_DEPREL = ["nsubj", "csubj", "expl"]

class RootRule:
    def apply(self, dtree):
        in_upos = dtree.token["upos"] in UPOS
        chld_in_deprel = False

        for chld in dtree.children:
            if chld.token["deprel"] in CHLD_DEPREL:
                chld_in_deprel = True

        if in_upos and not chld_in_deprel: return "NP"
        if not in_upos and chld_in_deprel: return "S|NP"
        return "S"