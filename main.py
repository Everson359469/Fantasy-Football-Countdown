#!/usr/bin/python3 
# This python script will calculate and communicate the exact number of days until the event you input# import datetime 
import smtplib 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import logging,sys
import random
import datetime
logging.basicConfig(level=logging.DEBUG)
dars_logger = logging.getLogger("dars_logger")
stdout = logging.StreamHandler(stream=sys.stdout)

fmt = logging.Formatter(
    "%(name)s: %(asctime)s | %(levelname)s | %(filename)s%(lineno)s | %(process)d >>> %(message)s" )


stdout.setFormatter(fmt)

dars_logger.addHandler(stdout)
fh = logging.FileHandler('/home/ubuntu/foosball_alerts.log')
fh.setLevel(logging.DEBUG)
dars_logger.addHandler(fh)

dars_logger.info("Let's do this...")

def send_email(subject, mms_subject, body, sender, recipients, password):
    dat_image = 'BobOblaw'
    for recipient in recipients:
        msg = MIMEMultipart()
        if 'gmail.com' in recipient:
            msg['Subject'] = subject
        else:
            msg['Subject'] = mms_subject
        msg['From'] = sender
        msg['To'] = recipient
        body_text = MIMEText(body,'html')
        #print("DEBUG: body_text is {}".format(body_text)) 
        if recipient:
            msg.attach(body_text)
            #text = MIMEText('<img src="cid:image1">', 'html') 
            #msg.attach(text) 

    #Images = [https://www.google.com/search?sca_esv=5bdde8b43c3acd18&sxsrf=ACQVn0-pvTx3yh0Y0xswdvSQRLGe6oKK9A:1708969389875&q=christian+mccaffrey&tbm=isch&source=lnms&prmd=invhsmbt&sa=X&sqi=2&ved=2ahUKEwjt_KiLx8mEAxVY5MkDHR66CKoQ0pQJegQICxAB&biw=1690&bih=872&dpr=2#imgrc=nb1bI74l5JidIM, https://www.google.com/search?q=12th+man&tbm=isch&ved=2ahUKEwjtwZOMyMmEAxU478kDHUW3Bc8Q2-cCegQIABAA&oq=12th+man&gs_lp=EgNpbWciCDEydGggbWFuMgQQIxgnMgQQIxgnMgoQABiABBiKBRhDMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABEisElDvAliCEnABeACQAQCYAT-gAakDqgEBN7gBA8gBAPgBAYoCC2d3cy13aXotaW1nwgIHEAAYgAQYGMICBhAAGAUYHsICBhAAGAgYHogGAQ&sclient=img&ei=vM7cZe3zArjep84Pxe6W-Aw#imgrc=U1sORik7GnRvUM&imgdii=6JIjow8dU5qWtM, ]
        image = MIMEImage(open('/home/ubuntu/cmac.jpeg', 'rb').read())
        image2 = MIMEImage(open('/home/ubuntu/ags.jpeg', 'rb').read())
        image3 = MIMEImage(open('/home/ubuntu/12.gif', 'rb').read())

        dars_images = [image,image2,image3]
        # Define the image's ID as referenced in the HTML body above 
        #image.add_header('Content-ID', '<image1>') 
        dis_image = random.choice(dars_images)
        while True:
            if dis_image == dat_image:
                dis_image = random.choice(dars_images)
            else:
                break
        msg.attach(dis_image)
        dat_image = dis_image
       # if 'gmail.com' in recipient: 
         #   msg.attach(image2) 
        #    msg.attach(image3) 
       # msg.attach(body) 
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.set_debuglevel(1)
        smtp_server.login(sender, password)
        smtp_server.sendmail(sender, recipient, msg.as_string())
    dars_logger.info("Messages sent!")

def calculate_days():
    today = datetime.date.today()
    # NFL Playoffs 
    nfl_playoffs_future = datetime.date(2025,1,11)
    print(nfl_playoffs_future)
    nfl_playoffs_diff = nfl_playoffs_future - today
    #Fantasy football 
    fantasy_playoffs_future = datetime.date(2024, 12, 20)
    print(fantasy_playoffs_future)
    fantasy_playoffs_diff = fantasy_playoffs_future - today
    #College football 
    college_playoffs_future = datetime.date(2024,12,12)
    print(college_playoffs_future)
    college_playoffs_diff = college_playoffs_future - today
    # Super Bowl
    super_bowl_future = datetime.date(2025,2,9)
    print(super_bowl_future)
    super_bowl_diff = super_bowl_future - today
    days_until_football =f"""\ 
    <html> 
        <head> 
            <title>FOOTBALL IS COMING!!!</title> 
            <style> 
                table,tr,th,td {{ border:1px solid black;}}
            </style> 
        </head> 
        <body> 
            <p><strong><mark><i>FOOTBALL IS COMING!!!!</i></mark></strong><br><br> <table> 
            <tr> 
                <th scope="col" style="text-align: center">Event</th> 
                <th scope="col" style="text-align: center">Days Until Event</th> 
            </tr>
            <tr> 
                <td>NFL Season</td> 
                <td style="text-align: center">{nfl_playoffs_diff.days}</td> 
            </tr> 
            <tr> 
                <td>Fantasy Football</td> 
                <td style="text-align: center">{fantasy_playoffs_diff.days}</td> 
            </tr>  
            <tr> 
                <td>TAMU Football</td> 
                <td style="text-align: center"> {college_playoffs_diff.days}</td> 
            </tr> 
        </table> 
        </p> 
    </body> 
</html> 
"""
    mms_subject = " NFL Playoffs: {} days. Fantasy Football Playoffs: {} days. CFP: {} days. Super Bowl: {} days.".format(nfl_playoffs_diff.days,fantasy_playoffs_diff.days, college_playoffs_diff.days, super_bowl_diff.days)
    return (fantasy_playoffs_diff,days_until_football,mms_subject)
# Email background information 
days_until,body,mms_subject = calculate_days()
email_subject = "{} Days Until Football Event".format(days_until.days)
sender = "eversonsmith30@gmail.com"
google_password = "mcglibpvbptmlvow"
email_recipients = ["eversonsmith30@gmail.com", "5124848182@mms.att.net"]
send_email(email_subject, mms_subject, body, sender, email_recipients, google_password)
