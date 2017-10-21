import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import distance
import scipy
import random
import sys
import math
sys.path.append('data/')
data = np.loadtxt("data/Aggregation.csv", skiprows=0, delimiter=',')  # usecols表示读取列数
import matplotlib.pyplot as plt
import  mydbscan
eps=2
minPts=1
repClass=mydbscan.clustering(data,eps,minPts)
plt.figure(figsize=(7, 7))
plt.scatter(data[:, 0], data[:, 1], c=repClass)
plt.show()

