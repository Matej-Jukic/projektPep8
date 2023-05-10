def openFile(fileName):
    
    lines = []
        
    with open(fileName, "r+") as fp:
        print(fileName)
        lines = fp.readlines()
        lines=lookForImports(lines)
        print(lines)
        fp.seek(0)
        fp.truncate()
        fp.writelines(lines)
        
        


def lookForImports(lines):
    importLines = []
    splittedImports = []
    for line in lines:
        if line[0:6] == "import" or " import " in line:
            splittedImports = line[(line.index("import ")+7):].split(",")
            for element in splittedImports:
                
                if element[-1] == "\n":
                    print (element)
                    importLines.append(line[:line.index("import ")+7] 
                                       + element                                        
                                       )
                else:
                    importLines.append(line[:line.index("import ")+7] 
                                       + element
                                       + "\n")
            lines.remove(line)
    lines = importLines + lines    
    return lines

def removeSpacesRightAndLeftFromBrackets(lines):
    count = 0
    for line in lines:
        while "( " in line:
            line = line[:line.index("( ")+1] + line[line.index("( ")+2:]
        while "[ " in line:
            line = line[:line.index("[ ")+1] + line[line.index("[ ")+2:]
        while "{ " in line:
            line = line[:line.index("{ ")+1] + line[line.index("{ ")+2:]
        while " )" in line:
            line = line[:line.index(" )")] + line[line.index(" )")+1:]
        while " ]" in line:
            line = line[:line.index(" ]")] + line[line.index(" ]")+1:]
        while " }" in line:
            line = line[:line.index(" }")] + line[line.index(" }")+1:]
        count += 1

    lines[count] = line

def addSpacesArroundEqual
            
def lineDepth(lines):
    count = 0
    for line in lines:

        count += 1
