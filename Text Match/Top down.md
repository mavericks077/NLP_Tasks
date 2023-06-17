# 语义匹配

目标：判断两句话是否表达了相同的或相近的意思

## Representation-based Match

主要的思路如下，关键在于特征提取器 Encoder 的设计。

![img](https://pic3.zhimg.com/80/v2-7c98ed5bfbd64731cafeb49a5138cefe_720w.webp)

## Interaction - based Match

两个文本交互匹配本身就会产生有关匹配程度的信息，利用好这个信息可以提升模型的匹配能力。

![img](https://pic4.zhimg.com/80/v2-8ce500852048f695920a2efc6f7a5907_720w.webp)

## RBM中经典的算法

### 易于拓展和修改的DSSM



### 并行困难(耗时)但效果较好的Siamese-RNN



### 不断改进的TextCNN



### “大新闻” Transformer

## IBM中的经典算法

### 结构简单的ESIM



### 精心设计但颇为耗时的BiMPM

