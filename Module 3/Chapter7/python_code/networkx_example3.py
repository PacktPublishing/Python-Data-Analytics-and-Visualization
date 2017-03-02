import networkx as nx

g = nx.Graph()
g.add_edge('m','i',weight=0.1)
g.add_edge('i','a',weight=1.5)
g.add_edge('m','a',weight=1.0)
g.add_edge('a','e',weight=0.75)
g.add_edge('e','h',weight=1.5) 
g.add_edge('a','h',weight=2.2)

print nx.shortest_path(g,'i','h')
nx.draw(g)

