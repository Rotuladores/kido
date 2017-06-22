#!/bin/bash

touch dictionary/bigrams.txt
python3 dict.py
python3 bigrams.py
rm dictionary/bigrams.txt
mv bigrams.txt dictionary/bigrams.txt
python3 dict.py
