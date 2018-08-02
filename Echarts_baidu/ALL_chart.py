import json
from pyecharts import Pie,Bar,Funnel

f = open("../datas/pies.json")
data = json.load(f)
name = data['name']
sales = data['sales']
sales_volume = data['sales_volume']

pie = Pie("", width=800)
pie.add("", name,sales,is_label_show=True)
pie.render('D:\zxc_E\python-study\Echarts_baidu/pie.html')

funnel = Funnel("",width = 800)
funnel.add(" 成交量 ",name,sales_volume,is_label_show=True,label_pos='inside',label_text_color='#fff')
funnel.render('D:\zxc_E\python-study\Echarts_baidu/funnle.html')

bar = Bar("衣服清洗市场占比柱状图",width=800)
bar.add("成交量",name,sales_volume,center=[25,50],mark_point=['average'])
bar.add("销售额",name,sales,center=[25,50],mark_point=['max','min'])
# add函数里加上 is_stack = True  参数，实现堆叠效果
bar.render('D:\zxc_E\python-study\Echarts_baidu/bar.html')

bar1 = Bar("衣服清洗市场占比柱状图",width=800)
bar1.add("成交量",name,sales_volume,center=[25,50],mark_point=['average'])
bar1.add("销售额",name,sales,center=[25,50],mark_point=['max','min'],is_convert = True)
# add函数里加上 is_stack = True  参数，实现堆叠效果
bar1.render('D:\zxc_E\python-study\Echarts_baidu/bar_convert.html')