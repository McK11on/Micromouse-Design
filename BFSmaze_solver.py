# This file is in charge of solving the maze by the BFS (Breadth First Search) method
# ------------------------------------------------------------------------------------------------------------ #
from pyamaze import maze,agent,textLabel,COLOR
from collections import deque


# SearchAlgorithm: BFS
def BFS(m,start=None):
    if start is None:
        start=(m.rows,m.cols)
    frontier = deque()
    frontier.append(start)
    bfsPath = {}
    explored = [start]
    bSearch=[]

    while len(frontier)>0:
        currCell=frontier.popleft()
        if currCell==m._goal:
            break
        for d in 'ESNW':
            if m.maze_map[currCell][d]==True:
                if d=='E':
                    childCell=(currCell[0],currCell[1]+1)
                elif d=='W':
                    childCell=(currCell[0],currCell[1]-1)
                elif d=='S':
                    childCell=(currCell[0]+1,currCell[1])
                elif d=='N':
                    childCell=(currCell[0]-1,currCell[1])
                if childCell in explored:
                    continue
                frontier.append(childCell)
                explored.append(childCell)
                bfsPath[childCell] = currCell
                bSearch.append(childCell)
    # print(f'{bfsPath}')
    fwdPath={}
    cell=m._goal
    while cell!=start:
        fwdPath[bfsPath[cell]]=cell
        cell=bfsPath[cell]
    return bSearch,bfsPath,fwdPath


if __name__=='__main__':
    # Configuring the maze
    m=maze(10,10)

    ini_cell= (1,1) # Start Cell
    goal_cell = (10,2) # Goal Cell

    m.CreateMaze(goal_cell[0],goal_cell[1],loopPercent=100)

    # BFS algorithm
    bSearch,bfsPath,fwdPath=BFS(m,ini_cell)

    # Agents
    a=agent(m,ini_cell[0],ini_cell[1],footprints=True,color=COLOR.green,shape='square') # Search agent
    c=agent(m,goal_cell[0],goal_cell[1],goal=(ini_cell),footprints=True,color=COLOR.cyan,shape='square',filled=True) # Return agent
    b=agent(m,ini_cell[0],ini_cell[1],color=COLOR.yellow,shape='arrow') # Forward agent

    # Trace the path
    m.tracePath({a:bSearch},showMarked=True,delay=100)
    m.tracePath({c:bfsPath},delay=100)
    m.tracePath({b:fwdPath},delay=100)

    m.run()