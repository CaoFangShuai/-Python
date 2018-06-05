# -*-coding:utf-8 -*-
from datetime import datetime,timedelta,timezone
print(datetime.now())#获取当前时间
# datetime.now()返回当前日期和时间，其类型是datetime。
dt = datetime(2015, 4, 19, 12, 20) # 用指定日期时间创建datetime
print(dt)
# datetime转换为timestamp
# 在计算机中，时间实际上是用数字表示的。我们把1970年1月1日 00:00:00 UTC+00:00时区的时刻称为epoch time，
# 记为0（1970年以前的时间timestamp为负数），当前时间就是相对于epoch time的秒数，称为timestamp(时间戳)。
# timestamp = 0 = 1970-1-1 00:00:00 UTC+0:00
# 对应的北京时间是：timestamp = 0 = 1970-1-1 08:00:00 UTC+8:00
'''
可见timestamp的值与时区毫无关系，因为timestamp一旦确定，其UTC时间就确定了，转换到任意时区的时间也是完全确定的，
这就是为什么计算机存储的当前时间是以timestamp表示的，因为全球各地的计算机在任意时刻的timestamp都是完全相同的（假定时间已校准）。
'''
print(dt.timestamp())
# timestamp转换为datetime
# 要把timestamp转换为datetime，使用datetime提供的fromtimestamp()方法：
t=1429417200.0
print(datetime.fromtimestamp(t))#本地时间  操作系统指定的UTC时间
print(datetime.utcfromtimestamp(t)) # UTC时间
# str转换为datetime
# 很多时候，用户输入的日期和时间是字符串，要处理日期和时间，首先必须把str转换为datetime。转换方法是通过datetime.strptime()实现，需要一个日期和时间的格式化字符串：
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)
now = datetime.now()
print(now.strftime('%a,%b %d %H:%M'))
# datetime加减
now = datetime.now()
print(now)

# print(now + timedelta(hours=10))
# print(now - timedelta(days=1))
print(now + timedelta(days=2, hours=12))
# 本地时间转换为UTC时间
'''
本地时间是指系统设定时区的时间，例如北京时间是UTC+8:00时区的时间，而UTC时间指UTC+0:00时区的时间。

一个datetime类型有一个时区属性tzinfo，但是默认为None，所以无法区分这个datetime到底是哪个时区，除非强行给datetime设置一个时区：
'''
tz_utc_8 = timezone(timedelta(hours=8)) # 创建时区UTC+8:00
now=datetime.now()
print(now)
dt=now.replace(tzinfo=tz_utc_8)#强制设置失去UTC+8:00
print(dt)
# 如果系统时区恰好是UTC+8:00，那么上述代码就是正确的，否则，不能强制设置为UTC+8:00时区。
# 时区转换
# 我们可以先通过utcnow()拿到当前的UTC时间，再转换为任意时区的时间：

# 拿到UTC时间，并强制设置时区为UTC+0:00:
utc_dt=datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
