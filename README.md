# AI-project

# Summary:

A python project that starts with x agents and slowly improves through the use of neurons to more concistantly reach the goal dot.

# In-Depth:

This project uses the python library Tkinter to draw a series of dots that are controlled by neurons. At the start of the program, the dots pick random paths and follow them. These dots then use a fitness function and natural selection to create a new generation of dots that ideally should be better than the previous generation. A small amount of random mutation is also added to the dot's movements and breeding, to simulate an aspect of randomness.

# To-Do:
- Allow generations to run in the background.
  - This way we can fast forward n generations.
- Potentially improve wall creation system. For example, create a grid with coords. Maybe allow runtime creation of walls.
  - Using mouse to draw.
- Exploitation vs Exploration
  - Improve fitness function: Less hardcoded, more generalized (Don't really like "+ 0.1" just because it was a random choice.)
  - Improve selection/tournament style
- Improve the best dot display, a little hard to see in the crowd.