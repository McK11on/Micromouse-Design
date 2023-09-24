# This program creates a maze and solves it with the A* search algorithm

# To remember
# m = maze
# p = searchAlgo(m)
# a = agent(m)
# m.tracePath({a:p})

# ------------------------------------------------------------------------------------------------------------ #
import pyamaze as pm
# Create a maze
m = pm.maze(9,9)

# Setting the goal
goal_x,goal_y = 1,3

m.CreateMaze(goal_x,goal_y,loopPercent=70)

# Create an agent
a = pm.agent(m, footprints=True, filled=True)

# Create a label
l1 = pm.textLabel(m,"Toltal Cells",m.cols*m.rows)

# Create the trace path
m.tracePath({a: m.path},delay=100,showMarked=True)



m.run()