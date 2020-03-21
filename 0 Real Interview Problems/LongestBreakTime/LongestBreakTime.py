# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from collections import namedtuple
import re

weekday_order = {
    "Mon" : 0,
    "Tue" : 1,
    "Wed" : 2,
    "Thu" : 3,
    "Fri" : 4, 
    "Sat" : 5, 
    "Sun" : 6,
}

def get_minute(time):
    hour = int(time[:2])
    minute = int(time[3:])
    return hour*60+minute
    
time_slot = namedtuple('time_slot', ['begin', 'end'])

# Convertion split using regex
def convert_time(time_slot_str):
    weekday, start, end = re.split('[ -]', time_slot_str)
    start_minute = get_minute(start) 
    end_minute = get_minute(end)
    weekday_minute = weekday_order[weekday] * 24 * 60 
    ret = time_slot(begin = weekday_minute+start_minute, end=weekday_minute+end_minute)
    return ret
    
# Dummy time take care of edge case when James only has 1 item on calendar
# Since there are no 2 ongoing meeting at the same time. We don't have to merge interval
def solution(S):
    S_array = S.split('\n')
    dummy_time = [time_slot(begin = 0, end=0), time_slot(begin=10080, end=10080)]
    relative_time = dummy_time + [convert_time(time_slot) for time_slot in S_array]
    relative_time.sort(key = lambda interval: interval.begin)
    longest_break_time = 0
    for i, cur_slot in enumerate(relative_time):
        if i == 0: continue
        pre_slot = relative_time[i-1]
        cur_break_time = cur_slot.begin - pre_slot.end
        longest_break_time = max(longest_break_time, cur_break_time)
    return longest_break_time
    
    
    
    
