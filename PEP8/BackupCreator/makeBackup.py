import shutil
import os
import time
from FileParser.treeWalk import backslashToSlash

def createBackupFolder(path):
    # Create a unique name for the destination directory
    
    currentDir = os.path.split(path)[-1]   
    day=str(time.localtime().tm_mday)
    month=str(time.localtime().tm_mon)
    year=str(time.localtime().tm_year)
    hour=str(time.localtime().tm_hour)
    minute=str(time.localtime().tm_min)
    second=str(time.localtime().tm_sec)
    dateAndTime = (day + "_" 
                 + month + "_" 
                 + year + "_" 
                 + hour + "_" 
                 + minute + "_" 
                 + second)
    # Copy the directory to the destination
    path=backslashToSlash(path)
    newPath = path + "/../" + currentDir + "_copy_" + dateAndTime
    shutil.copytree(path, newPath)
    print(newPath)
    print(path)

