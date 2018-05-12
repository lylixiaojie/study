# -*- coding: utf-8 -*-
#python
#用于实现读取excel的测试用例，生成markdown文件

import xlrd
import os

excel_url =r'E:\test\test.xlsx'
md_url='E:\\test\\'

workbook = xlrd.open_workbook(excel_url)
print(workbook.sheet_names())

sheet1 = workbook.sheet_by_index(0)

print('有',sheet1.nrows , '列')
print('有',sheet1.ncols ,'行')
def insert_md():
    max=sheet1.nrows-1
    i=1
    for i in range(1,max):
        md_example_name = sheet1.cell(i, 0).value
        file = open(md_url + md_example_name + '.md', 'w')
        file.write('<br/><h3>用例编号:')
        file.write('<br/>')
        file.write(sheet1.cell(i, 0).value)
        file.write('<br/><h3>测试项:')
        file.write('<br/>')
        file.write(sheet1.cell(i, 1).value)
        file.write('<br/>')
        file.write('<br/><h3>前置条件:')
        file.write('<br/>')
        file.write(sheet1.cell(i, 2).value)
        file.write('<br/>')
        file.write('<br/><h3>测试步骤:')
        file.write('<br/>')
        file.write(sheet1.cell(i, 3).value)
        file.write('<br/>')
        file.write('<br/><h3>预期结果:')
        file.write('<br/>')
        file.write(sheet1.cell(i, 4).value)
        file.close()

print(sheet1.cell(1,0).value)

#获取类型
print(sheet1.cell_type(3,0))
insert_md()

