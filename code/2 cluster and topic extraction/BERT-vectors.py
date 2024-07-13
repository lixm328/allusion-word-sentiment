from bert_serving.client import BertClient
import numpy as np


class SimilarModel:
    def __init__(self):
        # ip默认为本地模式，如果bert服务部署在其他服务器上，修改为对应ip
        self.bert_client = BertClient()

    def close_bert(self):
        self.bert_client.close()

    def get_sentence_vec(self,sentence):
        '''
        根据bert获取句子向量
        :param sentence:
        :return:
        '''
        return self.bert_client.encode([sentence])[0]

    def cos_similar(self,sen_a_vec, sen_b_vec):
        '''
        计算两个句子的余弦相似度
        :param sen_a_vec:
        :param sen_b_vec:
        :return:
        '''
        vector_a = np.mat(sen_a_vec)
        vector_b = np.mat(sen_b_vec)
        num = float(vector_a * vector_b.T)
        denom = np.linalg.norm(vector_a) * np.linalg.norm(vector_b)
        cos = num / denom
        return cos

if __name__=='__main__':
    # 从候选集condinates 中选出与sentence_a 最相近的句子
    path = 'yuliao.txt'
    pathout = 'yuliao-11.txt'
    fw = open(pathout, 'w', encoding='utf-8')
    f = open(path, 'r', encoding='utf-8')
    bert_client = SimilarModel()
    lines = f.readlines()
    for i in range(len(lines)):
        sentence_a_vec = bert_client.get_sentence_vec(lines[i])
        print(sentence_a_vec)
        fw.write(str(i) + ' ' + str(sentence_a_vec))
