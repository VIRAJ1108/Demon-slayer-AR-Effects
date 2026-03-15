import random

class Particle:

    def __init__(self, x, y, dx, dy, life=20):

        self.x = x
        self.y = y

        self.dx = dx
        self.dy = dy

        self.life = life


    def update(self):

        self.x += self.dx
        self.y += self.dy

        self.life -= 1


class ParticleSystem:

    def __init__(self):

        self.particles = []


    def emit(self, x, y, direction):

        dx, dy = direction

        dx += random.uniform(-1,1)
        dy += random.uniform(-1,1)

        particle = Particle(x, y, dx*5, dy*5)

        self.particles.append(particle)


    def update(self):

        for p in self.particles:
            p.update()

        self.particles = [p for p in self.particles if p.life > 0]