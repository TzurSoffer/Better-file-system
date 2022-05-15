import os

class MakeFile():
    def __init__(self, file):
        self.file = file
        try:
            with open(self.file, "r"):
                pass
        except:
            with open(self.file,"w"):
                pass
    def cls(self):
        with open(self.file,"w"):
            pass

    def clear(self):
        with open(self.file,"w"):
            pass

    def read(self):
        with open(self.file,"r") as f:
            return(f.read())
        
    def write(self, writing):
        with open(self.file,"w") as f:
            f.write(writing)

    def append(self, writing):
        with open(self.file,"a") as f:
            f.write(writing)

    def newLine(self, writing):
        self.append("\n"+writing)

    def getLine(self, line):
        f = self.read()
        lines = f.split("\n")
        return(lines[line-1])

    def readLine(self, line):
        self.getLine(line)

    def changeLine(self, line, newLine):
        f = self.read()
        lines = f.split("\n")
        lines[line-1] = newLine
        linesNew = "" 
        for l in range(len(lines)):
            linesNew += str(lines[l])+"\n"
        self.write(linesNew)

class MakeFolder():
    def __init__(self, name, basePath = ""):
        self.path = str(basePath)+str(name)
        self.name = name
        self.basePath = basePath
        if not os.path.exists(self.path):
            os.mkdir(self.path)

    def createPath(self):
        self.path = self.basePath+self.name

    def removeFolder(self):
        if os.path.exists(self.path):
            os.rmdir(self.path)
        else:
            print("folder dosn't exist")

    def changeFolder(self, newName, newBasePath = ""):
        self.path = str(newBasePath+newName)
        self.basePath= newBasePath
        self.name = newName
        if not os.path.exists(self.path):
            os.mkdir(self.path)
        else:
            pass


    def rename(self, newName):
        try:
            if not os.path.exists(self.basePath+newName):
                os.rename(self.path, (self.basePath+newName))
                self.name = newName
                self.createPath()
            else:
                print("folder already created")
        except:
            print("error in renaming")
        
        
        

if __name__ == "__main__":
    pass




