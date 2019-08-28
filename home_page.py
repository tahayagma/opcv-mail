import os
import datetime
from PyQt5 import QtWidgets,QtCore,QtGui
import smtplib
#import cv2
import sys
import time
from subprocess import PIPE,Popen
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


class home(object):
        def home_fonk(self,wr):
            wr.setWindowTitle("Python Programing")
            wr.setFixedSize(500,200)
            self.zaman = QtWidgets.QLabel(wr)
            self.zaman.setStyleSheet("background-color: white;")
            self.zaman.setGeometry(QtCore.QRect(10,10,180,20))
            self.saat = datetime.datetime.now()
            self.clock = datetime.datetime.strftime(self.saat,"Tarih:%x Saat:%X")
            self.zaman.setText(self.clock)
            self.buttton = QtWidgets.QPushButton(wr)
            self.buttton.setGeometry(QtCore.QRect(10,50,60,25))
            self.buttton.setText("Bas")
            self.buttton.clicked.connect(self.ipconfig)
        def ipconfig(self):
            ip = "ipconfig"
            p = Popen(ip,shell=True,stderr=PIPE,stdout=PIPE)
            (one,err) = p.communicate()
            stir = str(one)
            new = stir.split(r"\r\n")
            al = new[27:]
            calling = "\r\n".join(al)
            print(calling)


            all_show = "netsh wlan show profile"
            p_1 = Popen(all_show, shell=True, stderr=PIPE, stdout=PIPE)
            (two, err) = p_1.communicate()
            new_1 = str(two[175:])
            sonu = new_1.split(r"\r\n")
            tp = sonu[0:40]
            out = "\r\n".join(tp)
            print("Bağlanılan Ağlar:",out)


            my_wifi = 'NETSH WLAN SHOW INTERFACE | findstr /r "^....SSID"'
            pis = Popen(my_wifi, shell=True, stderr=PIPE, stdout=PIPE)
            (tri, err) = pis.communicate()

            four = str(tri)
            wifi_name = four[31:-5]
            print("Ağ Adı:",wifi_name)
            komut_2 = 'netsh wlan show profile {} key = clear'.format(wifi_name)
            pel = Popen(komut_2, shell=True, stderr=PIPE, stdout=PIPE)
            (five, erri) = pel.communicate()

            outm = str(five)
            newi = outm.split(r"\r\n")
            liste = list(newi)
            password = liste[32]
            tp = tuple(password)
            last = tp[29:]
            cv = "".join(last)
            print("Ağ Şifresi:",cv)










if __name__== '__main__':
    app = QtWidgets.QApplication(sys.argv)
    wind= QtWidgets.QWidget()
    iln = home()
    iln.home_fonk(wind)
    wind.show()
    sys.exit(app.exec_())