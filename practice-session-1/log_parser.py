import re
from datetime import datetime
import functools
import operator


def datetime_to_string(line):
    match = re.search('(\w{3} \d{2} \d{2}:\d{2}:\d{2}:\d{2})', line)
    return match.group()


def convert_to_datetime(line):
    return datetime.strptime(datetime_to_string(line), '%b %d %H:%M:%S:%f')


with open(file='device.log') as f:
    f = f.readlines()

error_event = []
d = {}
active = []
for line in f:
    if 'ERR' in line:
        error_event.append(datetime_to_string(line))

    elif 'ON' in line:
        d[convert_to_datetime(line)] = 'ON'

    elif 'OFF' in line:
        d[convert_to_datetime(line)] = 'OFF'

    else:
        pass

ok = 0  # to get the first ON/OFF state
for k, v in d.items():
    if v == "ON":
        if ok == 0:
            time_start = k
            ok = 1

    elif v == "OFF":
        if ok == 1:
            dif = k - time_start
            active.append(dif)
            ok = 0

if not active:
    print("The device was OFF")
else:
    print("The device was ON:",functools.reduce(operator.add, active))

if not error_event:
    print("No errors")
else:
    print("The timestamps of errors:", error_event)
