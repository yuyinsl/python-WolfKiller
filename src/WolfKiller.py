#!/usr/bin/env python
# encoding: utf-8

import urllib2
import cookielib
import os
import time
import logging

import sys
import re
import string
import random


def idGenerator(size=8, chars=string.ascii_letters+string.digits):
    return ''.join(random.choice(chars) for x in range(size))


class WolfKiller:

    def __init__(self):
        """


        """
        self.registerURL = "http://www.langren8.com/regaction2013.aspx"
        self.logInURL = "http://www.langren8.com/loginaction2013.aspx"
        self.userInfoURL = "http://www.langren8.com/Service/Service.aspx?api_key=LJfi1j3MNfk1op23&method=ClientUser.GetLoginedUserInfo"
        self.userList = {}
        self.cookie = cookielib.CookieJar()
        self.httpcookie = urllib2.HTTPCookieProcessor(self.cookie)
        self.opener = urllib2.build_opener(self.httpcookie)
        urllib2.install_opener(self.opener)

    def register(self, num=1):
        while num > 0:
            num -= 1
            if num % 50 == 1:
                time.sleep(1)
            try:
                account = idGenerator()
                if self.userList.get(account):
                    continue

                enparams="account=" + account + "&nickname=" + account + "&sex=1&password=" + account + "&password1=" + account + "&qq=&email="\
                    +account + "%40126.com&mobile=&Submit=%E4%B8%80%E5%88%87%E5%B0%B1%E7%BB%AA%EF%BC%8C%E7%AB%8B%E5%8D%B3%E6%B3%A8%E5%86%8C%EF%BC%81"
                headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Connection': 'Keep-Alive'}
                request = urllib2.Request(url=self.registerURL, headers=headers, data=enparams)
                urllib2.urlopen(request)
                if self.logIn(account, account):
                    uk = self.getUK()
                    self.signIn(uk)
                    regLogger.info(account + ':' + uk + ';')

            except Exception, e:
                print e
                print account

    def logIn(self, account, password):
        enparams = "account=" + account + "&password=" + password
        headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Connection': 'Keep-Alive'}
        request = urllib2.Request(url=self.logInURL, headers=headers, data=enparams)
        stream = urllib2.urlopen(request)
        result = stream.read()
        if result.find('index2013.aspx') == -1:
#             print "Login failed! Please check your account and password."
            print account
            return False
        else:
            return True

    def getInfo(self):
        try:
            stream = urllib2.urlopen(self.userInfoURL).readlines()
            p = '<\w+>[^<]+</\w+>'
            result = re.findall(p, stream[0])
            for element in result:
                print element
        except Exception, e:
            print e
            print urllib2.urlopen(self.userInfoURL).read()

    def getUK(self):
        try:
            stream = urllib2.urlopen(self.userInfoURL).readlines()
            p = '>[^<]+<'
            result = re.findall(p, stream[0])
            uk = result[0].strip('<>')
            return uk
        except Exception, e:
            print e
            return None

    def getID(self):
        try:
            stream = urllib2.urlopen(self.userInfoURL).readlines()
            p = '>[^<]+<'
            result = re.findall(p, stream[0])
            ID = result[2].strip('<>')
            return ID
        except Exception, e:
            print e
            return None

    def getGiftAmount(self):
        try:
            stream = urllib2.urlopen(self.userInfoURL).readlines()
            p = '<Gift>[^<]+</Gift>'
            result = re.search(p, stream[0]).group()
            giftAmount = re.search('\d+', result).group()
            return giftAmount
        except Exception, e:
            print e
            return None

    def draw(self, gifts=False):
        uk = self.getUK()
        totalGift = self.getGiftAmount()
        if not gifts:
            gifts = totalGift
        print "total gifts is %s" % totalGift
        drawURL = "http://www.langren8.com/Service/Service.aspx?api_key=LJfi1j3MNfk1op23&method=ClientChouJiang.Start&uk=%s" % uk
        print "gifts= %s" % gifts
        i = 0
        jz = 0
        num = int(gifts) / 10
        while i < num:
            try:
                result = urllib2.urlopen(drawURL).read()
                i += 1
                try:
                    if int(result) == 12:
                        jz += 1
                except:
                    print result
                time.sleep(1)
                if i % 1000 == 0:
                    print i, jz
                #     time.sleep(3)
            except Exception, e:
                print e

    def signIn(self, uk=None):
        #  must login first
        if uk:
            try:
                signInURL1 = "http://www.langren8.com/Service/Service.aspx?api_key=LJfi1j3MNfk1op23&method=UserGuanZhu.Login&uk=" + uk.strip()
                signInURL2 = "http://www.langren8.com/Service/Service.aspx?api_key=LJfi1j3MNfk1op23&method=UserGuanZhu.Play&uk=" + uk.strip()
                urllib2.urlopen(signInURL1)
                urllib2.urlopen(signInURL2)
            except Exception, e:
                print e
                print uk

        else:
            filePath = open("getGold.log", 'r')
            i = 0
            for line in filePath:
                if i < 2000:
                    i += 1
                    continue

                account = line.split(':')[0].strip()
                uk = line.split(':')[1].strip(';')
                if self.logIn(account, account):
                    try:
                        signInURL = "http://www.langren8.com/Service/Service.aspx?api_key=LJfi1j3MNfk1op23&method=UserGuanZhu.Login&uk=" + uk
                        playURL = "http://www.langren8.com/Service/Service.aspx?api_key=LJfi1j3MNfk1op23&method=UserGuanZhu.Play&uk=" + uk
                        urllib2.urlopen(signInURL)
                        urllib2.urlopen(playURL)
                    except Exception, e:
                        print e
                        signInLogger.info("%s:%s" % (account, uk))
                else:
                    print "Login failed: %s, %s" % (account, account)
                i += 1
                if i % 100 == 0:
                    print i
