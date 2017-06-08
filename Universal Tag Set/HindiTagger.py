# -*- coding: utf-8 -*-

import sys
import codecs

g=[]
ng=[]

def replace(x,j):
	x=x.strip()
	dict={
		"NN" : "NOUN",
		"NNC" : "NOUN",
		"NST" : "NOUN",
		"NSTC" : "NOUN",
		"N_NN" : "NOUN",
		"N_NNP" : "NOUN",
		"N_NST" : "NOUN",
		"N_NP" : "NOUN",
		"NN_NNP" : "NOUN",
		"N_N_NNP" : "NOUN",
		"N_N" : "NOUN",
		"N_NNN" : "NOUN",
		"N_PP" : "NOUN",
		"n-nn" : "NOUN",
		"N_NNp" : "NOUN",
		"N-NN" : "NOUN",
		"\N_NNP" : "NOUN",
		"\N_NN" : "NOUN",
		"N_NNP-\RD_PUNC" : "NOUN",
		"JN_NN" : "NOUN",
		"N_NJN" : "NOUN",
		"N_NN[P" : "NOUN",
		"_NNP" : "NOUN",
		"_NN" : "NOUN",

		"NNP" : "PROPN",
		"NNPC" : "PROPN",
		
		"PRP" : "PRON",
		"PRPC" : "PRON",
		"PR__PRP" : "PRON",
		"PR_PRF" : "PRON",
		"PR_PRL" : "PRON",
		"PR_PRC" : "PRON",
		"PR_PRQ" : "PRON",
		"PR_PRI" : "PRON",
		"WQ" : "PRON",
		"PR_PRP" : "PRON",
		"PR" : "PRON",
		"PR_PRR" : "PRON",
		"PR_RPF" : "PRON",
		"PR_RPP" : "PRON",
		"PR_RPL" : "PRON",
		"RP__INTF" : "PRON",
		"PR_PRp" : "PRON",
		
		"JJ" : "ADJ",
		"JJC" : "ADJ",
		"QO" : "ADJ",
		"RDP" : "ADJ",
		"JJ" : "ADJ",
		"RBQT_QTC" : "ADJ",
		
		"INTF" : "ADV",
		"RB" : "ADV",
		"RBC" : "ADV",
		"RP_ING" : "ADV",
		"N_NEG" : "ADV",
		
		"PSP" : "ADP",
		"PPS" : "ADP",
		"RD_ECH" : "ADP",
		"PP" : "ADP",
		"SP" : "ADP",
		"SPP" : "ADP",

		"CC" : "CONJ",
		"CC_CCD" : "CCONJ",
		"CCC_CD" : "CCONJ",
		"C_CCD" : "CCONJ",

		"CC_CCS" : "SCONJ",
		"C_CCS" : "SCONJ",
		"CC_CS" : "SCONJ",

		"INJ" : "INTJ",
		
		"RP" : "PART",
		"NEG" : "PART",
		"RP_RPD" : "PART",
		"RP_INJ" : "PART",
		"RP_INTF" : "PART",
		"RP_NEG" : "PART",
		"RPD_RPD" : "PART",
		"RP_PRD" : "PART",
		"PR_PRD" : "PART",
		"RD_RPD" : "PART",
		"RP_ING" : "PART",
		"RP_RP" : "PART",
		
		"QC" : "NUM",
		"QCC" : "NUM",
		"QT" : "NUM",
		"QT_QTF" : "NUM",
		"QT_QTC" : "NUM",
		"QT_QTO" : "NUM",
		"QQTC" : "NUM",
		"QT-QTO" : "NUM",
		"QT_QT_QTC" : "NUM",
		"QT_TQC" : "NUM",
		"QT_TQC" : "NUM",
		"QT_QT" : "NUM",
		"QT_TC" : "NUM",
		
		"SYM" : "PUNCT",
		
		"UNK" : "X",
		"UNKC" : "X",
		
		"VAUX" : "AUX",
		"V_VAUX" : "AUX",
		"V_VAUX," : "AUX",
		u"V_VAUX।" : "AUX",
		"V_VVAUX" : "AUX",
		"V_AUX" : "AUX",
		"V_VAX" : "AUX",
		"V_V_VAUX" : "AUX",
		"V_VAX" : "AUX",
		"V_VUX" : "AUX",
		"_VAUX" : "AUX",
		u"V_VAUX।\RD_PUNC" : "AUX",
		
		"VM" : "VERB",
		"VMC" : "VERB",
		"V_VM" : "VERB",
		"V" : "VERB",
		"V_VMP" : "VERB",
		"VV_VM" : "VERB",
		"V_M" : "VERB",
		"V_VV" : "VERB",
		"V_V" : "VERB",
		"RP__NEG" : "VERB",

		"RD_PUNC" : ".",
		"RD" : ".",
		"RD_RDF" : ".",
		"RD_SYM" : ".",
		"RD_UNK" : ".",
		"RD_PUNCS" : ".",
		"RD_PUC" : ".",
		"RD_PUN" : ".",
		"RD__SYM" : ".",

		"QFC" : "DET",
		"DEM" : "DET",
		"QF" : "DET",
		"DM" : "DET",
		"DM_DMD" : "DET",
		"DD_DMD" : "DET",
		"DM_DMR" : "DET",
		"DM_DMQ" : "DET",
		"DM_DMI" : "DET",
		"DM_DM" : "DET",
		"D_DMD" : "DET",
		"DM_DMM" : "DET",
		"DM_DND" : "DET",
		"DR_DMD" : "DET"
		
	}


	if dict.has_key(x):
		if x not in ng:
			ng.append(x)
		return dict[x]
	else : 
		if x not in g:
			g.append(x)
		print x , j
		return x

def process(data,j):
	new=data.partition("\\")[2]
	new=replace(new,j)
	return data.partition("\\")[0]+data.partition("\\")[1]+new

count=int(sys.argv[1])
for i in range(count):
	j=i+1
	if j<10:
		f=codecs.open("../Hindi_English/hin_tourism_set0"+str(j)+".txt", "r", "utf-8")
		w=codecs.open("hin_tourism_parsedset0"+str(j)+".hi", "w", "utf-8")
	else:
		f=codecs.open("../Hindi_English/hin_tourism_set"+str(j)+".txt", "r", "utf-8")
		w=codecs.open("hin_tourism_parsedset"+str(j)+".hi", "w", "utf-8")
		
	for line in f:
		data=[]
		new_data=[]
		data=line.split(' ')
		for data_line in data:
			if "\\" in data_line:
				new_data.append(process(data_line,j))
			else :
				new_data.append(data_line)
		w.write(" ".join(new_data)) 
		w.write("\n")

print len(ng)
print len(g)

'''for x in g:
	print x
'''
