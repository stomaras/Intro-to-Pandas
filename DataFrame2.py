import numpy as np
import pandas as pd
from numpy.random import randn

#What a Seed is just to make sure that we get the same random numbers 
np.random.seed(101)
df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
############################ Conditional Selection ######################

booldf = df > 0
print(booldf)
#Returns only the true Statemnts 
dfnew = df[df>0]
#print(dfnew)
w = df['W']>0
#print(w)
#print(df['W'])
k = df[df['W']>0][['Y','X']]
print(k)

L = df[(df['W']>0) & (df['Y']>1)]
print(L)
b = df.reset_index()
print(b)

################################### How to create a new series ##############
newind = 'CA NY GR CO ALB'.split()
print(newind)
#Result = ['CA','NY','GR','CO','ALB']
df['States'] = newind
print(df)
