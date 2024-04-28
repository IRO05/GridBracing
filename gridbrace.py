    
rows = input("How many rows (1-5)? ")
columns = input("How many columns (1-5)? ")
rows = int(rows)
columns = int(columns)
gridList = []
columnList = []

def ID(num):
    match num:
        case 1:
            r = "A"
        case 2:
            r = "B"
        case 3:
            r = "C"
        case 4:
            r = "D"
        case 5:
            r = "E"
        case 6:
            r = "F"
        case 7:
            r = "G"
        case 8:
            r = "H"
        case 9:
            r = "I"
        case 10:
            r = "J"
        case 11:
            r = "K"
        case 12:
            r = "L"
        case 13:
            r = "M"
        case 14:
            r = "N"
        case 15:
            r = "O"
        case 16:
            r = "P"
        case 17:
            r = "Q"
        case 18:
            r = "R"
        case 19:
            r = "S"
        case 20:
            r = "T"
        case 21:
            r = "U"
        case 22:
            r = "V"
        case 23:
            r = "W"
        case 24:
            r = "X"
        case 24:
            r = "Y"
        case 25:
            r = "Z"
    return r

def letterToBrace(iden:int, bracList:list):
    for i in bracList:
        if iden == i:
            return "/"
        else:
            r = " "
    return r

def braceToMatrix(strBrace):
    if strBrace == "/":
        r = 1
    elif strBrace == " ":
        r = 0
    return r


def prompt():
    print("Please stay within the range: ")
    rows = input("How many rows (1-5)? ")
    columns = input("How many columns (1-5)? ")
    rows = int(rows)
    columns = int(columns)



class grid(object):
    def __init__(self, row, col):
        if (row < 6 and col < 6):
            row = int(row)
            col = int(col)
        
        else:
            prompt()
            
        self.row = int(row)
        self.col = int(col)
        self.dim = row * col
        
        self.ID = 1
    
    def show(self):
        gridface = ""
        currentRow = ""
        
        
        for r in range(self.row):
            

                
                for p in range(3):
                    
                    if p == 0:
                        currentRow += ",___,"*self.col
                    elif p == 1:
                        for c in range(self.col):
                            currentRow += "| " + ID(self.ID) + " |"
                            self.ID += 1
                    elif p == 2:
                        currentRow += ";___;"*self.col
                    gridface += currentRow + "\n"
                    currentRow = ""
        
        print(gridface)
    
    def brace(self):
        braceCount = int(input("How many braces would you like to add? "))
        braceList = []
        for b in range(braceCount):
            r = input("[" + str(b+1) + "]" + "Where would you like to place this brace? ").upper()
            
            braceList.append(r)
        
        self.ID = 1
        gridface = ""
        currentRow = ""
        
        
        for r in range(self.row):
            
                gridList.append([])
                
                for p in range(3):
                    
                    if p == 0:
                        currentRow += ",___,"*self.col
                    elif p == 1:
                        for c in range(self.col):
                            currentRow += "| " + letterToBrace(ID(self.ID), braceList) + " |"
                            gridList[r].append(braceToMatrix(letterToBrace(ID(self.ID), braceList)))
                            self.ID += 1
                    elif p == 2:
                        currentRow += ";___;"*self.col
                    gridface += currentRow + "\n"
                    currentRow = ""
        print(gridface)
            

class Point(object):
        
    def __init__(self, ID, neighborList):
        
        self.ID = ID
        self.neighborList = neighborList
        self.visited = False
    
    def getID(self):
        
        return self.ID
    
    def getList(self):
        
        return self.neighborList
    
    def visit(self):
        
        self.visited = True
        
    def unvisit(self):
        
        self.visited = False
        
    def addNeighbor(self, ID):
        
        self.neighborList.append(ID)
        
class graph(object):
        
    def __init__(self, pointList):
        
        self.pointList = pointList
        self.stack = []
        
    def dfs(self, node):
        
        for i in self.pointList:
            
            ID = i.getID()
            
            if ID == node:
                
                node = i
                
                break
                
        
        self.stack.append(node)
        
        while len(self.stack) > 0:
            
            currentNode = self.stack[0]
            currentList = currentNode.neighborList
            
            for i in currentList:
                
                ipoint = None
                
                for z in self.pointList:
                    
                    ID = z.getID()
                    
                    if ID == i:
                        
                        ipoint = z
                        break
            
                
                if ipoint != None and not ipoint.visited:
                    
                    self.stack.append(ipoint)
            
            currentNode.visit()
            self.stack.remove(currentNode)
        
        for i in self.pointList:
            
            if not i.visited:
                
                fullyVisited = False
                
                break
            else:
                
                fullyVisited = True
            
        if fullyVisited:
            
            print("Connected")
        else:
            
            print("Not connected")
                
def matrixTo(nestedList):
            
            pointList = []
            
            currentNode = 0
            
            
            for i in range(len(nestedList)):
                
                if i == 0:
                      
                    currentNode = Point("r0", [])
                      
                elif i == 1:
                    
                    currentNode = Point("r1", [])
                    
                elif i == 2:
                    
                    currentNode = Point("r2", [])
                    
                elif i == 3:
                    
                    currentNode = Point("r3", [])
                    
                elif i == 4:
                    
                    currentNode = Point("r4", [])
                
                
                
                for z in range(len(nestedList[i])):
                    
                    
                    
                    if nestedList[i][z] == 1:
                        
                        neighborID = "c" + str(z)
                        currentNode.addNeighbor(neighborID)
                        
    
                
                    pointList.append(currentNode)
                    
            return pointList    
                
                
    
    
        
            
    
    
            
          
g = grid(rows, columns)
g.show()
g.brace()
print(gridList)

g = graph(matrixTo(gridList))
g.dfs(g.pointList[0])
