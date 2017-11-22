import urllib2
import json

#f = open("topcategories.txt")
#catdict = f.read()

catdict = {}
with open("topcategories.txt") as f:
    for line in f:
       (key, val) = line.split(",")
       catdict[key] = val

def questiondict(cat):
    retdict = {}
    if cat not in catdict:
        print "error"
        return
    print catdict
    url = "http://www.jservice.io/api/category?id=" + str(catdict[cat])
    uResp = urllib2.urlopen( url )
    raw = uResp.read()
    dat = json.loads(raw)
    clues = dat["clues"]
    
    x=0
    i=1
    while i < 6:
        if clues[x]["values"] == i*100:
            retdict[i*100] = [ clues[x]["question"], clues[x]["answer"] ]
            i += 1
            x = -1
        if x >= len(clues):
            i += 1
            x = -1
        x += 1
    return retdict
print questiondict('History')
        
