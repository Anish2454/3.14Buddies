import urllib2
import urllib
import json

def getKey():
    f = open("util/gettyKey.txt")
    key = f.read()
    return key[:-1] #Removes Newline

def getImage(answer): #input the description of the desired image, which is the answer to the jeopardy question
    answer = urllib.quote(answer)
    url = urllib2.Request("https://api.gettyimages.com/v3/search/images?sort_order=most_popular&phrase=" + answer, headers={ 'Api-Key' : getKey()})
    print url
    uResp = urllib2.urlopen( url )
    contentsraw = uResp.read()
    dat = json.loads(contentsraw)
    if len(dat['images']) == 0:
        return "https://rlv.zcache.com/sad_smiley_face_classic_round_sticker-r364e0eed23d248b982dc0b717710afc1_v9wth_8byvr_324.jpg"
    else:
        return dat['images'][0]['display_sizes'][0]['uri'] #outputs a url to the image



