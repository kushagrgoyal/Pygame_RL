# Pygame_RL

The initial code for the Pygame grid setup is heavily inspired from @techwithtim 's https://github.com/techwithtim/A-Path-Finding-Visualization
I've changed the algorithm from A* to a Reinforcement Learning based method for finding the path. The RL method uses a Q-learning approach to find the path.

# Requirements
- Pygame
- Numpy

# How to run:
- Clone the repository
- Pygame_V_0.1.py is the file that needs to be run. Change the number of rows in the main function call to increase the grid size
- It will take longer and some training parameters will need to be adjusted for getting a proper legal path in complex maze pattern
- The first mouse click on running the code will set the START point
- The second mouse click will set the END point
- Third click onwards will be BARRIERS
- Right click can be used to delete and move any of the START, END & BARRIERS after the fact
- SPACEBAR to make the algorithm learn and the final path will be plotted in Green colour
