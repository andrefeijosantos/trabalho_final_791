from btree.node import *

class BTree:
    # Constructor.
    # @param inst The DT instance.
    def __init__(self, inst : str):
        self.sent_id, self.text, i = inst.split("\n", maxsplit=2)
        self.root = None
        self.to_btree(i)

    # Parsing function, for converting a string into a binary tree.
    # @param inst The DT instance.
    # @returns tree The binary tree representation of the instance
    def to_btree(self, inst : str):
        tree = ""; lines = inst.split("\n")
        for line in lines:
            tree += " " + line.lstrip(" ")
        tree = tree.rstrip(" ").lstrip(" ")

        self.root = [None]
        self.parse(tree, self.root)
        self.root = self.root[0]

    # A recursive function to create the binary tree from its string representation
    # @param string The current string representation
    # @param node The node that will store the tree root
    def parse(self, tree : str, nodes, pos = 0):
        if not len(tree): return

        # First, removes the enclosing parenthesws to get root node
        tree = tree.rstrip(" ").lstrip(" ")
        new_tree = tree[1:len(tree)-1]

        # If there's still any parathenses in the subtree, so it's not a leaf, then
        # it's a Deprel Node.
        if "(" in new_tree:
            new_tree = new_tree.split(" ")
            deprel, new_tree = new_tree[0], " ".join(new_tree[1:])
            nodes[pos] = DepRelNode(deprel=deprel)

            lchild, rchild = self.get_subtrees(new_tree)
            self.parse(lchild, nodes[pos].children, pos=0)
            self.parse(rchild, nodes[pos].children, pos=1)
        else:
            new_tree = new_tree.split(" ")
            upos, word = new_tree[0], " ".join(new_tree[1:])
            nodes = WordNode(word=word, upos=upos)
            return
        
    # Given a string-represented tree, returns the present subtrees in this string
    # @param tree The string representation
    # @returns (lchild, rchild) the left and right subtrees
    def get_subtrees(self, tree : str):
        lchild, rchild = "", tree
        cnt, lstart = 0, 0

        for i in range(len(tree)):
            if tree[i] == "(": cnt += 1
            elif tree[i] == ")": cnt -= 1

            # Pop a char from the right subtree and add it on left one
            lstart += 1; lchild += tree[i]

            # If the parathenses are balanced, then we found the left subtree.
            if cnt == 0: return lchild, rchild[lstart:]