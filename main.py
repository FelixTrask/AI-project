import tkinter as tk
from population import Population
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Dots")
        self.canvas = tk.Canvas(self, width=SCREEN_WIDTH, height=SCREEN_HEIGHT, bg="black")
        self.canvas.pack()
        self.population = Population()
        self.epoch = 0
        self.update_canvas()

    def update_canvas(self):
        self.canvas.delete("all")
        self.population.update()
        self.population.draw(self.canvas)
        if not self.population.alive():
            print(f"Running Generation {self.epoch}...")
            self.population = self.population.natural_selection()
            print(f"Generation {self.epoch} finished.")
            self.epoch += 1
        self.after(10, self.update_canvas)


if __name__ == "__main__":
    app = App()
    app.mainloop()
