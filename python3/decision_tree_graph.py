#!/usr/bin/env python
'''Decision Tree Graph: Step by Step Guide Using Iris Dataset'''

from sklearn.datasets import load_iris
from sklearn import tree
from sklearn.tree import export_graphviz
from sklearn.externals.six import StringIO
import pydotplus

clf = tree.DecisionTreeClassifier()
iris = load_iris()

#train the classifier
clf = clf.fit(iris.data, iris.target)

#create a StringIO object
dot_data = StringIO() 

#export the tree in the DOT format
tree.export_graphviz(clf, out_file=dot_data, feature_names=iris.feature_names, class_names=iris.target_names, filled=True, impurity=False)
 
#load the graph in the DOT format. StringIO instances are OK. Extract the content of the StringIO file-like object using getvalue().
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())

#save the graph (as pdf, png, gif, etc.)
graph.write_pdf("my_iris_tree.pdf")