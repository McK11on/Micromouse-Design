# This program creates a maze and solves it 

# To remember
# m = maze
# p = searchAlgo(m)
# a = agent(m)
# m.tracePath({a:p})

# ------------------------------------------------------------------------------------------------------------ #
import pyamaze as pm
# Configuring the maze
m = pm.maze(9,9)

# Setting the goal
goal_x,goal_y = 1,3
# Create the maze
m.CreateMaze(goal_x,goal_y,loopPercent=90)

# Create an agent
a = pm.agent(m, footprints=True, filled=True)

# Create a label
l1 = pm.textLabel(m,"Toltal Cells",m.cols*m.rows)

# Create the trace path
m.tracePath({a: m.path},delay=100)

m.run()