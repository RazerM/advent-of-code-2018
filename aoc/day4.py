import re
from collections import defaultdict
from operator import itemgetter

re_date = re.compile(r'\[\d{4}-\d{2}-\d{2} \d{2}:(\d{2})\] (.*)')

re_begins = re.compile(r'Guard #(\d+) begins shift')


def solve(file):
    guard = None
    asleep_since = None

    guard_sleep_time = defaultdict(lambda: defaultdict(int))
    guard_total_sleep = defaultdict(int)

    lines = sorted(file)

    for line in lines:
        minute, message = re_date.match(line).groups()
        minute = int(minute)

        begins = re_begins.match(message)

        if begins:
            guard = int(begins.group(1))
        elif message == 'falls asleep':
            asleep_since = minute
        elif message == 'wakes up':
            for t in range(asleep_since, minute):
                guard_sleep_time[guard][t] += 1
                guard_total_sleep[guard] += 1

    guard_id, _ = max(guard_total_sleep.items(), key=itemgetter(1))
    sleepiest_min, _ = max(guard_sleep_time[guard_id].items(), key=itemgetter(1))
    print('Part 1:', guard_id * sleepiest_min)

    top_guard_id = None
    top_minute = None
    top_frequency = 0
    for guard_id, sleep_times in guard_sleep_time.items():
        minute, frequency = max(sleep_times.items(), key=itemgetter(1))
        if frequency > top_frequency:
            top_guard_id = guard_id
            top_minute = minute
            top_frequency = frequency

    print('Part 2:', top_guard_id * top_minute)