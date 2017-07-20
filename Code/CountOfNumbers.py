import collections
import jieba
import numpy as numpy
from isIdealString import *

WordsToIndex = collections.defaultdict(int)

counter = 0
BigramCounter = collections.defaultdict(int)

for i in range(1,3):
    f = open("../Data/File%d.txt" % i)
    file = f.read()
    seg_list = jieba.cut(file, cut_all = False)

    for word in seg_list:
        if word not in WordsToIndex:
            WordsToIndex[word] = counter
            counter = counter + 1
        
        if counter == 1:
            PreviousWord = word
        else:
            if isIdealString(word, PreviousWord):
                BigramCounter[WordsToIndex[PreviousWord], WordsToIndex[word]] += 1
            PreviousWord = word
np.save('WordsToIndex_test.npy', WordsToIndex)
p.save('BigramCounter_test.npy', BigramCounter)