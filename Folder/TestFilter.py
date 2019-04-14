
def Filter():
    
    fr = open('alexaSites1.txt', 'r')
    fw = open('alexaSitesFinal.txt','w')
    
    for line in fr.readlines():
        line = line.split(',')
        fw.write(line[1])
    
    
Filter()    