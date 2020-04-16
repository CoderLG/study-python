import xlrd
import xlwt
def set_style(name,height,bold=False):
    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.name = name
    font.bold = bold
    font.color_index = 4
    font.height = height
    style.font = font
    return style

def diff(arr,str):
    res = ''
    for s in arr:
        if(s in str):
            qe=1
        else:
            res += s + ";"

    return res



if __name__ == '__main__':
    file = 'jishuzhan.xlsx'

    f = xlwt.Workbook()
    sheet2 = f.add_sheet('diff',cell_overwrite_ok=True)
    row0 = ["姓名","结果一和结果二","结果一和结果三"]

    for i in range(0,len(row0)):  #写第一行
        sheet2.write(0,i,row0[i],set_style('Times New Roman',220,True))


    wb = xlrd.open_workbook(filename=file)#打开文件
    #print(wb.sheet_names())#获取所有表格名字
    sheet1 = wb.sheet_by_index(0)#通过索引获取表格

    for i in range(1,87):
        rows = sheet1.row_values(i)#获取行内容


        name = rows[0]
        r1 = rows[1]
        r1Arr = r1.split(';')
        print(r1)
        print('-----------')

        r2 = rows[2]
        r2Arr = r2.split(';')
        print(r2)
        print('-----------')

        r3 = rows[3]
        r3Arr = r3.split(';')
        print(r3)

        row = []
        dif1 = diff(r2Arr,r1)
        dif2 = diff(r3Arr,r1)

        row.append(name)
        row.append(dif1)
        row.append(dif2)
        for j in range(0,len(row)):  #写剩下的
            sheet2.write(i,j,row[j],set_style('Times New Roman',220,True))

    f.save('test1.xls')

