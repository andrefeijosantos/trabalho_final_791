from btree.btree import BTree
from ccg_converter.ccg_converter import CCGConverter
import sys, os
from conllu import parse_tree

# === .BINARIZED FILES PARSING ===
# Separate all sentences in a list of instances
def get_sentences(file):
    i, instances = "", []
    for line in file:
        if line == "\n": instances.append(i); i = ""
        else: i += line
    return instances

# Parse all sentences separated into binary trees.
def get_trees(btree_file, dtree_file):
    instances = get_sentences(btree_file)
    trees = []; dtrees = parse_tree(dtree_file.read())

    for i in range(len(instances)):
        trees.append(BTree(instances[i], dtrees[i]))
    return trees

# === END OF .BINARIZED FILES PARSING ===


if __name__ == "__main__":
    btree_path = "../../datasets/" + sys.argv[1] + "/tree_binarization/"
    dtree_path = "../../datasets/" + sys.argv[1] + "/UD/"
    out_path = "../../datasets/" + sys.argv[1] + "/CCG_conversions/"

    converter = CCGConverter()
    for (dirpath, dirnames, filenames) in os.walk(btree_path):
        for filename in filenames:
            print("Running \"" + filename + "\" conversion...", end=" ")

            btree_fin = open(btree_path + filename, "r", encoding="utf8")
            dtree_fin = open(dtree_path + filename.rstrip("binarized") + "conllu", "r", encoding="utf8")
            fout = open(out_path + filename.rstrip("binarized") + "ccg", "w", encoding="utf8")

            trees = get_trees(btree_fin, dtree_fin)
            for tree in trees: fout.write(converter.convert(tree).to_string())

            print("done!")