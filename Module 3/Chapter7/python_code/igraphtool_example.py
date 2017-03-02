import graph_tool.all as gtool

gr = gtool.collection.data["polblogs"]
gr = gtool.GraphView(gr, vfilt=gtool.label_largest_component(gr))

cness = gtool.closeness(gr)

gtool.graph_draw(gr, pos=gr.vp["pos"], vertex_fill_color=cness,
               vertex_size=gtool.prop_to_size(cness, mi=5, ma=15),
               vorder=cness, vcmap=matplotlib.cm.gist_heat,
               output="political_closeness.pdf")

