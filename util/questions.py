import urllib2
import json
import random

def questiondict(cat):
    f = open("util/topcategories.txt")
    catdict = eval(f.read())

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
            retdict[i*100] = [ clues[x]["question"], clues[x]["answer"], True ]
            i += 1
            x = -1
        if x >= len(clues):
            i += 1
            x = -1
        x += 1
    return retdict

def get_categories():
    f = open("util/topcategories.txt")
    catdict = eval(f.read())
    categories = catdict.keys()
    random.shuffle(categories)
    return categories[:20]

if __name__ == '__main__':
    print get_categories()
    print questiondict('History') #test
