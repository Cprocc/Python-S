from pyecharts import Bar3D
import json

bar3d = Bar3D('3D 柱形图', width=1200, height=600)
f = open("../datas/bar3ds.json")
datas = json.load(f)
x_axis = datas['x_axis']
y_axis = datas['y_axis']
data = datas['data']
range_color = datas['range_color']

bar3d.add("",x_axis,y_axis,[[d[1],d[0],d[2]] for d in data],is_visualmap=True,visual_range=[0,20],visual_range_color=range_color)
bar3d.render('D:\zxc_E\python-study\Echarts_baidu/bar3d.html')