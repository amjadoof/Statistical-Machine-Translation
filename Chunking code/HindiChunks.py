#This code forms phrases from the output of Hindi shallow parser.

import codecs

k=0
for k in range(17,18):
    parse=codecs.open("/home/akanksha/Desktop/Sem_Project/shallow-parser-hin-4.0.fc8/output/output"+str(k)+".txt",encoding='utf-8')
    w=codecs.open("/home/akanksha/Desktop/Sem_Project/shallow-parser-hin-4.0.fc8/output0/output"+str(k)+".txt","w",encoding='utf-8',)
    f=0
    i=0
    x=0
    strs=''
    for lines in parse.readlines():

        if '<Sentence' in lines:
            f=1
            if i!=0:
                w.write('\n')
            i=i+1
        elif '</Sentence>' in lines:
            w.write(strs)
            strs=''
            f=0
        if '((' in lines and f==1:
            x=1
            strs+=' {{'
            continue
        elif '))' in lines:
            strs+='}}'
            x=0
        
        if x==1:
            data=lines.split('\t')
            if data[1]=='(' or data[1]==')':
                continue
            else:
                #print(data[1],end=' ')
                strs+=data[1]+' '
