from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler
import time
'''
def my_job():
	print('hello')

# BlockingScheduler在当前线程的主线程运行
# 每隔5s执行一次my_job函数，输出hello world
scheduler = BlockingScheduler()
scheduler.add_job(my_job, 'interval', seconds = 5)#间隔5秒钟执行一次
scheduler.start()

while(True):
	print('main 1s')
	time.sleep(1)
输出结果：
hello
hello
（不会打印出main 1s 因为blockingscheduler会阻塞主线程的运行）
'''

'''
def my_job():
	# print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
	print('working 3s')
# BackgroundScheduler在其他线程运行
scheduler = BackgroundScheduler()
scheduler.add_job(my_job, 'interval', seconds = 3)#间隔3秒钟执行一次
scheduler.start()

while(True):
	print('main 1s')
	time.sleep(1)

输出结果：
main 1s
main 1s
main 1s
working 3s
main 1s
main 1s
main 1s
（不会阻塞主线程的运行）
'''

'''
from apscheduler.schedulers.background import BackgroundScheduler
import time

def job():
    print('job 3s')
    time.sleep(5)

# 假如执行时间大于间隔时间，则可以开多个线程来运行
# 配置调度器的参数max_instances，设置多个job()同时运行
if __name__=='__main__':
    job_defaults = { 'max_instances': 2 }
    sched = BackgroundScheduler(timezone='MST', job_defaults=job_defaults)
    sched.add_job(job, 'interval', id='3_second_job', seconds=3)
    sched.start()

    while(True):
        print('main 1s')
        time.sleep(1)
'''

# 触发器控制

# interval间隔调度
# weeks (int) – number of weeks to wait
# days (int) – number of days to wait
# hours (int) – number of hours to wait
# minutes (int) – number of minutes to wait
# seconds (int) – number of seconds to wait
# start_date (datetime|str) – starting point for the interval calculation
# end_date (datetime|str) – latest possible date/time to trigger on
# timezone (datetime.tzinfo|str) – time zone to use for the date/time calculations

# 例子
# 表示每隔3天17时19分07秒执行一次任务
# sched.add_job(my_job, 'interval', days=03, hours=17, minutes=19, seconds=07)
#间隔3秒钟执行一次
# scheduler.add_job(job3, 'interval', seconds=3)

# date 定时调度（作业只会执行一次）
# run_date (datetime|str) – the date/time to run the job at  -（任务开始的时间）
# timezone (datetime.tzinfo|str) – time zone for run_date if it doesn’t have one already

# 例子
# 在指定的时间，只执行一次
# scheduler.add_job(tick, 'date', run_date='xxxx-xx-xx xx:xx:xx')　　
# The job will be executed on November 6th, 2009
# sched.add_job(my_job, 'date', run_date=date(2009, 11, 6), args=['text'])
# The job will be executed on November 6th, 2009 at 16:30:05
# sched.add_job(my_job, 'date', run_date=datetime(2009, 11, 6, 16, 30, 5), args=['text'])

# cron定时调度（某一定时时刻执行）
# (int|str) 表示参数既可以是int类型，也可以是str类型
# (datetime | str) 表示参数既可以是datetime类型，也可以是str类型
# year (int|str) – 4-digit year -（表示四位数的年份，如2008年）
# month (int|str) – month (1-12) -（表示取值范围为1-12月）
# day (int|str) – day of the (1-31) -（表示取值范围为1-31日）
# week (int|str) – ISO week (1-53) -（格里历2006年12月31日可以写成2006年-W52-7（扩展形式）或2006W527（紧凑形式））
# day_of_week (int|str) – number or name of weekday (0-6 or mon,tue,wed,thu,fri,sat,sun) - （表示一周中的第几天，既可以用0-6表示也可以用其英语缩写表示）
# hour (int|str) – hour (0-23) - （表示取值范围为0-23时）
# minute (int|str) – minute (0-59) - （表示取值范围为0-59分）
# second (int|str) – second (0-59) - （表示取值范围为0-59秒）
# start_date (datetime|str) – earliest possible date/time to trigger on (inclusive) - （表示开始时间）
# end_date (datetime|str) – latest possible date/time to trigger on (inclusive) - （表示结束时间）
# timezone (datetime.tzinfo|str) – time zone to use for the date/time calculations (defaults to scheduler timezone) -（表示时区取值）

# 例子
#表示2017年3月22日17时19分07秒执行该程序
# sched.add_job(my_job, 'cron', year=2017,month = 03,day = 22,hour = 17,minute = 19,second = 07)

#表示任务在6,7,8,11,12月份的第三个星期五的00:00,01:00,02:00,03:00 执行该程序
# sched.add_job(my_job, 'cron', month='6-8,11-12', day='3rd fri', hour='0-3')

#表示从星期一到星期五5:30（AM）直到2014-05-30 00:00:00
# sched.add_job(my_job(), 'cron', day_of_week='mon-fri', hour=5, minute=30,end_date='2014-05-30')

#表示每5秒执行该程序一次，相当于interval 间隔调度中seconds = 5
# sched.add_job(my_job, 'cron',second = '*/5')