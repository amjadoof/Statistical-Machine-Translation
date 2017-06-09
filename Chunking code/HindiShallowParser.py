#This script runs Hindi Shallow http://ltrc.iiit.ac.in/analyzer/hindi/ on one whole file

import sys
import codecs
import subprocess

#f=codecs.open("./input/full.hi")

i=0
j=0
w=codecs.open("./output/output"+str(j)+".txt","w", "utf-8")
f=codecs.open("./input/full"+str(j)+".txt")
for lines in f.readlines():
	r=codecs.open("input.txt","w", "utf-8")
	r.write(lines.decode('utf-8'))
	cmd=["shallow_parser_hin"]
	subprocess.call(cmd,stdin=r,stdout=w)
