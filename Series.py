import numpy as np
import pandas as pd
labels = ['a','b','c']
#print(labels)
my_data = [10,20,30]
#print(my_data)
arr = np.array(my_data)
#print(arr)
d = {'a':10, 'b':20, 'c':30}
#print(d)
df = pd.Series(data = my_data)
#print(df)
df1 = pd.Series(data=my_data,index=labels)
#print(df1)
#You do not have to say data equals or index equals you could say my data and then labels
#as such and you would also get a series in the same manner
#So you do not need to constantly specify that equals or index equals as long as
#you put them in the correct order
df2 = pd.Series(my_data,labels)
#print(df2)
#pass dictionary
df3 = pd.Series(d)
#print(df3)
df4 = pd.Series(data=labels)
#print(df4)
########################SOS###################################################
#So a series can actually hold pretty much almost any type of data object with python
#as it is data point so it can be strings and even more interesting than that
#you could say data equals and you could have actually passen built in function
#so i could say something like  some print Eliane and it is actually holding
#references to these built in functions as data points in this panda series
#holding different object types
df5 = pd.Series(data=[sum,print,len])
#print(df5)

#So key to using series is understanding its index in Pandas make use of these
#index names or numbers by allowing for very fast lookups of information and
#its works just like hash table or a dictionary .Now let's go in and see some
#examples of how we can grab information from a series in order to do this
############################# Example ##############################################

ser1 = pd.Series([1,2,3,4],['USA','Germany','USSR','Japan'])

#So these are kind of like World War II country name references with some values
#print(ser1)

ser2 = pd.Series([1,2,5,4],['USA','Germany','Italy','Japan'])
#print(ser2)
#So italy ids different here and has a different data point
k = ser1['USA']
#print(k)
#I passing string because index is String it depends on what data type is your actual data

ser = ser1 + ser2
print(ser)

#When you are performing operations with panda series integers converted to float
