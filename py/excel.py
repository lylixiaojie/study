# -*- coding: utf-8 -*-
#python
#用于实现读取excel的测试用例，生成markdown文件

import xlrd
import os
import string

<<<<<<< HEAD
excel_url =r'C:\test\test.xlsx'
md_url='C:\\test\\'
=======
excel_url =r'c:\test\test.xlsx'
md_url='c:\\test\\'
>>>>>>> ec0b3cd20d59f6cabe278eaa5951120beebc7cec

workbook = xlrd.open_workbook(excel_url)
print(workbook.sheet_names())

sheet1 = workbook.sheet_by_index(0)

print('有',sheet1.nrows , '列')
print('有',sheet1.ncols ,'行')
def insert_md():
<<<<<<< HEAD
    max=sheet1.nrows
=======
    max=sheet1.nrows-1
>>>>>>> cb9f8ba1cbeb27bb603fc01cfc5312cc208ddccb
    for i in range(1,max):
        try:
            md_example_name = sheet1.cell(i, 0).value
            md_example_name_y = md_example_name.strip()
            md_url_file='%s%s.md'%(md_url,md_example_name_y)
            file = open(md_url_file, 'w')
            file.write('### 用例编号:  ')
            file.write('\n')
            file.write('\n')
            file.write(sheet1.cell(i, 1).value)
            file.write('\n')
            file.write('\n')
            file.write('### 测试项:')
            file.write('\n')
            file.write('\n')
            file.write(sheet1.cell(i, 2).value)
            file.write('\n')
            file.write('\n')
            file.write('### 级别:')
            file.write('\n')
            file.write('\n')
            file.write(sheet1.cell(i, 3).value)
            file.write('\n')
            file.write('\n')
            file.write('### 前置条件:')
            file.write('\n')
            file.write('\n')
            file.write(sheet1.cell(i, 4).value)
            file.write('\n')
            file.write('\n')
            file.write('### 测试步骤:')
            file.write('\n')
            file.write('\n')
            file.write(sheet1.cell(i, 5).value)
            file.write('\n')
            file.write('\n')
            file.write('### 预期结果:')
            file.write('\n')
            file.write('\n')
            file.write(sheet1.cell(i, 6).value)
            file.write('\n')
            file.write('\n')
            file.write('### 测试结果:')
            file.write('\n')
            file.write('\n')
            file.write(sheet1.cell(i, 7).value)
            file.write('\n')
            file.write('\n')
            file.write('### 设计人:')
            file.write('\n')
            file.write('\n')
            file.write(sheet1.cell(i, 8).value)
            file.write('\n')
            file.write('\n')
            file.write('### 修改日期:')
            file.write('\n')
            file.write('\n')
            file.write(sheet1.cell(i, 9).value)
            file.write('\n')
            file.write('\n')
            file.write('### 备注:')
            file.write('\n')
            file.write('\n')
            file.write(sheet1.cell(i, 10).value)
            file.write('\n')
            file.close()
            print(sheet1.cell(i, 0).value)
        except IOError:
            print("Error: 文件名有问题")
        else:
            continue

#获取类型

insert_md()

print('pause')
