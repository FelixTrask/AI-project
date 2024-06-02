from vpoint import VPoint
from constants import VELOCITY, MUTATION_RATE, RADIUS, GOAL, MAX_MOVES
import random
import math

class Dot:
    def __init__(self):
        self.curMove = 0
        self.pos = VPoint(0.5, 0.5)
        self.status = 'ALIVE'
        self.moves = [VELOCITY * VPoint.random() for _ in range(MAX_MOVES)]

    def mutate(self):
        mut = Dot()
        mut.moves = [move + VELOCITY * MUTATION_RATE * VPoint.random() for move in self.moves]
        return mut

    def fitness(self):
        if self.win():
            return 1 + (1.0 / MAX_MOVES) * (MAX_MOVES - self.curMove)
        return 1.0 / self.pos.dist(GOAL)

    def alive(self):
        return self.status == 'ALIVE'

    def win(self):
        return self.status == 'WIN'

    def lose(self):
        return self.status == 'LOSE'

    def update(self):
        if self.curMove < len(self.moves):
            self.pos += self.moves[self.curMove]
            self.curMove += 1
            if self.pos.x < RADIUS or self.pos.y < RADIUS or self.pos.x > 1.0 - RADIUS or self.pos.y > 1.0 - RADIUS:
                self.status = 'LOSE'
            elif self.pos.dist(GOAL) < RADIUS:
                self.status = 'WIN'
        else:
            self.status = 'LOSE'

    def draw(self, canvas):
        size = min(canvas.winfo_width(), canvas.winfo_height())
        x = int(size * self.pos.x)
        y = int(size * self.pos.y)
        radius = int(size * RADIUS)
        canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill='red')
