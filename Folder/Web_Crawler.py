
#Web Crawler
import re
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd  

import math
from collections import Counter

import time

#Scraping using Beautiful Soup 
url = 'https://www.freetutorials.eu/investing-in-stocks-the-complete-course-11-hour-1/'
source = requests.get(url)

"""r = requests.get("http://example.com/", proxies=dict(
    http="http://proxy_user:proxy_pass@104.255.255.255:port",
))"""

plaintext = source.text
soup = bs(plaintext)

#Scraping the sites
def find():
    fw = open('src.txt','w')
    for link in soup.findAll('script'):    
        href = link.get('src')
        if href != None:
            fw.write(href)
            fw.write('\n')
        
    fw.close()
        
find()

#Crawler
flog = open('output.txt', 'r')
fog = open('arg.txt', 'r')

string = []
substr = []

for line in flog.readlines():
    string.append(line)
for line in fog.readlines():
    substr.append(line)

ad = []

#Classification into Ad/Non-Ad for attribute creation
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
    
    return ad

search()        


#Letter Digit Letter
def isLDL(s):
    strng = []
    strng.extend(s.split("/"))
    for i in strng:        
        if bool(re.match('^(?=.*[0-9])(?=.*[a-zA-Z]$)',str(i))):
            return 1
    return 0

#Digit Letter Digit         ----not implemented yet
def DLD(s):
    strng = []
    strng.extend(s.split("/"))
    for i in strng:        
        if bool(re.match('^(?=.*[0-9])(?=.*[a-zA-Z]$)',str(i))):
            return 1
    return 0

#Creating the Dataset
def create_ds():
    records = []  
    
    fr = open('output.txt','r')
    
    for line in fr.readlines():
        #line = line[:-2]
        
        lengthUrl = len(line)      #Length of the string
        special_char = re.findall('[!@#$%^&*(),.?":{}|<>]', str(line))      #Special Characters
                
        numberOfSpecial_chars = len(special_char)           #Number of special characters in the string
        isLetterDigitLetter = isLDL(str(line))              #letter digit letter
                
        #number of Dot Occurences
        dotOcc = 0
        for i in special_char:
            if i.__eq__("."):
                dotOcc += 1
                
        #Presence of Numeric Token
        if bool(re.match('^(?=.*[0-9])',line)):
            numToken = 1
        else:
            numToken = 0
        
        #Dash Count
        dashCount = 0
        for i in line:
            if i.__eq__("-"):
                dashCount += 1
            
        #Tokens and Entropy
        token = getTokens(str(line))
        entr = entropy(token)           #Alphabet Entropy
        
        #Max Token Length and Average Token Length
        maxLength = 0
        total = 0
        countToken = 0
        for item in token:
            lengthToken = len(item)
            
            #Average Token Length
            total += lengthToken
            countToken += 1
            avgLength = total/countToken
            
            #Max Token Length
            if lengthToken > maxLength:
                maxLength = lengthToken

        records.append((line,lengthUrl,numToken,special_char,numberOfSpecial_chars,dotOcc,dashCount,isLetterDigitLetter,token,entr, maxLength,avgLength,countToken))
        
    #Dataframe       
    df = pd.DataFrame(records, columns=['URL','Length-of-url','Numeric Token','Special_chars','Number of Special Characters','Number of Dot Occurences','Dash Count','LetterDigitLetter','Tokens','Alphabet Entropy','Max Token Length','Average Token Length','URL Token Count'])
    df['Ads_Class'] = ad
    
    #Converting to CSV
    df.to_csv('TempDataset.csv',index=False,encoding='utf-8')
    

create_ds()
    
    
#Alphabet Entropy
def entropy(s):
	p, lns = Counter(s), float(len(s))
	return -sum( count/lns * math.log(count/lns, 2) for count in p.values())

#Token Generator
def getTokens(input):
	tokensBySlash = str(input.encode('utf-8')).split('/')	#get tokens after splitting by slash
	allTokens = []
	for i in tokensBySlash:
		tokens = str(i).split('-')	#get tokens after splitting by dash
		tokensByDot = []
		for j in range(0,len(tokens)):
			tempTokens = str(tokens[j]).split('.')	#get tokens after splitting by dot
			tokensByDot = tokensByDot + tempTokens
		allTokens = allTokens + tokens + tokensByDot
	allTokens = list(set(allTokens))	#remove redundant tokens
	if 'com' in allTokens:
		allTokens.remove('com')	#removing .com since it occurs a lot of times and it should not be included in our features
	return allTokens

#Generating Tokens 
def generateTokens():
    global tokens
    tokens = []
    fr = open('output.txt','r')
    fw = open('token.txt','w')
    for line in fr.readlines():
        token = getTokens(str(line))
        fw.write(str(token))
        fw.write("\n")
        tokens.append(token)
        print(token)
    
#Debug   
def abc():
    tokens = []
    generateTokens()
    print(tokens)

abc()         
generateTokens()         

print(tokens)
#End of Debug


#TokenLength
def tokenLength():
    global lenList
    lenList = []
    fr = open('output.txt','r')
    for line in fr.readlines():
        token = getTokens(str(line))
        
        maxLength = 0
        count = 0
        total = 0
        
        for item in token:
            print(item)
            length = len(item)
            #Average Token Length
            total += length 
            count += 1
            
            
            if length > maxLength:
                maxLength = length
        
        print(count)
        avgLength = total/count
        print(avgLength)
        #Debug
        #print(maxLength)
        
        lenList.append(maxLength)
    return lenList
        
                
tokenLength() 


#Numeric Tokens
name = "as-f--a-skn"
if bool(re.match('^(?=.*[0-9])',name)):
    print("done")
else:
    print("not done")
            
#Dash Count
var = 0
for i in name:
            if i.__eq__("-"):
                var += 1   
print(var)


#Length of String
fr = open('output.txt','r')
for line in fr.readlines():
    print(len(line))



#Crawling Alexa top sites
def init(url):
        global soup
        url = "https://" + url
        source = requests.get(url)
        plaintext = source.text
        soup = bs(plaintext)
        
def iterate():
    fr = open('alexaSitesFinal.txt','r')
    fw = open('output1.txt','a')
    for line in fr.readlines():
        init(line)
                  
        for link in soup.findAll('script'):
            href = link.get('src')
            if href != None:
                fw.write(href)
                fw.write('\n')
            time.sleep(2)
    fr.close()
    fw.close()


iterate()


















