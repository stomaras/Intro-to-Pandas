import numpy as np
import pandas as pd
from numpy.random import randn

#What a Seed is just to make sure that we get the same random numbers 
np.random.seed(10)
df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
#print(df)
#Each of these columns is actually just a panda's series So w is a pandas series
#as well as XY and Z and they all share a common index and that's basically all
#Data frame is a bunch of series that share an index
serieW = df['W']
#print(serieW)
#type(df['W'])
        #pandas.core.series.Series
#type(df)
        #pandas.core.frame.DataFrame
k = df.W
#print(k)

l = df[['W','Z']]
#print(l)

#We will create a new column with this way
df['new'] = df['W'] + df['Y']
print(df)

#if i actually want to refer to the columns i need to specify access is equal to
#1 and then it will drop

#Wrong ->>  df.drop('new')

dfnew = df.drop('new',axis=1)
print(dfnew)

shape = df.shape
print(shape)

#################################### SELECT ROWS #############################



row1 = df.loc['A']
print(row1)
    

row2 = df.iloc[0]
print(row2)

subset = df.loc['B','Y']
print(subset)

subset2 = df.loc[['A','B'],['W','Y']]
print(subset2)
