from igraph import *

vertices = ["A", "B", "C", "D", "E"]

edges = [(0,1),(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(7,1),
         (1,8),  (8,2),(2,4),(4,9),(9,5),(5,7),(7,0)]

graphStyle = { 'vertex_size': 20}
g = Graph(vertex_attrs={"label": vertices}, edges=edges, directed=True)
g.write_svg("simple_star.svg", width=500, height=300, **graphStyle)

