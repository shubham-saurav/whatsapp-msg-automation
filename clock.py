from datetime import *
from msg_automation import *
from apscheduler.schedulers.blocking import BlockingScheduler




sched = BlockingScheduler()


sched.add_job(send_msg, 'interval', seconds=100)

sched.start()