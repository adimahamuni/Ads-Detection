flog = open('src.txt', 'r')
fog = open('arg.txt', 'r')

string = []
substr = []

for line in flog.readlines():
    string.append(line)
for line in fog.readlines():
    substr.append(line)
  
ad = []

def search():
    res = False
    for st in string:
        st = st[:-2]
        for sub in substr: 
            sub = sub[:-2]
            if sub in st: 
                res = True
                break
            else:
                res = False
        if res:
            ad.append("ad")
        else:
            ad.append("non-ad")
   
    if res:
        #ad.append("ad")
        print('res true')
    else: 
        #ad.append("non-ad")
        print('res false')
        

search()