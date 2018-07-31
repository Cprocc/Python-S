import pandas as pd
df = pd.read_csv("D:/taobao_data.csv")
df.head()

# 删除“商品”“卖家”两列，并根据数值字段求均值进行分组汇总，最后根据成交量均值降序排序
df_mean = df.drop(columns=['宝贝','卖家']).groupby('位置').mean().sort_values("成交量",ascending=False)
print(df_mean)
#drop(默认axis = 0)是删掉行,axis=1是删掉列
#groupby 汇总



# %matplotlib inline
# import matplotlib as mpl
# import matplotlib.pyplot as plt

mpl.style.use('ggplot')

fig, (ax1, ax2) = plt.subplots(1, 2, figsize = (12, 4))
df_mean.价格.plot(kind = 'barh',ax = ax1)
ax1.set_xlabel("ave prices of every provinces")
df_mean.成交量.plot(kind = 'barh',ax = ax2)
ax2.set_xlabel("ave nums of every provinces")
fig.tight_layout()

fig, axes = plt.subplots(2,2,figsize= (10,10))
s = df_mean.成交量
s.plot(ax = axes[0][0], kind = 'line', title="line")
s.plot(ax = axes[0][1], kind = 'bar', title="bar")
s.plot(ax = axes[1][0], kind = 'box', title="box")
s.plot(ax = axes[1][1], kind = 'pie', title="pie")
fig.tight_layout()

fig, ax = plt.subplots(1,1,figsize=(12,4))
ax.scatter(df.价格,df.成交量)
ax.set_xlabel("price")
ax.set_ylabel("nums")