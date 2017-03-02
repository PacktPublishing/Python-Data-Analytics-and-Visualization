import networkx as nx
G = nx.DiGraph()
G.add_edge('p','y', capacity=5.0)
G.add_edge('p','s', capacity=4.0)
G.add_edge('y','t', capacity=3.0)
G.add_edge('s','h', capacity=5.0)
G.add_edge('s','o', capacity=4.0)

flow_value = nx.maximum_flow_value(G, 'p', 'o')

print "Flow value", flow_value

