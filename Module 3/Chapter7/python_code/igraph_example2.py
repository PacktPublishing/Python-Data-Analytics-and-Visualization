from igraph import read  

g=read("ragusa.net",format="pajek")  
  
g.vs["color"]="#3d679d" 
g.es["color"]="red" 

graphStyle={ 'vertex_size': 12, 'margin': 6} 
#graphStyle["layout"]=g.layout("fr")  # optional

g.write_svg("ragusa_graph.svg", width=600, height=600,**graphStyle)

