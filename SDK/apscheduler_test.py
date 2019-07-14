from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.executors.pool import ThreadPoolExecutor

def fn(num):
    with open('./test.txt', "w", encoding="utf-8") as f:
        print(num)
        f.write(str(num)*10)

executors = {
    'default': ThreadPoolExecutor(10)
}

# scheduler_ = BackgroundScheduler(executors=executors)
scheduler_ = BlockingScheduler(executors=executors)
# scheduler_.add_job(fn, 'interval', seconds=3, args=(1000,))
# scheduler_.add_job(fn, 'cron', second='1-59', args=(1000,))

from apscheduler.triggers import interval,date,cron
i = interval.IntervalTrigger(seconds=3)
# d = date.DateTrigger()
# c = cron.CronTrigger(second="1-10")
scheduler_.add_job(fn, trigger=i, args=(100,))
# scheduler_.add_job(fn, trigger=d, args=(100,))
# scheduler_.add_job(fn, trigger=c, args=(100,))




scheduler_.start()
