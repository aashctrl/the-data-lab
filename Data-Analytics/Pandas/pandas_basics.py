import pandas as pd

s1=pd.Series(data=[10,20,30,40], index=['Math','English','Hindi','Science']) 
print(s1) 
s2=pd.Series(data=[13,24,33,49], index=['Math','English','Hindi','Science']) 
print(s2) 

df1=pd.DataFrame(data={'Eng1':[10,20,30,40],'Hindi':[10,20,30,67]},index=['a','b','c','d'])
print(df1)
df2=pd.DataFrame(data={'col1':s1,'col2':s2})
print(df2) 

df=pd.read_csv('file_location') 
#High Level Understanding of Data 
df.head()
df.tail()
df.head(10)
df.tail(10)
df.dtypes 
df.info()
df.describe() 
#Low Level Understanding of Data 
df['column_name'].describe() 
df.column_name
