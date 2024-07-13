import matplotlib.pyplot as plt
import numpy as np
import time
from django.template.defaultfilters import center
np.set_printoptions(threshold=np.inf)
def loadDataSet(fileName):
    dataMat=[]
    fr=open(fileName)
    for line in fr.readlines():
        curLine=line.strip().split(' ')
        fltLine=map(float,curLine)
        dataMat.append([i for i in fltLine])
    return dataMat

def distEclud(vecA,vecB):
    return np.sqrt(np.sum(np.power(vecA-vecB,2)))

def randCent(dataSet,k):
    n=np.shape(dataSet)[1]
    centroids=np.mat(np.zeros((k,n)))
    for j in range(n):
        minJ=min(dataSet[:,j])
        rangeJ=float(max(dataSet[:,j])-minJ)
        centroids[:,j]=minJ+rangeJ*np.random.rand(k,1)
    return centroids

def kMeans(dataSet,k):
    m=np.shape(dataSet)[0]
    clusterAssment=np.mat(np.zeros((m,2)))
    centroids=randCent(dataSet, k)
    clusterChanged=True
    while clusterChanged:
        clusterChanged=False
        for i in range(m):
            minDist=np.inf
            minIndex=-1
            for j in range(k):
                distJI=distEclud(centroids[j,:], dataSet[i,:])
                if distJI < minDist:
                    minDist=distJI;minIndex=j
            if  clusterAssment[i,0] != minIndex:
                clusterChanged=True
            clusterAssment[i,:]=minIndex,minDist**2
        for cent in range(k):
            ptsInClust=dataSet[np.nonzero(clusterAssment[:,0].A == cent)[0]]
            centroids[cent,:]=np.mean(ptsInClust, axis=0)
    return centroids,clusterAssment
def showImage(dataSet,center,label):
    c=['black','dimgray','silver','lightcoral','red','indianred','sienna','sandybrown','peachpuff','goldenrod','gold','darkkhaki','olive','yellow','darkolivegreen','lightcyan','cyan','lightblue','slategray','navy','blueviolet','fuchsia','orange','lawngreen','mediumslateblue','slategrey','violet','purple','chocolate','linen']
    n=np.shape(dataSet)[0]
    for i in range(30):
        x=[]
        y=[]
        for j in range(n):
            if label[j]==i:
                x.append(dataSet[j,0])
                y.append(dataSet[j,1])
        plt.scatter(x,y,s=40,c=c[i])
    center=center.A
    plt.scatter(center[:,0],center[:,1],c='m',marker='p',s=200)
    plt.show()
if __name__ == '__main__':
    startTime=time.clock()
    dataSet=loadDataSet("E:/典故/计算相似度/yuliao-11111.txt")
    fileout = open('jieguo2.txt','w',encoding='utf-8')
    dataSet=np.array(dataSet)
    print(dataSet)
    center,cluster=kMeans(dataSet, 31)
    print(center)
    endTime=time.clock()
    print(endTime-startTime)
    print(cluster)
    fileout.write(str(cluster))
    showImage(dataSet, center, cluster[:,0])
