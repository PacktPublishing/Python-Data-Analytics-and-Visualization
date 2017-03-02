import matplotlib.pyplot as plt
import matplotlib.cm
import random
import squarify

x = 0.
y = 0.
width = 950.
height = 733.
norm_x=1000
norm_y=1000

fig = plt.figure(figsize=(15,13))
ax=fig.add_subplot(111,axisbg='white')

initvalues = [285.4,188.4,173,140.6,91.4,75.5,62.3,39.6,29.4,28.5, 26.2, 22.2]
values = initvalues
labels = ["South Africa", "Egypt", "Nigeria", "Algeria", "Morocco",
"Angola", "Libya", "Tunisia", "Kenya", "Ethiopia", "Ghana", "Cameron"]

colors = [(214,27,31),(229,109,0),(109,178,2),(50,155,18), 
(41,127,214),(27,70,163),(72,17,121),(209,0,89), 
(148,0,26),(223,44,13), (195,215,0)] 
# Scale the RGB values to the [0, 1] range, which is the format matplotlib accepts. 
for i in range(len(colors)): 
  r, g, b = colors[i] 
  colors[i] = (r / 255., g / 255., b / 255.) 

# values must be sorted descending (and positive, obviously)
values.sort(reverse=True)

# the sum of the values must equal the total area to be laid out
# i.e., sum(values) == width * height
values = squarify.normalize_sizes(values, width, height)

# padded rectangles will probably visualize better for certain cases
rects = squarify.padded_squarify(values, x, y, width, height)

cmap = matplotlib.cm.get_cmap()

color = [cmap(random.random()) for i in range(len(values))]
x = [rect['x'] for rect in rects]
y = [rect['y'] for rect in rects]
dx = [rect['dx'] for rect in rects]
dy = [rect['dy'] for rect in rects]

ax.bar(x, dy, width=dx, bottom=y, color=colors, label=labels)

va = 'center'
idx=1

for l, r, v in zip(labels, rects, initvalues):
    x, y, dx, dy = r['x'], r['y'], r['dx'], r['dy']
    ax.text(x + dx / 2, y + dy / 2+10, str(idx)+"--> "+l, va=va, ha='center', color='white', fontsize=14)
    ax.text(x + dx / 2, y + dy / 2-12, "($"+str(v)+"b)", va=va, ha='center', color='white', fontsize=12)
    idx = idx+1

ax.set_xlim(0, norm_x)
ax.set_ylim(0, norm_y)

plt.show()

