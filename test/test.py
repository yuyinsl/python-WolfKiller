#!/usr/bin/env python
import urllib2,cookielib
import os
import re

class WolfKiller:  

    def __init__(self):
        self.logInURL="http://www.langren8.com/loginaction.aspx"
        self.userInfoURL="http://www.langren8.com/Service/Service.aspx?api_key=LJfi1j3MNfk1op23&method=ClientUser.GetLoginedUserInfo"     
        self.cookie = cookielib.CookieJar()
        self.httpcookie = urllib2.HTTPCookieProcessor(self.cookie)
        self.opener = urllib2.build_opener(self.httpcookie)
        urllib2.install_opener(self.opener)       
    
    def logIn(self,username,pwd):    
        enparams="username="+username+"&pwd="+pwd
        headers = {'Content-Type':'application/x-www-form-urlencoded','Connection':'Keep-Alive'}
        request = urllib2.Request(url = self.logInURL,headers = headers,data=enparams)
        stream=urllib2.urlopen(request)
        result=stream.read()
        if (result.find('Game')==-1):
            return False
        else:
            return True  
        
    def getInfo(self):
        try:
            stream = urllib2.urlopen(self.userInfoURL).readlines()
            p='<\w+>[^<]+</\w+>'
            result=re.findall(p,stream[0])
            for element in result:
                print element
        except Exception, e:
            print e
            print urllib2.urlopen(self.userInfoURL).read()             
    
    def getID(self):
        try:
            stream = urllib2.urlopen(self.userInfoURL).readlines()
            p='>[^<]+<'
            result=re.findall(p,stream[0])
            ID=result[2].strip('<>')
            return ID
        except Exception, e:
            print e
            return None     
        
if __name__ == "__main__":

    filePath=open("test.txt",'r')
    getGold = WolfKiller()
    for line in filePath:
        line=line.strip()
        if line:
            username,pwd=line.split('|')
            getGold.logIn(username,pwd)
            ID=getGold.getID()
            print ID
    str = os.popen('shutdown -r 0.5').read
    print str
    raw_input("Press Enter to exit....")

