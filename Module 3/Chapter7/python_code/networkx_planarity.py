import planarity 
import networkx as nx 

# complete graph of 8 nodes, K8 
G8=nx.complete_graph(8) 

# K8 is not planar 
print(planarity.is_planar(G8)) 

# Will display false because G8 is not planar
subgraph K=planarity.kuratowski_subgraph(G8) 

# Will display the edges
print(K.edges())
 
#Will display the graph
nx.draw(G8)

