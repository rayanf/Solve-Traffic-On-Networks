class Point:
    def __init__(self,initx,inity):
        self.x = initx
        self.y = inity

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def negx(self):
        return -(self.x)

    def negy(self):
        return -(self.y)

    def __str__(self):
        return 'x=' + str(self.x) + ', y=' + str(self.y)

    def halfway(self,target):
        midx = (self.x + target.x) / 2
        midy = (self.y + target.y) / 2
        return Point(midx, midy)

    def distance(self,target):
        xdiff = target.x - self.x
        ydiff = target.y - self.y
        dist = math.sqrt(xdiff**2 + ydiff**2)
        return dist

    def reflect_x(self):
        return Point(self.negx(),self.y)

    def reflect_y(self):
        return Point(self.x,self.negy())

    def reflect_x_y(self):
        return Point(self.negx(),self.negy())

    def slope_from_origin(self):
        if self.x == 0:
            return None
        else:
            return self.y / self.x

    def slope(self,target):
        if target.x == self.x:
            return None
        else:
            m = (target.y - self.y) / (target.x - self.x)
            return m


class Line:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def calLine(self,a,b):
        self.div = (b.y - a.y)/(b.x - a.x)
        self.k = b.x - (self.div * a.x)


    def y(self,x):
        return (self.div*x) + self.k


def alghoritm(restsPoint,firePoint,alpha):
    p = 10
    checkk = check(firePoint,p)
    while checkk == False:
        p -= alpha
        checkk = check(firePoint,p)

    return p

def check(firePoint,p):
    for i in firePoint:
        if i < p:
            return False
    else:
         return True


def findProb(x,line_0,line_Q):
    fireProb = line_0.y(x)
    restsProb = line_Q.y(x)
    return fireProb,restsProb



a = Point(0,10)
b = Point(10,0)

line_0 = Line(a,b)
line_0.calLine(a,b)


restsPoint = [0,0,1,3,3]
firePoint = [4, 5, 5,5 ,6 ,6 ,7 ,8,10]

p = alghoritm(restsPoint,firePoint,0.5)
p = Point(p,10-p)
# q, q_ =findProb(p,line)
c = Point(0,0)

line_Q = Line(c,p)
line_Q.calLine(c,p)
x = 1
rest,fire = findProb(x,line_0,line_Q)

if rest >= fire:
    print('rest')

else:
    print('fire')
