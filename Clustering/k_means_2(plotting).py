import matplotlib.pyplot as plt
import pandas as pd
#import numpy as np
from sklearn.cluster import KMeans

similar_student_list=[]
df=pd.read_excel('Dataset.xlsx')
df['Label']=df['English']*0
n=len(df['Name'])
kmeans=KMeans(n_clusters=4)
kmeans.fit(df[['Math','English']])
df['Label']=kmeans.predict(df[['Math','English']])
centroids=kmeans.cluster_centers_
colmap={1:'r',2:'g',3:'b',4:'black'}
fig=plt.figure(figsize=(8,8))
colors=map(lambda x: colmap[x+1],df['Label'])
color1=list(colors)
plt.scatter(df['Math'],df['English'],color=color1,alpha=0.5,edgecolor='k')
plt.xlabel('Maths')
plt.ylabel('English')
for idx ,centroid in enumerate(centroids):
    plt.scatter(*centroid,color=colmap[idx+1])
plt.xlim(0,12)
plt.ylim(0,12)
plt.show()
