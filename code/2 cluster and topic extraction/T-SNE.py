import numpy as np
from sklearn.manifold import TSNE
import pandas as pd


np.set_printoptions(threshold=np.inf)
"""将3维数据降维2维"""

# 4个3维的数据
data=[]
From_file = open('E:/典故/计算相似度/yuliao-1111.txt', 'r', encoding='utf-8')
To_file = open('E:/典故/计算相似度/yuliaos.txt', 'a+', encoding='utf-8')
lines = From_file.readlines()
for line in lines:
    line1 = line.split(' ')
    data1 = [float(x) for x in line1]
    #print(data)
    data.append(data1)
    #print(data)
    data2 = np.array(data)
    #print(data2)

# 嵌入空间的维度为2，即将数据降维成2维
ts = TSNE(n_components=2)
# 训练模型
result = ts.fit_transform(data)
# 打印结果
print(ts.embedding_)
To_file.write(str(ts.embedding_))

plt.sactter(ts.embedding_[:,0],ts.embedding_[:,1])
plt.show()