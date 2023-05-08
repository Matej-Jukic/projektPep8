import os
from . import pythonFeatureHandler as pFH


def walkAndExecute(startPoint):
    array=[]
    startPoint = backslashToSlash(startPoint) 
    
    exclude = set(['.git', '__pycache__'])
    rootDirFileArray = []
    for (root,dirs,files) in os.walk(startPoint, topdown=True):
            dirs[:] = [d for d in dirs if d not in exclude]
            files = [f for f in files if f.endswith('.py')]
            rootDirFileArray.append([root, dirs, files])
            print ("THIS IS ROOOT: "+ root)
            

    for element in rootDirFileArray:
        for file in element[2]:
            print(str(backslashToSlash(element[0]))+"/"+str(file))
            array.append(str(backslashToSlash(element[0]))+"/"+str(file))
            pFH.openFile(str(backslashToSlash(element[0]))+"/"+str(file))
    
    return array
    
def backslashToSlash(startPoint):
    counter = 0
    for char in startPoint:
        if char == "\\" or char == "":
            startPoint = startPoint[0:counter] + "/" + startPoint[counter + 1:len(startPoint)]
        counter += 1  
    return startPoint

