import urllib2
import json

def getKey():
    f = open("gettyKey.txt")
    key = f.read()
    return key[:-1] #Removes Newline

def getImage(answer): #input the description of the desired image, which is the answer to the jeopardy question
    url = urllib2.Request("https://api.gettyimages.com/v3/search/images?sort_order=most_popular&phrase=" + answer, headers={ 'Api-Key' : getKey()})
    print url
    uResp = urllib2.urlopen( url )
    contentsraw = uResp.read()
    dat = json.loads(contentsraw)
    return dat['images'][0]['display_sizes'][0]['uri'] #outputs a url to the image
