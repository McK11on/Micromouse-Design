# This file is in charge of solving the maze by the DFS (Deep First Search) method
# ------------------------------------------------------------------------------------------------------------ #
from pyamaze import maze,agent,textLabel,COLOR


# SearchAlgorithm: DFS
def DFS(m,start=None):
    if start is None:
        start=(m.rows,m.cols)
    explored=[start]
    frontier=[start]
    dfsPath={}
    dSeacrh=[]
    while len(frontier)>0:
        currCell=frontier.pop()
        dSeacrh.append(currCell)
        if currCell==m._goal:
            break
        poss=0
        for d in 'ESNW':
            if m.maze_map[currCell][d]==True:
                if d =='E':
                    child=(currCell[0],currCell[1]+1)
                if d =='W':
                    child=(currCell[0],currCell[1]-1)
                if d =='N':
                    child=(currCell[0]-1,currCell[1])
                if d =='S':
                    child=(currCell[0]+1,currCell[1])
                if child in explored:
                    continue
                poss+=1
                explored.append(child)
                frontier.append(child)
                dfsPath[child]=currCell
        if poss>1:
            m.markCells.append(currCell)
    fwdPath={}
    cell=m._goal
    while cell!=start:
        fwdPath[dfsPath[cell]]=cell
        cell=dfsPath[cell]
    return dSeacrh,dfsPath,fwdPath


if __name__=='__main__':
    m=maze(10,10) # Change to any size
    
    ini_cell= (1,3) # Start Cell
    goal_cell = (10,10) # Goal Cell

    # Configuring the maze
    m.CreateMaze(goal_cell[0],goal_cell[1],loopPercent=40,loadMaze="testingMaze.csv") 

    # DFS algorithm
    dSeacrh,dfsPath,fwdPath=DFS(m,ini_cell) 

    # Agents
    a=agent(m,ini_cell[0],ini_cell[1],goal=goal_cell,footprints=True,shape='square',color=COLOR.green) # Search agent
    b=agent(m,goal_cell[0],goal_cell[1],goal=ini_cell,footprints=True,filled=True) # Return agent
    c=agent(m,ini_cell[0],ini_cell[1],shape='arrow',color=COLOR.yellow) # Forward agent


    m.tracePath({a:dSeacrh},showMarked=True,delay=300) # Show the path of the agent
    m.tracePath({b:dfsPath},delay=100) # Show the path of the return agent
    m.tracePath({c:fwdPath},delay=200) # Show the path of the forward agent

    l=textLabel(m,'DFS Final Path Length',len(fwdPath)+1)
    l=textLabel(m,'DFS Search Length',len(dSeacrh))

    m.run()

