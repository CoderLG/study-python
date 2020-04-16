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

if __name__ == '__main__':
    f = xlwt.Workbook()
    sheet1 = f.add_sheet('diff',cell_overwrite_ok=True)
    row0 = ["姓名","结果一和结果二","结果一和结果三"]

    for i in range(0,len(row0)):  #写第一行
        sheet1.write(0,i,row0[i],set_style('Times New Roman',220,True))

    for i in range(0,len(row0)):  #写剩下的
        sheet1.write(0,i,row0[i],set_style('Times New Roman',220,True))