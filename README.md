# AI-project

# Summary:

A python project that starts with x agents and slowly improves through the use of neurons to more concistantly reach the goal dot.

# In-Depth:

This project uses the python library Tkinter to draw a series of dots that are controlled by neurons. At the start of the program, the dots pick random paths and follow them. These dots then use a fitness function and natural selection to create a new generation of dots that ideally should be better than the previous generation. A small amount of random mutation is also added to the dot's movements and breeding, to simulate an aspect of randomness.

# To-Do:
- Potentially improve wall creation system, or simplify. For example, add a grid with coords on tkinter.
- Exploitation vs Exploration
  - Improve fitness function
  - Improve selection/tournament style
- Should they be able to move off screen?
- Highlight the best dot with green!
- Allow generations to run in the background.
  - This way we can fast forward n generations.