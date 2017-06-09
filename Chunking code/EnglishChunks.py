#This code forms chunks of english on the output of Stanford English Consituency parser

import codecs

for k in range(0,16):
    f=codecs.open("/home/akanksha/Desktop/Sem_Project/stanford-parser-full-2015-12-09/output/output"+str(k)+".txt",encoding='utf-8')
    w=codecs.open("/home/akanksha/Desktop/Sem_Project/stanford-parser-full-2015-12-09/output0/output"+str(k)+".txt","w",encoding='utf-8')

    strs=''
    parse=0
    i=0
    for lines in f.readlines():
        if '(ROOT' in lines:
            parse=1
            if i>1:
                w.write('\n')
            if i!=0:
                w.write(strs)
                strs=''
            i=i+1
        elif parse==1:
            data=lines.split(' ')
            r=1
            m=''
            m+="{{ "
            for d in data:
                if ')' in d:
                    m+=d[:d.index(')')]+' '
                    r=0
            m+=" }}"
            if r==0:
                strs+=m
    if strs!='':
        w.write('\n')
        w.write(strs)
