from dot import Dot
from constants import POPULATION_SIZE, GOAL, RADIUS
import random

class Population:
    def __init__(self):
        self.active = True
        self.pop = [Dot() for _ in range(POPULATION_SIZE)]

    def alive(self):
        return self.active

    def draw(self, canvas):
        for dot in self.pop:
            dot.draw(canvas)
        size = min(canvas.winfo_width(), canvas.winfo_height())
        goal_x = int(size * GOAL.x)
        goal_y = int(size * GOAL.y)
        radius = int(size * RADIUS)
        canvas.create_oval(goal_x - radius, goal_y - radius, goal_x + radius, goal_y + radius, fill='blue')

    def update(self):
        if self.active:
            self.active = False
            for dot in self.pop:
                dot.update()
                self.active |= dot.alive()

    def sum_fitness(self):
        return sum(dot.fitness() for dot in self.pop)

    def natural_selection(self):
        new_pop = []
        total_fitness = self.sum_fitness()
        for _ in range(len(self.pop)):
            fit_thres = random.uniform(0, total_fitness)
            running_fit = 0
            for dot in self.pop:
                running_fit += dot.fitness()
                if running_fit >= fit_thres:
                    new_pop.append(dot.mutate())
                    break
        return Population.from_parents(new_pop)

    @staticmethod
    def from_parents(parents):
        population = Population()
        population.pop = parents
        return population
