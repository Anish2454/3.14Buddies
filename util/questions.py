import urllib2
import json
import random

f = open("util/topcategories.txt")
catdict = eval(f.read())

def questiondict(cat):
    retdict = {}
    if cat not in catdict:
        print "error"
        return
    url = "http://www.jservice.io/api/category?id=" + str(catdict[cat])
    uResp = urllib2.urlopen( url )
    raw = uResp.read()
    dat = json.loads(raw)
    clues = dat["clues"]
    random.shuffle(clues) # so the same questions aren't chosen each time

    x=0
    i=1
    while i < 6:
        if clues[x]["value"] == i*100:
            retdict[i*100] = [ clues[x]["question"], clues[x]["answer"] ]
            i += 1
            x = -1
        if x >= len(clues):
            i += 1
            x = -1
        x += 1
    return retdict
print questiondict('History') #test
