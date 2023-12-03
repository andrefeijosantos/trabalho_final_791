from nltk import *
from nltk.corpus import *
import cld3
from langdetect import detect_langs
from spacy_langdetect import LanguageDetector
from spacy.language import Language
import spacy

import sys
import glob
import os

special = ['(; )']

@Language.factory('language_detector')
def language_detector(nlp, name):
    return LanguageDetector()

nlp = spacy.load('pt_core_news_sm')
nlp.add_pipe('language_detector', last=True)

def accept(sentence, g=3):
	# Verifica existência de tokens especiais.
    if "EMAIL" in sentence: return False
    if "URL" in sentence: return False
    if sum([1 for sp in special if sp in sentence]) > 0: return False

    # Verifica a probabilidade de ser português
    grams = sentence.split()
	
    prob, cnt = 0, 0
    for i in range(g-1, len(grams)):
        cnt+=1
        lang = nlp(" ".join(grams[i - (g-1) : i+1]))._.language

        # Como muitas vezes pt-br pode ser confundido com espanhol, é considerado espanhol, com um peso de 0.5.
        prob += (int(lang['language'] == 'pt') * lang['score']) + (int(lang['language'] == 'es') * lang['score']/2)

    # Se a probabilidade média dos 4-gramas for >= 60%, então ela é aceita (experimental)
    if prob/cnt < .60: return False

    return True

fin = open(sys.argv[1], "r")
new_file, i, cnt, total = "", 0, 0, 0

for line in fin:
    print(str(i)+"/1000")

    total += 1
    if accept(line): 
        new_file += line
        i += 1; cnt += 1

    if i == 1000:
        if len(glob.glob("Wiki/*")) < 10:
            fout = open("Wiki/wiki_000"+str(len(glob.glob("Wiki/*"))), "w")
        elif len(glob.glob("Wiki/*")) < 100:
            fout = open("Wiki/wiki_00"+str(len(glob.glob("Wiki/*"))), "w")
        elif len(glob.glob("Wiki/*")) < 1000:
            fout = open("Wiki/wiki_0"+str(len(glob.glob("Wiki/*"))), "w")
        else:
            fout = open("Wiki/wiki_"+str(len(glob.glob("Wiki/*"))), "w")
        fout.write(new_file); fout.close()
        new_file, i = "", 0

    os.system("clear")

if i != 0:
    if len(glob.glob("Wiki/*")) < 10:
        fout = open("Wiki/wiki_000"+str(len(glob.glob("Wiki/*"))), "w")
    elif len(glob.glob("Wiki/*")) < 100:
        fout = open("Wiki/wiki_00"+str(len(glob.glob("Wiki/*"))), "w")
    elif len(glob.glob("Wiki/*")) < 1000:
        fout = open("Wiki/wiki_0"+str(len(glob.glob("Wiki/*"))), "w")
    else:
        fout = open("Wiki/wiki_"+str(len(glob.glob("Wiki/*"))), "w")
    fout.write(new_file); fout.close()

fin.close()

fout = open("results.txt", "a")
fout.write(str(cnt) + " " + str(total) + "\n")
fout.close()