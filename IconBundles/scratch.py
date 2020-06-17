import os
import sys
filelist = os.listdir()
path = os.path.abspath('.')

n=0
for i in filelist:
    old = path+os.sep+filelist[n]
    new = old
    m=0
    new = new.replace('_','.')
    os.rename(old,new)
    print(old,"--->",new)
    n+=1
