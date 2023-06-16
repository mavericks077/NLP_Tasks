import numpy as np
import codecs
import re
import jieba
from scipy import spatial
import json

#句子切分，可以对中文文本进行分析
def get_sentence(corpus_dir, sentence_dir):
    re_han = re.compile(u"([\u4E00-\u9FD5a-zA-Z0-9]+)")  # the method of cutting text to sentence

    file_corpus = codecs.open(corpus_dir, 'r', encoding='utf-8')
    file_sentence = codecs.open(sentence_dir, 'w', encoding='utf-8')

    st = dict()
    for _, line in enumerate(file_corpus):
        line = line.strip()
        blocks = re_han.split(line)
        for blk in blocks:
            if re_han.match(blk) and len(blk) > 10:
                st[blk] = st.get(blk, 0) + 1

    st = sorted(st.items(), key=lambda x: x[1], reverse=True)
    for s in st[:10000]:
        file_sentence.write(s[0] + '\n')

    file_corpus.close()
    file_sentence.close()

#相似度计算，需理解计算过程
class ComputeSimilarity():
    def __init__(self, tf_idf_dir):
        self.tf_idf_dir = tf_idf_dir
        self.tf_idf = self.load_dict()
        self.vocab = list(self.tf_idf.keys())
        self.N = len(self.vocab)

    def load_dict(self):
        tf_idf = dict()
        with codecs.open(tf_idf_dir, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.split('\t')
                try:
                    assert len(line) == 2
                    tf_idf[line[0]] = float(line[1])
                except:
                    pass
        return tf_idf

    def similarity(self, s1, s2, use_idf=True):
        v1 = np.zeros((1, self.N))
        v2 = np.zeros((1, self.N))

        if use_idf:
            for w in jieba.cut(s1):
                if w in self.tf_idf:
                    v = self.tf_idf[w]
                    i = self.vocab.index(w)
                    v1[:, i] += v

            for w in jieba.cut(s2):
                if w in self.tf_idf:
                    v = self.tf_idf[w]
                    i = self.vocab.index(w)
                    v2[:, i] += v
        else:
            for w in jieba.cut(s1):
                if w in self.tf_idf:
                    i = self.vocab.index(w)
                    v1[:, i] = 1

            for w in jieba.cut(s2):
                if w in self.tf_idf:
                    i = self.vocab.index(w)
                    v2[:, i] = 1

        sim = 1 - spatial.distance.cosine(v1, v2)

        return sim

#利用样本进行测试
def test(tf_idf_dir, sentence_dir, test_dir):
    cs = ComputeSimilarity(tf_idf_dir)
    ssm = cs.similarity

    test_data = [u'临床表现及实验室检查即可做出诊断',
                 u'面条汤等容易消化吸收的食物为佳',
                 u'每天应该摄入足够的维生素A',
                 u'视患者情况逐渐恢复日常活动',
                 u'术前1天开始预防性运用广谱抗生素']

    model_list = ['use_idf', 'unuse_idf']

    file_sentence = codecs.open(sentence_dir, 'r', encoding='utf-8')
    train_data = file_sentence.readlines()

    for model in model_list:
        if model == 'use_idf':
            use_idf = True
        else:
            use_idf = False

        dataset = dict()
        result = dict()
        for s1 in test_data:
            dataset[s1] = dict()
            for s2 in train_data:
                s2 = s2.strip()
                if s1 != s2:
                    sim = ssm(s1, s2, use_idf=use_idf)
                    dataset[s1][s2] = dataset[s1].get(s2, 0) + sim
        for r in dataset:
            top = sorted(dataset[r].items(), key=lambda x: x[1], reverse=True)
            result[r] = top[0]

        with codecs.open(test_dir, 'a', encoding='utf-8') as f:
            f.write('--------------The result of %s method------------------\n ' % model)

            f.write(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=False))
            f.write('\n\n')

    file_sentence.close()

if __name__=="__main__":
    sentence_dir=r'C:\Users\lenovo\Desktop\code_py\TF-IDF\forum_test.txt'
    tf_idf_dir=r'C:\Users\lenovo\Desktop\code_py\TF-IDF\tf_idf.txt'
    test_dir=r'C:\Users\lenovo\Desktop\code_py\TF-IDF\test_result.txt'
    test(tf_idf_dir,sentence_dir,test_dir)