import pandas as pd
#从CSV中读取数据，还可以读取html,txt等格式的文件
# header: 指定第几行作为列名(忽略注解行)，如果没有指定列名，默认header=0; 如果指定了列名header=None
# names 指定列名，如果文件中不包含header的行，应该显性表示header=None

df = pd.read_csv("D:/taobao_data.csv", delimiter =',', encoding ="utf8", header = 0)
print (df)

# #向CSV中写数据
# df.to_csv("D:/taobao_data.csv",columns=['商品','价格',],index= False,header=True)

#输出第0-2行
rows = df[0:3]
print(rows)

#选取列
#cols.head()用于获取前五行
cols = df[['宝贝','价格']]
print(cols.head())

#块的选取
print(df.ix[0:3,['宝贝','价格']])

#创建一个新列
df['销售额'] = df['价格']*df['成交量']
print(df.head())

#根据条件筛选
print(df[(df['价格']<100)&(df['成交量']>10000)])





