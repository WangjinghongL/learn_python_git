import os
dirlist=[d for d in os.listdir('.')]
for dir in dirlist:
    print(dir)
    
dmap={'a':1,'b':2,'c':3,'d':4}

for k,v in dmap.items():
    print(k,'=',v)
    
l={'Hello','Love','And','Peace',666,7777}

def lower(s):
    if isinstance(s,str):
        return s.lower()
    else:
        return s
        

def upper(s):
    if isinstance(s,str):
        return s.upper()
    else :
        return s


lowerList=[lower(s) for s in l]

upperList=[upper(s) for s in l]

for s in lowerList:
    print (s)
    
    
for s in upperList:
    print(s)