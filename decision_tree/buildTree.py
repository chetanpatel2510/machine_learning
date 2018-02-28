from sklearn import tree
with open("C:/Users/Chetan/Desktop/decision_tree_classifier.txt", "w") as f:
    f = tree.export_graphviz(fruit_classifier, out_file=f)    