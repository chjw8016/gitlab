#!/usr/bin/env python
# coding=utf-8
import time
import datetime
import pytz


def utc_to_local(utc_time_str, utc_format='%Y-%m-%dT%H:%M:%S.%f+08:00'):
    local_tz = pytz.timezone('Asia/Shanghai')
    local_format = "%Y-%m-%d %H:%M:%S"
    utc_dt = datetime.datetime.strptime(utc_time_str, utc_format)
    local_dt = utc_dt.replace(tzinfo=pytz.utc).astimezone(local_tz)
    time_str = local_dt.strftime(local_format)
    return int(time.mktime(time.strptime(time_str, local_format)))
