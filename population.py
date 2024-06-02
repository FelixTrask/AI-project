from dot import Dot
from constants import POPULATION_SIZE, GOAL, RADIUS, WALLS, WALL_COLOR, GREEN
import random

class Population:
    def __init__(self):
        self.active = True
        self.pop = [Dot() for _ in range(POPULATION_SIZE)]
        self.best_dot = None

    def alive(self):
        return self.active

    def draw(self, canvas):
        for dot in self.pop:
            dot.draw(canvas)
        size = min(canvas.winfo_width(), canvas.winfo_height())
        goal_x = int(size * GOAL.x)
        goal_y = int(size * GOAL.y)
        radius = int(size * RADIUS) + 2
        canvas.create_oval(goal_x - radius, goal_y - radius, goal_x + radius, goal_y + radius, fill='blue', outline='black')
        for wall in WALLS:
            start_x = int(size * wall[0].x)
            start_y = int(size * wall[0].y)
            end_x = int(size * wall[1].x)
            end_y = int(size * wall[1].y)
            canvas.create_line(start_x, start_y, end_x, end_y, fill=WALL_COLOR, width=2)
        if self.best_dot:
            self.best_dot.color = GREEN
            self.best_dot.draw(canvas)

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
        best_fitness = -float('inf')
        worst_fitness = float('inf')

        for dot in self.pop:
            fit = dot.fitness()
            if fit > best_fitness:
                best_fitness = fit
                self.best_dot = dot
            if fit < worst_fitness:
                worst_fitness = fit


        # Fill the rest of the population with mutations of selected dots
        for _ in range(len(self.pop) - 1):
            fit_thres = random.uniform(0, total_fitness)
            running_fit = 0
            for dot in self.pop:
                running_fit += dot.fitness()
                if running_fit >= fit_thres:
                    new_pop.append(dot.mutate())
                    break
                
        best_clone = Dot()
        best_clone.moves = self.best_dot.moves
        best_clone.color = GREEN
        # Clone the best dot and add it to the new population without mutation
        new_pop.append(best_clone)

        print(f"Best Fitness: {best_fitness}")
        print(f"Worst Fitness: {worst_fitness}")

        new_population = Population.from_parents(new_pop)
        new_population.best_dot = self.best_dot  # Carry over the best dot to the new population
        return new_population

    @staticmethod
    def from_parents(parents):
        population = Population()
        population.pop = parents
        return population
