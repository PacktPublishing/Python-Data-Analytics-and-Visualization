import os
display_prog = 'more' # Command to execute to display images.
svcount=1
      
class Scene:
    def __init__(self,name="svg",height=400,width=1200):
        self.name = name
        self.items = []
        self.height = height
        self.width = width
        return

    def add(self,item): self.items.append(item)

    def strarray(self):
        var = [ "<html>\n<body>\n<svg height=\"%d\" width=\"%d\" >\n" % (self.height,self.width),
               "  <g id=\"setttings\">\n",
               "    <filter id=\"dropshadow\" height=\"160%\">\n",
               "     <feGaussianBlur in=\"SourceAlpha\" stdDeviation=\"5\"></feGaussianBlur>\n",
               "       <feOffset dx=\"0\" dy=\"3\" result=\"offsetblur\"></feOffset>\n",
               "       <feMerge>\n",
               "          <feMergeNode></feMergeNode>\n",
               "          <feMergeNode in=\"SourceGraphic\"></feMergeNode>\n",
               "       </feMerg>\n",
               "    </filter>\n"]
        for item in self.items: var += item.strarray()            
        var += [" </g>\n</svg>\n</body>\n</html>"]
        return var

    def write_svg(self,filename=None):
        if filename:
            self.svgname = filename
        else:
            self.svgname = self.name + ".html"
        file = open(self.svgname,'w')
        file.writelines(self.strarray())
        file.close()
        return

    def display(self,prog=display_prog):
        os.system("%s %s" % (prog,self.svgname))
        return        
        
def colorstr(rgb): return "#%x%x%x" % (rgb[0]/16,rgb[1]/16,rgb[2]/16)

class Text:
    def __init__(self, x,y,txt, color, isItbig, isBold):
        self.x = x
        self.y = y
        self.txt = txt
        self.color = color
        self.isItbig = isItbig 
        self.isBold = isBold
    def strarray(self):
        if ( self.isItbig == True ):
          if ( self.isBold == True ):
            retval = [" <text y=\"%d\" x=\"%d\" style=\"font-size:18px;font-weight:bold;fill:%s\">%s</text>\n" %(self.y, self.x, self.color,self.txt) ]
          else:
            retval = [" <text y=\"%d\" x=\"%d\" style=\"font-size:18px;fill:%s\">%s</text>\n" %(self.y, self.x, self.color,self.txt) ]
        else:
          if ( self.isBold == True ):
            retval = [" <text y=\"%d\" x=\"%d\" style=\"fill:%s;font-weight:bold;\">%s</text>\n" %(self.y, self.x, self.color,self.txt) ]
          else:
            retval = [" <text y=\"%d\" x=\"%d\" style=\"fill:%s\">%s</text>\n" %(self.y, self.x, self.color,self.txt) ]
        return retval

class Circle:
    def __init__(self,center,radius,color, perc):
        self.center = center #xy tuple
        self.radius = radius #xy tuple
        self.color = color   #rgb tuple in range(0,256)
        self.perc = perc
        return

    def strarray(self):
        global svcount
        diam = self.radius+self.radius
        fillamt = self.center[1]-self.radius - 6 + (100.0 - self.perc)*1.9
        xpos = self.center[0] - self.radius
        retval = ["  <circle cx=\"%d\" cy=\"%d\" r=\"%d\"\n" %\
                (self.center[0],self.center[1],self.radius),
                "    style=\"stroke: %s;stroke-width:2;fill:white;filter:url(#dropshadow)\"  />\n" % colorstr(self.color),
               "  <circle clip-path=\"url(#dataseg-%d)\" fill=\"%s\" cx=\"%d\" cy=\"%d\" r=\"%d\"\n" %\
                (svcount, colorstr(self.color),self.center[0],self.center[1],self.radius),
                "    style=\"stroke:rgb(0,0,0);stroke-width:0;z-index:10000;\"  />\n",
               "<clipPath id=\"dataseg-%d\"> <rect height=\"%d\" width=\"%d\" y=\"%d\" x=\"%d\"></rect>" %(svcount,diam, diam,fillamt,xpos),
               "</clipPath>\n"
                ]
        svcount += 1
        return retval

def languageDistribution():
    scene = Scene('test')
    scene.add(Circle((140,146),100,(0,128,0),54))
    scene.add(Circle((370,146),100,(232,33,50),42))
    scene.add(Circle((600,146),100,(32,119,180),65))
    scene.add(Circle((830,146),100,(255,128,0),27))
    scene.add(Text(120,176,"English", "white", False, True))
    scene.add(Text(120,196,"Speaking", "#e2e2e2", False, False))
    scene.add(Text(340,202,"German", "black", False, True))
    scene.add(Text(576,182,"Spanish", "white", False, True))
    scene.add(Text(804,198,"Japanese", "black", False, True))

    scene.add(Text(120,88,"54%", "black", True, True))
    scene.add(Text(350,88,"42%", "black", True, True))
    scene.add(Text(585,88,"65%", "black", True, True))
    scene.add(Text(815,88,"27%", "black", True, True))

    scene.write_svg()
    scene.display()
    return

if __name__ == '__main__': languageDistribution()

