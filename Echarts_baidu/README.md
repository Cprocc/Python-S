# Echarts &  pyecharts
## Echart
百度开发的开源可视化库
## pyecharts
python的一个用于生成Echarts图表的类库
### pyecharts的使用方法
1. `pip install pyecharts `
2. 图标大小及标题
    
    代码说明
     
     `Chart_name("Title", title_pos="left/right/center",height=,width)`
    
    Title表示图表标题，title_pos表示图表位置，height和width表示高度和宽度
3. 图表内容设置
    通过 ' add() ' 函数实现
    ' add("图表名"，数据集1，数据集2，位置，颜色，图形类型，图例格式，标签设置) '
    
    参数说明
        
    | 参数名称 | 参数作用 |
    |:---:|:---|
    | center | 指定饼图圆心的位置，第一个数值是x轴位置，第二个是y轴，单位是% |
    |radius|指定饼图半径范围，第一个数值是圆心，第二个是扇形|
    |visual_text_color| 指定文本颜色|
    |is_random|是否用随机配色|
    |rosetype|指定玫瑰图的图形类型|
    |is_legend_show|指定是否显示图例|
    |label_pos|指定标签的位置|
    |label_text_color|指定标签颜色|
    
4. 图表配置显示
    
    ` show_config() ` 方法
5. 图表输出
    
    ` render() ` 方法在制定目录下生成render.html文件
