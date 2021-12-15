#import matplotlib.pyplot as plt
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

for i in range(n):
    df['Name'][i]=(str(df['Name'][i]).lower())

name=input('Enter Student Name: ')
name=(str(name).lower())

for i in range(n):
    compare_name=df['Name'][i]
    if compare_name==name:
        reference_label=df['Label'][i]


for i in range(n):
    compare_label=df['Label'][i]
    try:
        if reference_label==compare_label:
            similar_student_list.append(df['Name'][i])
    except:
        print('Error no name found')
        break


print('\nCalibieration Complete Similar Students listed Below:\n\n')
n_list=len(similar_student_list)
if n_list!=0:
    for i in range(n_list):
        print(similar_student_list[i])
else:
    print('No Similar Student')
