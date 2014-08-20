#!/usr/bin/env python


import urllib2  


enparams="account=streem10086&nickname=streem10086&sex=1&password=streem&password1=streem&qq=123456789"
headers = {'Content-Type':'application/x-www-form-urlencoded','Connection':'Keep-Alive'}
request = urllib2.Request("http://www.langren8.com/reg2013.aspx",headers = headers,data=enparams)
stream=urllib2.urlopen(request)
result=stream.read()

