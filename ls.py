#import sys
import os

def getname(path):
    if os.path.isdir(path):
        filder = os.listdir(path)
        return filder

    else:
        print("wrong path")
        exit()