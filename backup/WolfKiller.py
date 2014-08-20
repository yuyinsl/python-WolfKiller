import urllib2,cookielib
import re
import logging
import os


class WolfKiller:  

    def __init__(self):
        self.logInURL="http://www.langren8.com/loginaction.aspx"
        self.userInfoURL="http://www.langren8.com/Service/Service.aspx?api_key=LJfi1j3MNfk1op23&method=ClientUser.GetLoginedUserInfo"     
        self.cookie = cookielib.CookieJar()
        self.httpcookie = urllib2.HTTPCookieProcessor(self.cookie)
        self.opener = urllib2.build_opener(self.httpcookie)
        urllib2.install_opener(self.opener)       
        
    
    def register(self,startNum,n):
        num=startNum
        while num<(startNum+n):
            username="wolfkiller"+str(num)
            pwd="wolfkiller"
            registerURL="http://www.langren8.com/Service/service.aspx?api_key=LJfi1j3MNfk1op23&method=User.Reg&un="+username+"&nn="+username+"&qq=982932568&tel=&pwd=wolfkiller&email=wolfkiller@126.com&sex=true&body=1&head=1&hair=1&eye=1&eyebrow=1&ear=1&nose=1&mouth=1&tjid=0"
            urllib2.urlopen(registerURL)
            if self.logIn(username,pwd):
                uk=self.getUK()
                logger.info(uk)
            num=num+1

        
    def logIn(self,username,pwd):    
        enparams="username="+username+"&pwd="+pwd
        headers = {'Content-Type':'application/x-www-form-urlencoded','Connection':'Keep-Alive'}
        request = urllib2.Request(url = self.logInURL,headers = headers,data=enparams)
        stream=urllib2.urlopen(request)
        result=stream.read()
        if result.find('Game')==-1:
            return False
        else:
            return True
        
        
    def getInfo(self):
        stream = urllib2.urlopen(self.userInfoURL).readlines()
        p='<\w+>[^<]+</\w+>'
        result=re.findall(p,stream[0])
        for element in result:
            print element
            
            
    def getUK(self):
        stream = urllib2.urlopen(self.userInfoURL).readlines()
        p='>[^<]+<'
        result=re.findall(p,stream[0])
        uk=result[0].strip('<>')
        return uk
    
    
    def signIn(self):
        filePath=open("getGold.log",'r')
        for uk in filePath:
            signInURL1="http://www.langren8.com/Service/Service.aspx?api_key=LJfi1j3MNfk1op23&method=UserGuanZhu.Login&uk="+uk
            signInURL2="http://www.langren8.com/Service/Service.aspx?api_key=LJfi1j3MNfk1op23&method=UserGuanZhu.Play&uk="+uk
            urllib2.urlopen(signInURL1)
            urllib2.urlopen(signInURL2)
            
            
    def showSign(self):
        filePath=open("getGold.log",'r')
        for uk in filePath:
            showSignURL="http://www.langren8.com/Service/Service.aspx?api_key=LJfi1j3MNfk1op23&method=UserGuanZhu.Get&uk="+uk
            result=urllib2.urlopen(showSignURL)
            print result.read()
        return
   

if __name__ == "__main__":
    logger=logging.getLogger()
    logfile="getGold.log"
    handler=logging.FileHandler(logfile)
    logger.addHandler(handler)
    logger.setLevel(logging.NOTSET)
    getGold = WolfKiller()

#    getGold.register(501, 500)
#    getGold.signIn()
#    getGold.showSign()


#    getGold.logIn("wolfkiller500", "wolfkiller")
#    getGold.getInfo()
    print 'end'
    
    
    
    
    
    
    
    
    
    
    
    
