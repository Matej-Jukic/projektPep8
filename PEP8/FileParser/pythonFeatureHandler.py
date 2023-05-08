from . import FeatureClass

def detectToken(line):

    isFeature = False
    asyncDefToken = "async def "
    classToken = "class "
    defToken = "def "

    tokenArray = [asyncDefToken, classToken, defToken]

    for token in tokenArray:
        if (token in line[0:len(token)] or (" " + token) in line) and onlySpaceCharacters(line):
            isFeature = True
            break

    return isFeature

def onlySpaceCharacters(line):
        
    asyncDefToken = "async def "
    classToken = "class "
    defToken = "def "
    tokenArray = [asyncDefToken, classToken, defToken]
    tokenIndex = -1

    for token in tokenArray:
        tokenIndex = line.find(token)
        if(tokenIndex > -1):
            break

    if(tokenIndex>-1):
        #print("Usao")
        #print(line)
        for x in range(tokenIndex):
            if line[x] != " ":
                
                return False
        return True

    else: 
        return False   

def detectFunction(line):
    
    isFunction = False

    
    if "def " in line[0:4] or " def " in line:
        isFunction = True
        indentDepth = line.find("def")

    return isFunction

def detectClass(line):
    isClass = False
    if "class " in line[0:6] or " class " in line:
        isClass = True
    return isClass

def getFeatureName(line): 
    
    if "async def" in line[0:10] or " async def " in line:  
        if ":" in line[line.find("async def "):len(line)]:
            return line[line.find("async def")+10: line.find("(")]
        else:
            return ""

    if "def" in line[0:4] or " def " in line:  
        if ":" in line[line.find("def "):len(line)]:
            return line[line.find("def")+4: line.find("(")]
        else:
            return ""

    elif "class " in line[0:6] or " class " in line:
        if ":" in line[line.find("class "):len(line)]:
            if "(" in line[line.find("class "):line.find(":")]:
                return line[line.find("class")+6: line.find("(")]
            return line[line.find("class")+6: line.find(":")]
        else:
            return ""

    else:
        return ""

def getLineDepth(line):
    
    counter = 0

    for char in line:

        if char != " ":
            break
        counter += 1

    return counter

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

def tabToFourSpaces(lines):
    count = 0
    for line in lines:
        for char in line:
            if char == "\t":
                line = line[:line.index("\t")] + "    " + line[line.index("\t")+1:]
                lines[count] = line
        count += 1
    return lines



def openFile(fileName):
 
    if( fileName [ len(fileName)-3 : len(fileName) ] == ".py" ):
        
        with open(fileName, "r+") as fp:
            print(fileName)
            lines = fp.readlines()
            lines=lookForImports(lines)
            
            fp.seek(0)
            fp.truncate()
            fp.writelines(lines)
