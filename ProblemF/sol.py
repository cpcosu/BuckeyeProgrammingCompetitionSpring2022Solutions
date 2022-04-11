from math import radians, cos, sin, sqrt

class traveler:
    def __init__(self, x:float = 0, y:float = 0, radius:float = 5, angle:float = 45, speed:float = 2):
        self.x = x
        self.y = y
        self.radius = radius

        self.angle = radians(angle)
        self.dAngle = angle
        self.speed = speed

        self.sx = speed * cos(self.angle)
        self.sy = speed * sin(self.angle)

    def __matmul__(self, time):
        return (self.x + self.sx * time, self.y + self.sy * time)

    def __str__(self):
        return f'{self.x} {self.y} {self.radius} {self.dAngle} {self.speed}'

    def intersects(self, other, maxTime) -> bool:

        dvx = other.sx - self.sx 
        dvy = other.sy - self.sy

        dx = other.x - self.x
        dy = other.y - self.y


        a = dvx ** 2 + dvy ** 2
        b = 2 * (dvx * dx + dvy * dy)
        c = other.x**2 + other.y**2 + self.x**2 + self.y** 2 - 2 * (self.x * other.x + self.y * other.y)

        if not a:
            dist = sqrt(dx**2 + dy**2)
            return dist < self.radius + other.radius, 0
        
        c -= (self.radius + other.radius) ** 2
        
        disc = b**2 - 4*a*c
        
        if disc > 0:
            disc = sqrt(disc)
        else:
            return 0, maxTime
        
        zero1 = (-b + disc) / (2 * a)
        zero2 = (-b - disc) / (2 * a)

        cols = (zero1, zero2)
        zero1 = min(cols)
        zero2 = max(cols)

        collided = 0

        if zero1 < 0 and zero2 > 0:
            collided, t = 1, 0

        elif zero2 < 0:
            collided, t = 0, zero2
        
        elif zero1 > maxTime:
            collided, t = 1, zero1

        else:
            collided, t = 1, zero1

        return collided, t

shipdata = tuple(map(int, input().split()))

ship = traveler(shipdata[0], shipdata[1], shipdata[2], shipdata[3], shipdata[4])
maxTime = shipdata[5] / shipdata[4]

numAsteroids = int(input())
asteroids = []
for _ in range(numAsteroids):
    asteroids.append(traveler(*tuple(map(int, input().split()))))

mint = maxTime; ind = 0
for check in asteroids:
    c, t = ship.intersects(check, maxTime)

    if c:
        
        x = round(t, 2)

        mint = min(x, mint)

    ind += 1

print(mint if mint < maxTime else 'safe')