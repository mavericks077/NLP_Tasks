# NLP_Tasks
This repository records my attempts in NLP field.
### 1 算法原理部分
  ##### TF-IDF算法：根据词汇的重要性赋予不同的权值，若某一词很少出现，则证明它作为关键字的可能性会更大。
  ##### TextRank算法：起源于Pagerank算法，根据连通图的原理，将权值通过节点分支个数进行划分。
  ##### LDA算法：涉及较为复杂的数学知识，如贝叶斯判据等，但 paddlehub 中已有集成好的库。
### 2 任务实现部分
本次的任务是通过用户画像对应的关键词，匹配输入的文本信息，给出它们之间的相似程度，并发送信息到匹配的用户。目前对于文本匹配在"Text Match"和"TextCNN"中, 发送验证在"Mail_Send"中，输入的用户画像为"User_Proflie", 要匹配的文本信息为"Input_info"。（读取文件的路径可能需要修改，这里用的绝对路径）
