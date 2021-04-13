from datetime import datetime
import time

time1 = datetime.now()

time.slee(10)

time2 = datetime.now()

delta_time = ((time2 - time1).total_seconds()) / 60
