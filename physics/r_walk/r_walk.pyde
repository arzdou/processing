class point():
    n_points = 0
    def __init__(self, x0, y0, dr):
        self._x = [x0,]
        self._y = [y0,]
        self._dr = dr
        point.n_points += 1
        
    def move(self):
        self._x.append((randomGaussian()*self._dr + self._x[-1])%height)
        self._y.append((randomGaussian()*self._dr + self._y[-1])%width)
        
    def reset(self, x0, y0):
        self._x = [x0,]
        self._y = [y0,]
        
    def get_pos(self):
        return (self._x[-1], self._y[-1])
    
    def get_vec_pos(self):
        return (self._x, self._y)
    
points = []
n_points = 100

def setup():
    global points, n_points
    size(1000, 1000)
    background(192, 64, 0)
    stroke(255)
        
      
def draw():
    global points, n_points
    background(192, 64, 0)
    bins = n_points
    histx = [0 for i in range(bins)]
    histy = [0 for i in range(bins)]

    for p in points:
        p.move()
        x,y = p.get_pos()
        histx[int(x / height * bins)]+=1
        histy[int(y / width * bins)]+=1
        
        fill(255),stroke(255)
        circle(x, y, 5)
    
    for i in range(bins):
        rect(height/bins*i, 0, height/bins, histx[i] * 60 / (max(histx)+1))
        rect(0, width/bins*i, histy[i] * 60 / (max(histy)+1), width/bins)

def mousePressed():
    points.extend([point(mouseX, mouseY, 1) for i in range(n_points)])

    
