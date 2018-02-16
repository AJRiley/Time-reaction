import time
from time import time as the_timer
import datetime
import random


now = datetime.datetime.now()

print(str(now))

print("Current year: {}".format(now.year))
print("Current Month: {}".format(now.month))
print("Current Day: {}".format(now.day))
print("Current hour: {}".format(now.hour))

input("Please, press enter to start")

wait_time = random.rimpandint(1, 6)
time.sleep(wait_time)
start_time = the_timer()

input("Please press enter to stop")

end_time = the_timer()

print("Started at " + time.strftime("%X", time.localtime(start_time)))
print("Ended at " + time.strftime("%X", time.localtime(end_time)))

print("Your reaction time was {}".format(end_time - start_time))
