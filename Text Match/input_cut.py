import jieba
import  os

filename = 'C:\\Users\\lenovo\\Desktop\\algorithm_code_py\\Text Match\\input_info.txt'
f = open(filename,encoding="utf-8").read()
words = jieba.lcut_for_search(f)

print(words)
