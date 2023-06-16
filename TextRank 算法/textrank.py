from textrank4zh import TextRank4Keyword, TextRank4Sentence
import  jieba.analyse
import  jieba
import pandas as pd
import numpy as np

def keywords_extraction(text):
    tr4w = TextRank4Keyword(allow_speech_tags=['n','nr','nrfg','ns','nt','nz'])
    tr4w.analyze(text = text, window=2, lower=True,vertex_source='all_filters',edge_source='no_stop_words',pagerank_config={'alpha':0.85})

    keywords = tr4w.get_keywords(num=6, word_min_len=2)
    return keywords

def keyphrases_extraction(text):
    tr4w = TextRank4Keyword()
    tr4w.analyze(text = text, window=2, lower=True,vertex_source='all_filters',edge_source='no_stop_words',pagerank_config={'alpha':0.85})

    keyphrases = tr4w.get_keyphrases(keywords_num=6, min_occur_num=1)
    return keyphrases

def keysentences_extraction(text):
    tr4s = TextRank4Sentence()
    tr4s.analyze(text, lower=True, source='all_filters')

    keysentence = tr4s.get_key_sentences(num=3, sentence_min_len=6)
    return keysentence

def keywords_textrank(text):
    keywords = jieba.analyse.textrank(text, topK=6)
    return keywords

if __name__ == "__main__":
    text = open('input_2.txt','r',encoding="utf-8").read()
    keywords = keywords_extraction(text)
    print(keywords)

    keyphrases = keyphrases_extraction(text)
    print(keyphrases)

    keysentences = keysentences_extraction(text)
    print(keysentences)



