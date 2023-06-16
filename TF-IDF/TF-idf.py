from collections import  defaultdict
import math
import operator

#该情况仅能对英文文本切分
def loadDataSet():
    dataset = ["","",""]                #需要切分后再输入dataset
    classvec =[0, 1, 0, 1, 0, 1]
    return dataset, classvec

def feature_select(list_words):
    doc_freq = defaultdict(int)
    for word_list in list_words:
        for i in word_list:
            doc_freq[i] = doc_freq[i]+1

    word_tf = {}
    for i in doc_freq:
        word_tf[i] = doc_freq[i]/sum(doc_freq.values())

    doc_num = len(list_words)
    word_idf = {}
    word_doc = defaultdict(int)
    for i in doc_freq:
        for j in list_words:
            if i in j :
                word_doc = word_doc + 1
        for i in doc_freq:
            word_idf[i] = math.log(doc_num/(word_doc[i]+1))

    word_tf_idf = {}
    for i in doc_freq:
        word_tf_idf[i] = word_tf[i]*word_idf[i]

    dict_feature_select = sorted(word_tf_idf.items(), key=operator.itemgetter(1),reverse=True,)
    return dict_feature_select


if __name__ == '__main__':
    data_list, label_list = loadDataSet()
    features = feature_select(data_list)
    print(features)
    print(len(features))