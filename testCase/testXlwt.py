# -*- codeing = utf-8 -*-
import xlwt

# 创建文档对象
workbook = xlwt.Workbook(encoding="utf-8")

worksheet = workbook.add_sheet("豆瓣电影TOP250")
# 参数1： 行号，参数2：列号,参数3：value
# worksheet.write(0, 0, 'hello')
for i in range(0, 9):
    for j in range(0, i + 1):
        worksheet.write(i, j, "%d * %d = %d" % (i + 1, j + 1, (i + 1) * (j + 1)))

workbook.save('test.xls')
