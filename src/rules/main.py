from btree.btree import BTree

import sys, os

# === .BINARIZED FILES PARSING ===
# Separate all sentences in a list of instances
def get_sentences(file):
    i, instances = "", []
    for line in file:
        if line == "\n": instances.append(i); i = ""
        else: i += line
    return instances

# Parse all sentences separated into binary trees.
def get_btrees(file):
    btrees = []
    instances = get_sentences(file)
    for instance in instances:
        btrees.append(BTree(instance))
    return btrees

# === END OF .BINARIZED FILES PARSING ===


if __name__ == "__main__":
    path = "../../datasets/" + sys.argv[1] + "/tree_binarization/"
    out_path = "../../datasets/" + sys.argv[1] + "/CCG_conversions/"

    for (dirpath, dirnames, filenames) in os.walk(path):
        for filename in filenames:
            print("Running \"" + filename + "\" conversion...")
            fin = open(path + filename, "r", encoding="utf8")
            trees = get_btrees(fin)