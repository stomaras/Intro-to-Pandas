import numpy as np
import pandas as pd

#we parse a list of values for each key 
d = {'A':[1,2,np.nan],'B':[5,np.nan,np.nan],'C':[1,2,3]}

df = pd.DataFrame(d)
print(df)
#Drop any row with Value Nan
dropp = df.dropna()
print(dropp)
#If you want to do the operation along the columns
column = df.dropna(axis=1)
print(column)
#If you want to hold some raws with Nan values you do the follow
#Hold all rows with at least 2 characters not null
thresh = df.dropna(thresh=2)
print(thresh)
############### Replace Missing Values #################################
fill = df.fillna(value='FILL VALUE')
print(fill)
a = df['A'].fillna(value=df['A'].mean())
print(a)
