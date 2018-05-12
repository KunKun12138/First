from builtins import print

list = ['aaa','bbb','ccc',['hahaha','heiheihie']]
tuple = [1,2,list]
print(tuple)
list[1] = 'eee'
print(tuple)
print(list[1])
print(list[3][1])



s = "装换摄氏温度和华氏温度"
print(s.encode('utf-8'))
g = s.encode('utf-8')
#print(g.decode('Unicode'))
CelsiusTemperature = eval(input("摄氏温度为："))
Fahrenheit = (9/5)*CelsiusTemperature+32
print("华氏温度为", float(Fahrenheit))

score_thisyear = eval(input('今年的成绩'))
score_lsatyear = eval(input('去年的成绩'))
improvePrecent = ((score_thisyear-score_lsatyear)/score_lsatyear)*100
improvePrecent_abs = abs(((score_thisyear-score_lsatyear)/score_lsatyear)*100)
if(improvePrecent>0):
    print('今年的成绩比去年提升：%.1f%%'%improvePrecent_abs)
else:
    print('今年的成绩比去年下降：%.1f%%' % improvePrecent_abs)



PI = 3.14159
radius = eval(input("圆柱体半径为"))
length = eval(input("圆柱体高度为"))
area = radius*radius*PI
volume = area * length
print("底部面积为", area)
print("圆柱体体积为", volume)