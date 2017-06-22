#!/bin/bash

#clean old files
rm dictionary/bigrams.txt
rm dictionary/smart_wordsen_bigram.dat

#recreate dictionary
touch dictionary/bigrams.txt
python3 dict.py
python3 bigrams.py
rm dictionary/bigrams.txt
mv bigrams.txt dictionary/bigrams.txt
rm dictionary/smart_wordsen_bigram.dat
python3 dict.py
