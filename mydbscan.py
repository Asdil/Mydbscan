import numpy as np
from scipy.spatial import distance
import random
import matplotlib.pyplot as plt
def inite(data):
    lab=data[:, -1]#获取类标签
    data = data[:, 0:-1]  #获取数据
    return data,lab
def selectStar(leastNumber):
    lenth=range(0,len(leastNumber))              #生成索引
    starID=random.sample(lenth,1)[0]       #在索引中随机选一个数
    starID=leastNumber[starID]   #获得该数在data索引中的值
    return starID              #返回类簇初始点，剩余样本
def checkCenter(data,starID,eps,minPts):
    starIDPoint=np.array([data[starID,:]])                  #data[starID,:]值形如[2 3],np.array([data[starID,:]]) 形如[[2 3]]
    distanceMatrix=distance.cdist(data,starIDPoint)         #得到距离矩阵
    neiborIndex=np.where(distanceMatrix<=eps)[0]               #找到半径内的样本
    neiborIndex=list(neiborIndex)                          #变为list方便删除自身
    del neiborIndex[neiborIndex.index(starID)]             #删除自身
    isCenter=False                                         #是否为中心点
    if (len(neiborIndex)>=minPts):
        isCenter=True
    return isCenter,neiborIndex

def clustering(data,eps,minPts):
    temp1=1
    data,lab=inite(data)
    dataNumber=data.shape[0]            #样本个数
    preClass=list(np.zeros(dataNumber))   #预测结果
    leastNumber=list(range(0,dataNumber))     #剩余样本数
    classType=1                                 #类簇种类
    while (len(leastNumber)>0):
        newseeds=[]
        isNewClass=True
        starID = selectStar(leastNumber)  # 选择初始样本
        if temp1==1:
            starID=36
            temp1=0
        seeds = [starID]  # 添加到seeds数组
        while (len(seeds)>0):
            for i in range(0, len(seeds[:])):
                head = seeds[0]  # 依次取出头元素
                del seeds[0]  # 删除头元素
                del leastNumber[leastNumber.index(head)]  # 丛剩余中删除钙元素
                isCenter, neiborIndex = checkCenter(data, head, eps, minPts)
                if isCenter:
                    preClass[head] = classType
                    newseeds.extend(neiborIndex)
                    isNewClass = False
                elif isNewClass:
                    preClass[head] = -1
                    break
                else:
                    preClass[head] = classType
            newseeds = list(set(newseeds))
            newseeds = list(set(leastNumber).intersection(set(newseeds)))
            seeds=newseeds[:]
            newseeds=[]
        classType+=1
    return preClass





