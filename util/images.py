import urllib2
import urllib
import json

def getKey():
    try:
        f = open("util/gettykeys.txt")
        key = f.read()
        return key.strip() #Removes Whitespace
    except Exception as e:
        print "****API KEY NOT FOUND******"
        return ""

def getImage(answer): #input the description of the desired image, which is the answer to the jeopardy question
    answer = urllib.quote(answer)
    key = getKey()
    #print key
    if key != "":
        url = urllib2.Request("https://api.gettyimages.com/v3/search/images?sort_order=most_popular&phrase=" + answer, headers={ 'Api-Key' : getKey()})
    else:
        return key
    print url
    uResp = urllib2.urlopen( url )
    contentsraw = uResp.read()
    dat = json.loads(contentsraw)
    if len(dat['images']) == 0:
        return "https://rlv.zcache.com/sad_smiley_face_classic_round_sticker-r364e0eed23d248b982dc0b717710afc1_v9wth_8byvr_324.jpg"
    else:
        return dat['images'][0]['display_sizes'][0]['uri'] #outputs a url to the image
