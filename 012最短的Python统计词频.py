#!/usr/bin/u/ubv/a python
# -*- coding:utf-8 -*-

from collections import Counter

def computeFrequencies(wordList):
    '''
    统计单词出现的频次
    :param wordList: 文本列表
    :return: 单词和其词频
    '''
    # 词频字典
    wordfrequencies = Counter(wordList)

    # 字典转换为列表
    masterList = list(wordfrequencies.keys())
    frequencies = list(wordfrequencies.values())

    return [masterList, frequencies]


words = [
    'aaa', 'bbb', 'ccc', 'ddd', 'ccc', 'aaa'
]
master, frequencies = computeFrequencies(words)
for word, frequence in zip(master, frequencies):
    print(word, frequence)