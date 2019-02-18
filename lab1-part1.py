# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 15:59:20 2019

@author: jason
"""

#logstats2
#map phase

import re
import sys
from operator import itemgetter

pat = re.compile('(?P<ip>\d+.\d+.\d+.\d+).*?\d{4}:(?P<hour>\d{2}):\d{2}.*? ')
for line in sys.stdin:
    match = pat.search(line)
    if match:
        print '%s\t%s' % ('[' + match.group('hour') + ':00' + ']' + match.group('ip'), 1)
    
#text = open("log2.txt")
#text2 = text.readlines()

#reduce phase

dict_ip_count = {}

for line in sys.stdin:
    line = line.strip()
    hour_ip, num = line.split('\t')
    try:
        num = int(num)
        dict_ip_count[hour_ip] = dict_ip_count.get(hour_ip, 0) + num

    except ValueError:
        pass

dict_hour_ip_count = {}
for hour_ip, count in dict_ip_count.items():
        hour = hour_ip[1:6]
        ip = hour_ip[7:]
        count = int(count)
        #print(hour)
        #print(ip)
        #print(count)
        if hour not in dict_hour_ip_count.keys():
            dict_hour_ip_count[hour] = [(ip,count)]
        else:
            dict_hour_ip_count[hour].append((ip, count))

for hour, ip_count in dict_hour_ip_count.items():
    print("The hour is", hour)
    #print("The ipcount is", ipcount)
    top_3_ip = sorted(list(ip_count), key = lambda x:x[1], reverse=True)[0:3]
    print("top 3 ip", top_3_ip)
    for ip, count in top_3_ip:
        print '%s\t%s' % ('['+hour+']' +ip, count)













