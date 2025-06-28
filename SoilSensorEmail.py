import RPi.GPIO as GPIO
import time
import random
import smtplib
from email.message import EmailMessage

from_email_addr = "1354267684@qq.com"
from_email_pass = "zbivegopkacvffbd"
to_email_addr = "1354267684@qq.com"

channel = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

def read_soil_moisture():
    return random.randint(0, 100)

def send_email(message):
    msg = EmailMessage()
    msg.set_content(message)
    msg['From'] = from_email_addr
    msg['To'] = to_email_addr
    msg['Subject'] = f"Plant Status Update: {time.strftime('%Y-%m-%d %H:%M:%S')}"
    
    try:
        server = smtplib.SMTP('smtp.qq.com', 587)
        server.starttls()
        server.login(from_email_addr, from_email_pass)
        server.send_message(msg)
        server.quit()
        print('Email sent successfully')
    except Exception as e:
        print(f"Failed to send email: {e}")

def check_soil_moisture():
    soil_moisture = read_soil_moisture()
    print(f"Current soil moisture: {soil_moisture}%")
    
    if soil_moisture < 30:
        return "Please water your plant."
    elif soil_moisture > 60:
        return "Water NOT needed."
    else:
        return "Soil moisture is sufficient."

def daily_check():
    for i in range(4):
        print(f"Reading {i+1}:")
        status = check_soil_moisture()
        send_email(status)
        time.sleep(6 * 60 * 60)

if __name__ == "__main__":
    daily_check()
