#  We follow Hockenmaier and Steedman (2007) and set the category of each punctuation 
# mark to be the punctuation mark itself. Exceptions include dashes, parentheses, and 
# variants of open and closing brackets in different languages (e.g., “【】” in Japanese,
# “《》” in Japanese, Chinese, and Korean). These punctuation marks are treated like 
# normal constituents and carry standard CCG categories.

PUNCTS = ['-', '--', '(', ')', '«', '»']

class PunctRule:
    def apply(self, node):
        if node.upos == "PUNCT" and node.token not in PUNCTS:
            return node.token
        return None