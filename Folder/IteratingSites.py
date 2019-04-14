

import requests
from bs4 import BeautifulSoup as bs
  
class crawl:
    def iterate(self):
        fr = open('alexaSitesFinal.txt','r')
        fw = open('output1.txt','w')
        for line in fr.readlines():
            line = line.strip()
            url = "http://www." + line
            try:
                source = requests.get(url, timeout=1000)
                plaintext = source.text
                soup = bs(plaintext)
                for link in soup.findAll('script'):
                    href = link.get('src')
                    if href != None:
                       fw.write(href)
                       fw.write('\n')
            except requests.exceptions.ConnectionError:
                continue
                        
        fw.close()
        fr.close()
       
    def main(self):
        self.iterate()
      
        
c = crawl()   

c.main()