#在收集完问卷后运行该python文件得到三个柱状图统计结果
import pyecharts
from pyecharts.charts import Bar
#性别结果
f = open("gender.txt","r")   #设置文件对象
str = f.read()     #将txt文件的所有内容读入到字符串str中
f.close()   #将文件关闭
m=0
f=0
for i in str:
    if(i=='M'):
        m=m+1
    else:
        f=f+1

bar = Bar()
bar.add_xaxis(["男性", "女性"])
bar.add_yaxis("性别人数统计", [m,f])
bar.render("outcoming_gender.html")

#睡觉时间结果
f = open("time.txt","r")   #设置文件对象
str = f.read()     #将txt文件的所有内容读入到字符串str中
f.close()   #将文件关闭
a=0
b=0
c=0
for i in str:
    if(i=='0'):
        a=a+1
    elif(i=='1'):
        b=b+1
    elif(i=='2'):
        c=c+1
    else:
        continue

bar = Bar()
bar.add_xaxis(["10：00-11：00", "11：00-12：00","12；00-1；00"])
bar.add_yaxis("睡觉时间人数统计", [a,b,c])
bar.render("outcoming_time.html")

#介意的生活习惯结果
f = open("habits.txt","r")   #设置文件对象
str = f.read()     #将txt文件的所有内容读入到字符串str中
f.close()   #将文件关闭
a=0
b=0
c=0
for i in str:
    if(i=='0'):
        a=a+1
    elif(i=='1'):
        b=b+1
    elif(i=='2'):
        c=c+1
    else:
        continue

bar = Bar()
bar.add_xaxis(["睡觉打呼噜", "大声说话","不爱卫生"])
bar.add_yaxis("介意的生活习惯人数统计", [a,b,c])
bar.render("outcoming_habits.html")

print("您可以在本文件夹下寻找outcoming_gender.html，outcoming_time.html，outcoming_habits.html得到统计结果")