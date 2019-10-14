import numpy as np
import pandas as pd


#We have a company column with three company codes
#Google , Microsoft, Facebook
#We have a person column with a bunch of unique people in it
#We have some Sales numbers 
data = {'Company':['GOOG','GOOG','MFST','MFST','FB','FB'],
        'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
        'Sales':[200,120,300,124,243,250]}
df = pd.DataFrame(data)
print(df)

#Group By Company
#Pandas ignores anything no numeric column 
byComp = df.groupby('Company')
print(byComp.mean())
print(byComp.sum().loc['FB'])

print(df.groupby('Company').sum().loc['FB'])

max = df.groupby('Company').max()
print(max)

describe = df.groupby('Company').describe()
print(describe)
