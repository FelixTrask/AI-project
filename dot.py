from vpoint import VPoint
from constants import VELOCITY, MUTATION_RATE, RADIUS, GOAL, MAX_MOVES, WALLS
import random
import math

class Dot:
    def __init__(self):
        self.curMove = 0
        self.pos = VPoint(0.5, 0.5)
        self.status = 'ALIVE'
        self.moves = [VELOCITY * VPoint.random() for _ in range(MAX_MOVES)]

    def mutate(self):
        # Mutate the moves of the dot
        mut = Dot()
        mut.moves = [move + VELOCITY * MUTATION_RATE * VPoint.random() for move in self.moves]
        return mut
    
    # Fitness function
    def fitness(self):
        # If the dot wins, it gets a bonus based on how many moves it took to reach the goal
        # If the dot loses, it gets a penalty based on how far it is from the goal
        if self.win():
            return 1 + (1.0 / MAX_MOVES) * (MAX_MOVES - self.curMove)
        dist = self.pos.dist(GOAL)
        return 1.0 / (dist * dist)

    def alive(self):
        return self.status == 'ALIVE'

    def win(self):
        return self.status == 'WIN'

    def lose(self):
        return self.status == 'LOSE'

    def update(self):
        if self.curMove < len(self.moves):
            new_pos = self.pos + self.moves[self.curMove]
            if not self.check_wall_collision(new_pos):
                self.pos = new_pos
                self.curMove += 1
                if self.pos.x < RADIUS or self.pos.y < RADIUS or self.pos.x > 1.0 - RADIUS or self.pos.y > 1.0 - RADIUS:
                    self.status = 'LOSE'
                elif self.pos.dist(GOAL) < RADIUS:
                    self.status = 'WIN'
            else:
                self.status = 'LOSE'
        else:
            self.status = 'LOSE'

    def draw(self, canvas):
        size = min(canvas.winfo_width(), canvas.winfo_height())
        x = int(size * self.pos.x)
        y = int(size * self.pos.y)
        radius = int(size * RADIUS)
        canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill='red')

    def check_wall_collision(self, new_pos):
        for wall in WALLS:
            if self.intersects_wall(self.pos, new_pos, wall[0], wall[1]):
                return True
        return False

    def intersects_wall(self, p1, p2, w1, w2):
        def ccw(A, B, C):
            return (C.y - A.y) * (B.x - A.x) > (B.y - A.y) * (C.x - A.x)

        return ccw(p1, w1, w2) != ccw(p2, w1, w2) and ccw(p1, p2, w1) != ccw(p1, p2, w2)
