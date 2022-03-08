from copy import deepcopy

class Node:
    def __init__(self,state,parent,g,h):
        self.state = state
        self.parent = parent
        self.g = g
        self.h = h

def calculateH(current,goal):
    h = 0
    for r in range(len(current)):
        for c in range(len(current[r])):
            if(current[r][c]!=goal[r][c] and current[r][c]!='-'):
                h+=1
    return h

def findPosition(state):
    for r in range(len(state)):
        for c in range(len(state[r])):
            if(state[r][c]=='-'):
                return [r,c]

def filterMovements(position):
    movements = [0,1,2,3]
    if(position[0]==0):
        movements.remove(0)
    if(position[0]==2):
        movements.remove(1)
    if(position[1]==0):
        movements.remove(2)
    if(position[1]==2):
        movements.remove(3)
    return movements

def up(current,position,g,goal):
    child_state = deepcopy(current.state)
    child_state[position[0]][position[1]] = child_state[position[0]-1][position[1]]
    child_state[position[0]-1][position[1]] = '-'
    child = Node(child_state,current,g,calculateH(child_state, goal))

    return child

def down(current,position,g,goal):
    child_state = deepcopy(current.state)
    child_state[position[0]][position[1]] = child_state[position[0]+1][position[1]]
    child_state[position[0]+1][position[1]] = '-'
    child = Node(child_state,current,g,calculateH(child_state, goal))

    return child

def left(current,position,g,goal):
    child_state = deepcopy(current.state)
    child_state[position[0]][position[1]] = child_state[position[0]][position[1]-1]
    child_state[position[0]][position[1]-1] = '-'
    child = Node(child_state,current,g,calculateH(child_state, goal))

    return child

def right(current,position,g,goal):
    child_state = deepcopy(current.state)
    child_state[position[0]][position[1]] = child_state[position[0]][position[1]+1]
    child_state[position[0]][position[1]+1] = '-'
    child = Node(child_state,current,g,calculateH(child_state, goal))

    return child

def sortChilds(childs):
    for i in range(len(childs)-1):
        for j in range(0, len(childs)-i-1):
            if((childs[j].g + childs[j].h) < (childs[j+1].g + childs[j+1].h)):
                aux = childs[j+1]
                childs[j+1] = childs[j]
                childs[j] = aux

def findChilds(frontier,current,g,goal):
    position = findPosition(current.state)
    movements = filterMovements(position)
    childs = []
    for m in movements:
        if(m==0):
            childs.append(up(current,position,g,goal))
        elif(m==1):
            childs.append(down(current,position,g,goal))
        elif(m==2):
            childs.append(left(current,position,g,goal))
        elif(m==3):
            childs.append(right(current,position,g,goal))
    sortChilds(childs)
    for n in childs:
        frontier.append(n)

def visited(path, current):
    visited = False
    for n in path:
        if(n.state==current.state):
            visited = True
    return visited

def printState(current):
    for r in current.state:
        print(r)
    print("\ng: ",current.g)
    print("h: ",current.h)
    print("f: ",current.g+current.h)
    print("------")

root = [[8,5,1],[3,7,2],[6,4,'-']]
goal = [[1,2,3],[4,5,6],[7,8,'-']]


g=0
found = False
frontier = []
path = []
current = None
i=0

root = Node(root,None,0,calculateH(root,goal))
print("\nThis is the initial state:")
printState(root)
print("This is the goal state:")
for a in goal:
    print(a)
print("\nDo you want to continue?")
input()
frontier.append(root)

while not found and frontier:
    current = frontier.pop()
    if(not visited(path, current)):
        path.append(current)
        printState(current)
        g = current.g
        if(current.h == 0):
            found = True
            break
        findChilds(frontier,current,g+1,goal)
