from ftplib import FTP
import os 

ftp = FTP('')
ftp.connect('localhost',21)
ftp.login("user","12345")
os.chdir('D:/Client')
#ftp.cwd('C:/Server/user') #replace with your directory
ftp.retrlines('LIST')

def uploadFile():
 filename = 'Hello.txt' #replace with your file in your home folder
 ftp.storbinary('STOR '+filename, open(filename, 'rb'))
 ftp.quit()

def downloadFile():
 filename = 'Finger_Tap_Single_Videvo.mov' #replace with your file in the directory ('directory_name')
 localfile = open(filename, 'wb')
 ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
 ftp.quit()
 localfile.close()


#uploadFile()
downloadFile()