from vpoint import VPoint
from constants import VELOCITY, MUTATION_RATE, RADIUS, GOAL, MAX_MOVES, WALLS, GREEN, RED
import random
import math

class Dot:
    def __init__(self):
        self.curMove = 0
        self.pos = VPoint(0.5, 0.5)
        self.status = 'ALIVE'
        self.moves = [VELOCITY * VPoint.random() for _ in range(MAX_MOVES)]
        self.color = RED

    def mutate(self):
        mut = Dot()
        mut.moves = [move + VELOCITY * MUTATION_RATE * VPoint.random() for move in self.moves]
        return mut

    def fitness(self):
        distance_to_goal = self.pos.dist(GOAL)
        if self.win():
            # Winning dots get a high fitness based on moves taken to reach the goal
            return 10.0 + (1.0 / MAX_MOVES) * (MAX_MOVES - self.curMove)
        elif self.alive():
            # Dots that are alive get a fitness based on distance to goal
            return 1.0 / distance_to_goal
        else:
            # Dots that are dead get a fitness based on distance to goal
            # with a small penalty
            return 1.0 / (distance_to_goal + 0.1)

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
        if self.color == GREEN:
            radius += 2
        canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill=self.color, outline='black')

    def check_wall_collision(self, new_pos):
        for wall in WALLS:
            if self.intersects_wall(self.pos, new_pos, wall[0], wall[1]):
                return True
        return False

    def intersects_wall(self, p1, p2, w1, w2):
        def ccw(A, B, C):
            return (C.y - A.y) * (B.x - A.x) > (B.y - A.y) * (C.x - A.x)

        return ccw(p1, w1, w2) != ccw(p2, w1, w2) and ccw(p1, p2, w1) != ccw(p1, p2, w2)
