import json
from pyecharts import Line

f = open("../datas/lines.json")
data = json.load(f)
date = data['date']
sales1 = data['sales1']
sales2 = data['sales2']

line = Line("洗衣液月销售数量")
line.add("成交量", date,sales1,mark_point=['average','max','min'],mark_point_symbol='diamond', mark_point_textcolor='#40ff27')
line.add("销售额",date,sales2,mark_point=['max'],is_smooth=True,mark_line=['max','average'],mark_point_symbol='arrow',mark_line_symbolsize='40')
line.render('D:\zxc_E\python-study\Echarts_baidu/line.html')

linestack = Line("洗衣液月销售数量")
linestack.add("成交量", date,sales1,mark_point=['average','max','min'],mark_point_symbol='diamond', mark_point_textcolor='#40ff27')
linestack.add("销售额",date,sales2,mark_point=['max'],is_smooth=True,mark_line=['max','average'],mark_point_symbol='arrow',mark_line_symbolsize='40',is_stack=True,is_label_show=True)
linestack.render('D:\zxc_E\python-study\Echarts_baidu/linestack.html')

lineStep = Line("洗衣液月销售数量阶梯折线图")
lineStep.add("成交量", date,sales1,mark_point=['average','max','min'],is_step=True,is_label_show=True)
lineStep.add("销售额",date,sales2,mark_point=['max'],mark_line=['max','average'],is_step=True,is_label_show=True)
lineStep.render('D:\zxc_E\python-study\Echarts_baidu/lineStep.html')

linefill = Line("洗衣液月销售数量")
linefill.add("成交量", date,sales1,mark_point=['average','max','min'],mark_point_symbol='diamond', mark_point_textcolor='#40ff27',is_fill=True,area_opacity=0.4)
linefill.add("销售额",date,sales2,mark_point=['max'],is_smooth=True,mark_line=['max','average'],mark_point_symbol='arrow',mark_line_symbolsize='40',is_stack=True,is_label_show=True,is_fill=True,area_opacity=0.2,area_color='#000')
linefill.render('D:\zxc_E\python-study\Echarts_baidu/linefill.html')

