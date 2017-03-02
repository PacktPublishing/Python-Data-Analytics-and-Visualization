from sklearn.externals.six import StringIO
from sklearn import tree
import pydot 

 
X=[[1,1,1,0],[1,1,1,1],[2,1,1,0],[2,3,2,1],[1,2,1,0],[1,3,2,0],\
[3,2,1,0],[3,3,2,0],[3,3,2,1],[3,2,2,0],[1,2,2,1],[2,2,1,1],\
[2,1,2,0],[3,2,1,0]]  

Y=[0,0,1,1,0,1,1,1,0,1,1,1,1,0] 

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)

dot_data = StringIO() 
tree.export_graphviz(clf, out_file=dot_data) 

graph = pydot.graph_from_dot_data(dot_data.getvalue()) 
graph.write_pdf("game.pdf")

