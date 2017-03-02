import networkx as nx
from pylab import rcParams
rcParams['figure.figsize'] = 12, 12

G = nx.read_gml('/Users/MacBook/Downloads/Book_code/Chapter7/python_code/lesmiserables.gml', relabel=True)
G8= G.copy()
dn = nx.degree(G8)
for n in G8.nodes():
  if dn[n] <= 8:
    G8.remove_node(n)
pos= nx.spring_layout(G8)
nx.draw(G8, node_size=10, edge_color='b', alpha=0.45, font_size=9, pos=pos)
labels = nx.draw_networkx_labels(G8, pos=pos)

