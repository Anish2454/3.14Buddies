import urllib2
import json

def getKey():
    f = open("gettyKey.txt")
    key = f.read()
    return key[:-1] #Removes Newline

print getKey()
