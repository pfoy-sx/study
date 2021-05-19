#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/10/19 14:25
# @Author  : Beam
# @Site    :
# @File    : demo_xlsxwriter.py
# @Software: PyCharm

import xlsxwriter

workbook = xlsxwriter.Workbook('chart.xlsx')  # 创建一个excel表
worksheet = workbook.add_worksheet()  # 创建一个工作表对象
chart = workbook.add_chart({'type': 'column'})  # 创建一个图形对象

title = [u'业务名称', u'星期一', u'星期二', u'星期三', u'星期四', u'星期五', u'星期六', u'星期日', u'平均流量']   #定义数据表头列表
buname = [u'PC站点', u'app', u'论坛', u'移动端', u'监控']    ##定义5个业务类型
data = [[100,127,211,123,185,164,134],[108,148,98,99,142,131,121],[241,211,222,199,244,216,228],[145,156,132,147,159,123,168],[148,139,128,146,175,185,148]]  #定义每个业务的7天数据流量，实际可以录入到CMDB然后序列化获取，看实际需求修改

format = workbook.add_format()   #定义format格式对象
format.set_border(1)              #定义format对象单元格边框加粗1像素

format_title = workbook.add_format()   #定义format_title格式对象
format_title.set_border(1)      #定义format_title对象单元格边框加粗1像素
format_title.set_bg_color('#cccccc')   #format_title对象单元格背景颜色设置为'#cccccc'
format_title.set_align('center')      #format_title对象单元格居中对齐
format_title.set_bold()               #format_title对象单元格内容加粗set_bold()是加粗方法

format_ave = workbook.add_format()    #创建format_ave格式对象
format_ave.set_border(1)
format_ave.set_bold()
format_ave.set_num_format('0.00')    #设置format_ave对象单元格数字类别显示格式

#分别以行或列的方式吧标题、业务类型、流量数据写入起始单元格，引用不同格式对象
worksheet.write_row('A1',title,format_title)
worksheet.write_column('A2',buname,format)
worksheet.write_row('B2',data[0],format)
worksheet.write_row('B3',data[1],format)
worksheet.write_row('B4',data[2],format)
worksheet.write_row('B5',data[3],format)
worksheet.write_row('B6',data[4],format)

#定义图表数据系统函数
def chartSeries(cur_row):
    worksheet.write_formula('I'+cur_row,'=AVERAGE(B'+cur_row+':H'+cur_row+')',format_ave)  #计算average函数一周的平均流量
    chart.add_series({
        'categories':'=Sheet1!$B$1:$H$1',   ##将星期一到星期日作为图表数据标签（X轴）
        'values':'=Sheet1!$B$'+cur_row+':$H$'+cur_row,   ##业务一周所有数据作为数据区域
        'line':{'color':'black'},             ##线条颜色设置为黑色
        'name':'=Sheet1!$A$'+cur_row,             ##引用业务名称为图例项
    })

for row in range(2,7):
    chartSeries(str(row))

chart.set_size({'width':577,'height':287})
chart.set_title({'name':u'业务周流量图表'})
chart.set_y_axis({'name':'Mb/s'})     #设置y轴左侧小标题，可以改成PV次数
worksheet.insert_chart('A8',chart)    #在A8单元格插入图表
workbook.close()



































