#  The UD guidelines detail five different constructions where parataxis can appear: 
# side-by-side sentences, reported speech, news article bylines, interjected clauses, 
# and tag questions. Unfortunately, this makes it difficult to define a common rule 
# for all the constructions. For example, side-by-side (“run-on”) sentences and reported 
# speech have different CCG analyses, but they are hard to distinguish just by their 
# dependency structures. We decide to treat the dependent constituent as a modifier to 
# the head constituent (Figure 7).

class PrataxisRule:
    def apply(self, node):
        return None