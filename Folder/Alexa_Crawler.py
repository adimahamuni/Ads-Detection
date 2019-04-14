import requests
import re
import pandas as pd
from bs4 import BeautifulSoup as bs
import time

class crawl:   
    
    def init(self, url):
        global soup
        url = "https://" + url
        source = requests.get(url)
        plaintext = source.text
        soup = bs(plaintext)
   
    def find_main(self):
        fw = open('sites.txt','w')
        links = soup.findAll('div', {'class':'DescriptionCell'})
        for link in links:    
            if link != None:
                fw.write(link.a.text)
                fw.write('\n')
        fw.close()
    
    def iterate(self):
        fr = open('sites.txt','r')
        fw = open('output.txt','a')
        for line in fr.readlines():
            self.init(line)
            
            for link in soup.findAll('script'):
                href = link.get('src')
                if href != None:
                    fw.write(href)
                    fw.write('\n')
                time.sleep(2)
        fr.close()
        fw.close()
        
    
    def create_ds():
        records = []
        fr = open('src.txt','r')
        for line in fr.readlines():
            length = len(line)
            special_char = re.findall('[!@#$%^&*(),.?":{}|<>]', str(line))
            #numberOfSpecial_chars = len(special_char)           #Number of special characters in the string
            #isLetterDigitLetter = isLDL(str(line))         
                  
            records.append((line,length,special_char))
            
        
        df = pd.DataFrame(records, columns=['URL','Length-of-url','Special_chars'])
        df.to_csv('dataset.csv',index=False,encoding='utf-8')
       
    def main(self):    
        self.init('www.alexa.com/topsites')
        self.find_main()
        self.iterate()
      
        
c = crawl()   

c.main()




#Using Proxy Server to hide IP address
"""r = requests.get("http://example.com/", proxies=dict(
    http="http://proxy_user:proxy_pass@104.255.255.255:port",
))"""



