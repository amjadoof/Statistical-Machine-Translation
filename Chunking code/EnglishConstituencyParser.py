#This code runs English Consitituency parser on input file https://nlp.stanford.edu/software/lex-parser.shtml

import sys
import codecs
import subprocess

f=codecs.open("ilci.en")

i=0
j=0
w=codecs.open("output"+str(j)+".txt","w", "utf-8")
for lines in f.readlines():
	i=i+1
	#print i
	if i>1000:
		i=0
		j=j+1
		w=codecs.open("output"+str(j)+".txt","w", "utf-8")
	r=codecs.open("input.txt","w", "utf-8")
	r.write(lines.decode('utf-8'))
	cmd=["./lexparser.sh"]
	subprocess.call(cmd,stdin=r,stdout=w)
