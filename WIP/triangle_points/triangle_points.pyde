class point_triangle:
    def __init__(self, r, x, y, dx, dy):
        self.r = r
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        
    def move(self, max_x, max_y):
        self.x = (self.x + self.dx) % max_x
        self.y = (self.y + self.dy) % max_y
        
    def draw_self(self):
        circle(self.x, self.y, self.r)
        
class line_triangle:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.c = self.get_c()
        
    def draw_self(self):
        self.c = self.get_c()
        stroke(255 * self.c)
        line(self.p1.x, self.p1.y, self.p2.x, self.p2.y)
        
    def get_c(self):
        d = ((self.p1.x - self.p2.x)**2 + (self.p1.y - self.p2.y)**2) ** 0.5
        return atan(d/50)**2 * 2/3.141592
    
    
 
points = []
lines = []

def setup():
    frameRate(40)
    size(400, 400)
    n_points = 20
    max_v = 3.
    for _ in range(n_points):
        points.append(point_triangle(10, float(random(width)), float(random(height)), 
                                     random(max_v) - max_v/2, random(max_v) - max_v/2))
    for p1 in points:
        for p2 in points:
            if p1!=p2:
                lines.append(line_triangle(p1, p2))
    
def draw():
    global points, lines
    clear()
    background(255)
    
    lines = sorted(lines, key= lambda l: 1 - l.c)
    for l in lines:
        l.draw_self()
    
    stroke(0)
    color(0)
    for p in points:
        p.move(width, height)
        p.draw_self()
