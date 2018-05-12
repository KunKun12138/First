import itertools
import xlrd   #使用xlrd读取文件
import xlwt   #使用xlwt生成Excel文件（可以控制Excel中单元格的格式）。但是用xlrd读取excel是不能对其进行操作的；而xlwt生成excel文件是不能在已有的excel文件基础上进行修改的，如需要修改文件就要使用xluntils模块。pyExcelerator模块与xlwt类似，也可以用来生成excel文件
from xlutils.copy import copy


#创建workbook和sheet对象
workbook = xlwt.Workbook() #注意Workbook的开头W要大写
#OriginalFile = open('D://test9.xls')
#workbook = copy(OriginalFile)
sheet1 = workbook.add_sheet('sheet1',cell_overwrite_ok=True)
sheet2 = workbook.add_sheet('sheet2',cell_overwrite_ok=True)

#向sheet页中写入数据
sheet1.write(0,0,'测试案例')
sheet1.write(0,1,'前提数据')
sheet1.write(0,2,'测试数据')
sheet1.write(0,3,'预测结果')
case = 1
Prerequisites = 1
##for testcase in itertools.product(["银行卡风险次数0次，最近一笔在7天内","银行卡风险次数1次，最近一笔在7天内","银行卡风险次数2次，最近一笔在7天内","银行卡风险次数3次，最近一笔在7天内","银行卡风险次数3次，最近一笔在7天外"],
##                                  ["交易手机号风险次数0次，最近一笔在7天内", "交易手机号风险次数1次，最近一笔在7天内", "交易手机号风险次数2次，最近一笔在7天内",
##                                   "交易手机号风险次数3次，最近一笔在7天内", "交易手机号风险次数3次，最近一笔在7天外"],
##                                  ["受益手机号风险次数0次，最近一笔在7天内", "受益手机号风险次数1次，最近一笔在7天内", "受益手机号风险次数2次，最近一笔在7天内",
##                                   "受益手机号风险次数3次，最近一笔在7天内", "受益手机号风险次数3次，最近一笔在7天外"]):

for testcase in itertools.product(["交易手机0笔有风险，最近一笔在5天内", "交易手机1笔有风险，最近一笔在5天内", "交易手机1笔有风险，最近一笔在5天外" ,"交易手机2笔有风险，最近一笔在5天内"],
                                  ["交易手机0笔有风险，最近一笔在5天内", "交易手机1笔有风险，最近一笔在5天内", "交易手机1笔有风险，最近一笔在5天外", "交易手机2笔有风险，最近一笔在5天内"]):

    print(testcase)
    #向excel表第一列写入测试案例
    sheet1.write(case, 0, testcase)
    case = case + 1
    print("发生时间点:")
    sheet1.write(Prerequisites, 1, "发生时间点:")
    b=0
    q=1
    for i in range(len(testcase)):
        if testcase[i].count('内')>0:
            if testcase[i].count('0') > 0:
               print("[]")
               sheet1.write(Prerequisites, 1, "[]")
               a=0
            elif testcase[i].count('1') > 0:
               print("[2017-12-01 00:01:00]")
               sheet1.write(Prerequisites, 1, "[2017-12-01 00:01:00]")
               a=1
            elif testcase[i].count('2') > 0:
               print("[2017-12-02 00:00:01] [2017-12-03 00:01:00]")
               sheet1.write(Prerequisites, 1, "[2017-10-11 00:00:01] [2017-10-11 00:01:00]")
               a=1
            elif testcase[i].count('3') > 0:
                print("[2017-10-11 00:00:01] [2017-10-11 00:01:00] [2017-10-12 00:01:00]")
                sheet1.write(Prerequisites, 1, "[2017-10-11 00:00:01] [2017-10-11 00:01:00] [2017-10-12 00:01:00]")
                a=3
        elif testcase[i].count('外')>0:
            print("[2017-10-08 00:00:01]")
            sheet1.write(Prerequisites, 1, "[2017-10-08 00:00:01]")
            a=0
        b=b+a
        Prerequisites = Prerequisites + 1

    print("交易结果为：")
    #print("b:",b)
    if b>=2 :
         print("锁卡")
    else:
         print("不锁卡")
    #q = q + 1
    print("交易时间点：[2017-12-04 00:00:00]")
    #print(q)
    workbook.save('D://test9.xls')
    print("xiewan")

