from datetime import datetime, timedelta, timezone

"""now"""
now = datetime.now()
print(now)
print(type(now))

"""定义，timestamp"""
dt = datetime(2015, 4, 19, 12, 20)
print(dt)
print(dt.timestamp())

t = 1429417200.0
print(datetime.fromtimestamp(t))
print(datetime.utcfromtimestamp(t))

"""string转datetime"""
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)

"""datetime转string"""
now = datetime.now()
print(now.strftime('%a, %b %d %H:%M'))

"""datetime加减运算"""
print(now)
print(now + timedelta(hours=10))
print(now - timedelta(days=1))
print(now + timedelta(days=2, hours=12))
delta = now - cday
print("delta:", now - cday)

"""本地时间转为UTC时间"""
tz_utc_8 = timezone(timedelta(hours=8))
print(now)
print(now.replace(tzinfo=tz_utc_8))

"""时区转换"""
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)  # 获取UTC时间
print("utc_time:", utc_dt)
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))  # 将UTC时间转换时区为北京时间
print("bj_time:", bj_dt)
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))  # 将UTC时间转换时区为东京时间
print("tokyo_dt:", tokyo_dt)
tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))  # 将北京时间转换时区为东京时间
print("tokyo_dt2:", tokyo_dt2)
