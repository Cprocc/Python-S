from pyecharts import Scatter
scatter = Scatter('爱心',width=800,height=480)
data1,data2 = scatter.draw("D:/love.jpg")
scatter.add('Love',data1,data2)
scatter.render('D:\zxc_E\python-study\Echarts_baidu/scatter_love.html')