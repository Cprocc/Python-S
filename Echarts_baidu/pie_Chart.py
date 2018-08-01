import json
from pyecharts import Pie

f = open("../datas/pies.json")
data = json.load(f)
name = data['name']
sales = data['sales']
sales_volume = data['sales_volume']
pie = Pie("衣服清洗剂市场占比",title_pos='left',width=800)
pie.add("成 交 量",name,sales_volume,center=[25,50],is_random=True,radius=[30,75],rosetype='radius')
pie.add("销售额",name,sales,center=[75,50],is_random=True,radius=[30,75],rosetype='area',
        is_legend_show=False,is_label_show=True)
pie.show_config()
pie.render('D:/rose.html')