from pyecharts import Gauge

gauge = Gauge('目标完成率')
gauge.add('任务指标','完成率',80.2)
gauge.render('D:\zxc_E\python-study\Echarts_baidu/gauge.html')

from pyecharts import Liquid

liquid = Liquid("水球图")
liquid.add("liquid",[0.8])
liquid.render('D:\zxc_E\python-study\Echarts_baidu/liquid.html')