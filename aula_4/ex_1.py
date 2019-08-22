import os
import sys
import subprocess
import datetime
import time

# for i in range(10 ** 6):
#    agora = datetime.datetime.now().strftime('%d-%m-%Y | %H-%M-%S')
#    print(
#        '{} | log {}'.format(agora, i)
#    )
#    time.sleep(0.01)


with open('log', 'r') as f:

    for line in f.readlines():
        date, hour, log = line.split('|')

        log_n = log.lstrip().split(' ')[-1]
        log_n = int(log_n)
        
        if log_n % 7 !=0:
            print(date,hour,log)