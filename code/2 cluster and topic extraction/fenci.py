import jieba
import jieba.posseg as pseg
file = open('1.txt','r',encoding='utf-8')    #要分词的文件\n",
file_result = open('1-1.txt','w',encoding='utf-8')  #分词后的文件\n",
#jieba.load_userdict('userdict.txt')     #用户自定义词典\n",
stopwords = {}.fromkeys([line.rstrip() for line in open('stopwords.txt',encoding='utf-8')])
for each_abstracts in file:
    segs = jieba.cut(each_abstracts)
    final = ''
    for seg in segs:
        if seg not in stopwords and  len(seg)>1:
            final = final + seg +' '
    final = final +'\n'
    file_result.write(final)