f = open('popular.html') #open
raw = f.read() #read and store
byrow = raw.split('<tr>') #split by row
del byrow[0]
del byrow[0] #delete garbage rows

clean = {} #to send to file later

for row in byrow: #loop through each row
    category = row[row.find('">')+2 : row.find('</a>')] #extract categtory name
    urlpart = row[row.find('popular/')+8 : row.find('">')] #extract category identifier
    category = category.replace('&amp;', '&') #strings are immutable!
    clean[category] = urlpart
print clean
                   
