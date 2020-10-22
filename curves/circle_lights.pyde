class Circles():
    n_objects = 0
    def __init__(self, _length, _color, _origin):
        self._length = _length
        self._color = _color
        self._origin = _origin
        self._theta = [random(2*3.141592) for i in range(self._length)]
        self._radius = [random(1, 15) for i in range(self._length)]
        self._omega = [random(0.01, 0.1) for i in range(self._length)]
        self._cX, self._cY, self._pathX, self._pathY = [],[],[],[]
        Circles.n_objects+=1
        
    def update(self):
        for i in range(self._length):
            self._theta[i] = (self._theta[i] + self._omega[i]) % (2 * 3.141592)
    
        x = [r*cos(t) for r,t in zip(self._radius, self._theta)]
        y = [r*sin(t) for r,t in zip(self._radius, self._theta)]
        self._cX, self._cY = self.cumsum(x), self.cumsum(y)
        self._pathX.append(self._cX[-1])
        self._pathY.append(self._cY[-1])
        if len(self._pathX)>50:
            self._pathX.pop(0)
            self._pathY.pop(0)
    
    def draw_particle(self):
        stroke(*self._color)
        a = 255
        for i in range(1, len(self._pathX)):
            alpha(a); a-=10
            line(self._origin[0] + self._pathX[i-1], self._origin[1] + self._pathY[i-1], 
                 self._origin[0] + self._pathX[i], self._origin[1] + self._pathY[i])
        
    def draw_circles(self):
        stroke(40)
        for i in range(1, self._length):
            line(self._origin[0] + self._cX[i-1], self._origin[1] + self._cY[i-1],
                 self._origin[0] + self._cX[i], self._origin[1] + self._cY[i])
        
        for i, j, k in zip(self._cX, self._cY, self._radius):
            circle(self._origin[0] + i, self._origin[1] + j, 2*k)
    
    @staticmethod
    def cumsum(l):
        return [sum(l[:i]) for i in range(len(l))]

circles = []

def setup():
    background(0)
    size(500,500)
    noFill(); stroke(255)

def draw():
    global circles
    background(0)
    for c in circles:
        c.update()
        c.draw_circles()
        c.draw_particle()
        
def mousePressed():
    c = (random(255), random(255), random(255))
    circles.append(Circles(int(random(15,60)), c, (mouseX, mouseY)))
    
