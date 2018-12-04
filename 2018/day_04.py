"""Advent of Code Day 4 - Repose Record"""

import collections
import datetime as dt
import re


def make_datetime(record):
    """Parse record and return timestamp converted to datetime object."""
    date_regex = re.compile(r'1518-(\d+)-(\d+) (\d+):(\d+)')
    month, day , hour, minutes = re.search(date_regex, record).groups()
    datetimed = dt.datetime(1518, int(month), int(day),
                            hour=int(hour), minute=int(minutes))
    return datetimed


def track_time(ordered_records):
    """Return dictionary of the state of each day's guard every minute."""
    guard_tracker = {}
    time_regex = re.compile(r'\[(\S+).*:(\d+)')
    guard_regex = re.compile(r'#(\d+)')
    for record in ordered_records:
        time_info = re.search(time_regex, record)
        date, mins = time_info.group(1), int(time_info.group(2))
        start_shift = re.search(guard_regex, record)
        if start_shift:
            guard = int(start_shift.group(1))
            mins = 0

        elif 'asleep' in record:
            # Make entry here to cope with shifts that start on previous day
            if (date, guard) not in guard_tracker:
                guard_tracker[(date, guard)] = ['.'] * 60

        elif 'wakes' in record:
            for minute in range(prev_mins, mins):
                guard_tracker[(date, guard)][minute] = '#'

        prev_mins = mins

    return guard_tracker


def track_sleep(guard_tracker):
    """Return dictionary that maps guards to the time they are asleep."""
    sleep_tracker = {}
    for key, value in guard_tracker.items():
        guard = key[1]
        if guard not in sleep_tracker:
            sleep_tracker[guard] = []
        for minute, state in enumerate(value):
            if state == '#':
                sleep_tracker[guard].append(minute)

    return sleep_tracker


def frequent_sleeper(sleep_tracker):
    """Return ID that sleeps the most * the minute they sleep most often."""
    sleepiest_guard, most_sleeps = None, 0
    for guard, sleeps in sleep_tracker.items():
        num_sleeps = len(sleeps)
        if num_sleeps > most_sleeps:
            sleepiest_guard, most_sleeps = guard, num_sleeps

    sleep_counter = collections.Counter(sleep_tracker[sleepiest_guard])
    sleepiest_time = sleep_counter.most_common(1)[0][0]

    return sleepiest_guard * sleepiest_time


def consistent_sleeper(sleep_tracker):
    """Return ID that sleeps most times at the same minute * that minute."""
    guard_id, minute, times_asleep_at = None, 0, 0
    for guard, sleeps in sleep_tracker.items():
        time, num_sleeps = collections.Counter(sleeps).most_common(1)[0]
        if num_sleeps > times_asleep_at:
            guard_id, minute, times_asleep_at = guard, time, num_sleeps

    return guard_id * minute


if __name__ == '__main__':

    with open('input.txt') as f:
        records = f.readlines()

    # Order records
    ordered_records = sorted(records, key=make_datetime)

    # Map each day to a guard and track the guards actions each minute
    guard_tracker = track_time(ordered_records)

    # Associate sleeping minutes with each guards ID
    sleep_tracker = track_sleep(guard_tracker)

    # Answer One
    print("Strategy One:", frequent_sleeper(sleep_tracker))

    # Answer Two
    print("Strategy Two:", consistent_sleeper(sleep_tracker))
