#coding=utf-8

from pydata.selenium_base import  *
from pydata.base import *
import xlwt

book = xlwt.Workbook()
sheet = book.add_sheet("sheet1",cell_overwrite_ok=True)

se = Base_()

se.open_("http://hngcjs.hnjs.gov.cn/company/list?corpname=")
# driver.switch_to_frame("newsiframe")
# ele = se.get_position("css selector","select#CretType")
#
# s = Select(ele)
# s.select_by_value("1")
# 选择建筑业
se.select_by_value("css selector","select#CretType","7")
# 点击唤出企业注册地下拉框
# se.click_("css selector",".filter_dropdown>span>span")
# 获取注册地的个数
len_di = len(se.get_positions("css selector",".dropdown-menu.staff_dropdown>li"))
print(len_di)
# 选择企业注册地
for i in range(1,len_di+1):
    # 点出下拉框
    se.click_("css selector", ".filter_dropdown>span>span")
    time.sleep(1)
    # 选择注册地
    se.click_("css selector",".dropdown-menu.staff_dropdown>li:nth-child("+str(i)+")>a")
    # 点击搜索
    se.click_("name","ctl09")
    # 保存页面并转换为soup文档
    html = driver.page_source
    # print(html)
    soup = BeautifulSoup(html,"html.parser")
    # 提取所有行
    qylis = soup.select("#tagContenth tbody>tr")
    print(qylis)
    # 获取所有行的长度
    len_q = len(qylis)
    print(len_q)
    qynames = []
    qyhrefs = []
    for i in range(2,len_q+1):
        qyname = soup.select("#tagContenth tbody>tr:nth-child("+str(i)+")>td:nth-child(2)>a")[0].get_text()
        qynames.append(qyname)
        qyhref = "http://hngcjs.hnjs.gov.cn"+ soup.select("#tagContenth tbody>tr:nth-child("+str(i)+")>td:nth-child(2)>a")[0]["href"]
        qyhrefs.append(qyhref)

    # print(qynames)
    # print(qyhrefs)

# for i in range(1,len_q):
#     row = i
#     qyname = qynames[i-1]
#     qyhref = qyhrefs[i-1]
#     sheet.write(row,1,qyname)
#     sheet.write(row,2,qyhref)
#
# book.save("E://mydata//qyzznames.xls")
# print("success")


