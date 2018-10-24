import pandas as pd
df = pd.read_csv("D:/taobao_data.csv")
df.head()

# 删除“商品”“卖家”两列，并根据数值字段求均值进行分组汇总，最后根据成交量均值降序排序
df_mean = df.drop(columns=['宝贝', '卖家']).groupby('位置').mean().sort_values("成交量",ascending=False)
print(df_mean)

# drop(默认axis = 0)是删掉行,axis=1是删掉列
# group_by 汇总
