#!/usr/bin/env python

import urllib2
import time


while True:
    uk = raw_input("Please input your uk: ")
    if len(uk) != 16:
        print "Your uk is error,please try again."
        continue
    else:
        break

tickets = raw_input("Please input your gifts to draw: ")
num = int(tickets) / 10
url = "http://www.langren8.com/Service/Service.aspx?api_key=LJfi1j3MNfk1op23&method=ClientChouJiang.Start2014&uk=" + uk

i = 0
while i < num:
    try:
        result = urllib2.urlopen(url).read()
        i += 1
#         print result
        if i % 50 == 0:
            print i
            time.sleep(3)
    except Exception, e:
        print e

raw_input("Press Enter to exit....")
