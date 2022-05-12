

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

    def changeLine(self, line, newLine):
        f = self.read()
        lines = f.split("\n")
        lines[line-1] = newLine
        linesNew = "" 
        for l in range(len(lines)):
            linesNew += str(lines[l])+"\n"
        self.write(linesNew)
        

if __name__ == "__main__":


