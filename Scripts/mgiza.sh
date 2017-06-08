#echo "Making simple corpus directory"

#mkdir corpus corpus/training
#cat ~/Desktop/Sem\ Project/Hindi_English/ilci/eng_tourism_set* |sed 's/\w\w*\t//'|sed 's/\\\w\w*//g'|sed 's/\\\W//g' > ~/corpus/training/ilci.en
#cat ~/Desktop/Sem\ Project/Hindi_English/ilci/hin_tourism_set* |sed 's/\w\w*\t//'|sed 's/[\\A-Z\_]//g'> ~/corpus/training/ilci.hi
#cat ~/Desktop/Sem\ Project/Hindi_English/health/eng_health_set* |sed 's/\w\w*\t//'|sed 's/\\\w\w*//g'|sed 's/\\\W//g' > ~/corpus/training/health.en
#cat ~/Desktop/Sem\ Project/Hindi_English/health/hin_health_set* |sed 's/\w\w*\t//'|sed 's/[\\A-Z\_]//g'> ~/corpus/training/health.hi

#cat ~/corpus/training/ilci.hi ~/corpus/training/health.hi ~/Desktop/Sem\ Project/Hindi_English/hindi\-english\-master/training.hi\-en.hi > ~/corpus/training/comR.hi
#cat ~/corpus/training/ilci.en ~/corpus/training/health.en ~/Desktop/Sem\ Project/Hindi_English/hindi\-english\-master/training.hi\-en.en > ~/corpus/training/comR.en


echo "Tokenizing"

~/mosesdecoder/scripts/tokenizer/tokenizer.perl -l en < ~/corpus/training/comR.en > ~/corpus/training/comR.tok.en
python ~/indic_nlp_library-master/src/indicnlp/normalize/indic_normalize.py ~/corpus/training/comR.hi ~/corpus/training/comR.norm.hi [True]
python ~/indic_nlp_library-master/src/indicnlp/tokenize/indic_tokenize.py ~/corpus/training/comR.norm.hi ~/corpus/training/comR.tok.hi hi

echo "Upper to lower"

cd ~/corpus/training
tr '[:upper:]' '[:lower:]' < comR.tok.en > comR.tok.low.en
mv comR.tok.hi  comR.tok.low.hi

echo "Finished preprocessing , starting creation of vocabulary, conccurrence and classes..."

~/mgiza/mgizapp/bin/mkcls -n10 -pcomR.tok.low.en -VcomR.tok.low.en.vcb.classes
~/mgiza/mgizapp/bin/mkcls -n10 -pcomR.tok.low.hi -VcomR.tok.low.hi.vcb.classes
~/mgiza/mgizapp/bin/plain2snt comR.tok.low.en comR.tok.low.hi
~/mgiza/mgizapp/bin/snt2cooc comR.tok.low.en_comR.tok.low.hi.cooc comR.tok.low.en.vcb comR.tok.low.hi.vcb comR.tok.low.en_comR.tok.low.hi.snt

echo "Finished creation ! Now we start , really :-)"

#cp ~/mgiza_config ~/corpus/training/

#echo "Starting alignment: en -> hi" > en.timelog

#date >> en.timelog
#mv mgiza_config configfile
~/Downloads/giza-pp-master/GIZA++-v2/GIZA++ mgiza_config

#echo "Finished alignment, starting merge of parts" >> en.timelog

#echo "Merging"
#date >> en.timelog
#for i in 0 1 2 3 4 5 6 7
#do
#    cat en_hi.dict.A3.final.part00${i} >> corpus_word_aligned_en_hi
#done

#echo "removing all files"
#rm en_hi.dict.A3.final.part*

#date >> en.timelog
#echo "End of process." >> en.timelog