#                 if i%50==0:
#                     time.sleep(1)

#                 if i%10==0:
#                     break
            self.signInRemain()
        return

    def signInRemain(self):
        signInLast = []
        i = 0
        signInLog = open("log/signIn.log", 'r')
        print "There are %s url remained after signIn function executed." % len(signInLog.readlines())

        for line in signInLog:
            account = line.split(':')[0].strip()
            uk = line.split(':')[1].strip()
            if self.logIn(account, account):
                try:
                    signInURL = "http://www.langren8.com/Service/Service.aspx?api_key=LJfi1j3MNfk1op23&method=UserGuanZhu.Login&uk=" + uk
                    playURL = "http://www.langren8.com/Service/Service.aspx?api_key=LJfi1j3MNfk1op23&method=UserGuanZhu.Play&uk=" + uk
                    urllib2.urlopen(signInURL)
                    urllib2.urlopen(playURL)
                    i += 1
                except Exception, e:
                    print e
#                     errorLogger.info(e)
                    signInLast.push(line)
            else:
                print "Login failed: %s, %s" % (account, account)
#             if(i%50==0):
#                 time.sleep(1)

        while len(signInLast) > 0:
            line = signInLast.pop()
            account = line.split(':')[0].strip()
            uk = line.split(':')[1].strip()
            if self.logIn(account, account):
                try:
                    signInURL = "http://www.langren8.com/Service/Service.aspx?api_key=LJfi1j3MNfk1op23&method=UserGuanZhu.Login&uk=" + uk
                    playURL = "http://www.langren8.com/Service/Service.aspx?api_key=LJfi1j3MNfk1op23&method=UserGuanZhu.Play&uk=" + uk
                    urllib2.urlopen(signInURL)
                    urllib2.urlopen(playURL)
                    i += 1
                except Exception, e:
                    print e
#                     errorLogger.info(e)
                    signInLast.push(line)
            else:
                print "Login failed: %s, %s"%(account, account)
#             if(i%50==0):
#                 time.sleep(1)

    def showSign(self, uk=None):
        #  must login first
        if uk:
            try:
                showSignURL = "http://www.langren8.com/Service/Service.aspx?api_key=LJfi1j3MNfk1op23&method=UserGuanZhu.Get&uk=" + uk
                result = urllib2.urlopen(showSignURL)
                print result.read()
            except Exception, e:
                print e
                print showSignURL

        else:
            filePath = open("getGold.log", 'r')
            i = 0
            for line in filePath:
                account = line.split(':')[1].strip(';')
                uk = line.split(':')[1].strip(';')
                if self.logIn(account, account):
                    try:
                        showSignURL = "http://www.langren8.com/Service/Service.aspx?api_key=LJfi1j3MNfk1op23&method=UserGuanZhu.Get&uk=" + uk
                        result = urllib2.urlopen(showSignURL)
                        i += 1
                        print uk.split(':')[0].strip(), result.read()
                    except Exception, e:
                        print e
                        print showSignURL
                else:
                    print "Login failed: %s, %s" % (account, account)
#                 if(i%50==0):
#                     time.sleep(1)
        return

def main():
    reload(sys)
    sys.setdefaultencoding('utf-8')

    # logPath = './log'
    # try:
    #     if os.path.exists(logPath):
    #         cmd = 'rm -rf %s' % logPath
    #         os.popen(cmd).read()
    #     os.makedirs(logPath)
    # except Exception, e:
    #     print e
    #
    # regLogger=logging.getLogger('register')
    # regLogfile="log/register.log"
    # regHandler=logging.FileHandler(regLogfile)
    # regLogger.addHandler(regHandler)
    # regLogger.setLevel(logging.NOTSET)
    # errorLogger=logging.getLogger('error')
    # errorLogfile="log/error.log"
    # errorHandler=logging.FileHandler(errorLogfile)
    # errorLogger.addHandler(errorHandler)
    # errorLogger.setLevel(logging.NOTSET)
    # signInLogger = logging.getLogger('signIn')
    # signInLogfile = "log/signIn.log"
    # signInHandler = logging.FileHandler(signInLogfile)
    # signInLogger.addHandler(signInHandler)
    # signInLogger.setLevel(logging.NOTSET)

    getGold = WolfKiller()
    getGold.logIn('凶残的女巫', 'sl19890920')
    start = time.time()
    print time.ctime(start)
    getGold.draw()

    #     getGold.register(10000)

    # getGold.signIn()
    #     getGold.showSign()
    #     account = 'theTest1002'
    #     password = 'theTest1002'
    #
    #     if getGold.logIn(account, password):
    #         print account,password
    #     else:
    #         print 'failed!'
    end = time.time()
    print time.ctime(end)
    print end - start

#    raw_input("Press Enter to exit....")

#   4nfst33yxoup3c55jdpfm5uo

if __name__ == "__main__":
    main()



