import smtplib
import imghdr
from email.message import EmailMessage
SENDER="kathikarthik972@gmail.com"
receiver="kathikarthik972@gmail.com"
password="efvddgwksaauqmog"
def send_email(image_path):
    email_msg=EmailMessage()
    email_msg["Subject"]="new email showed up"
    email_msg.set_content("hey, we just saw a new customer!")

    with open(image_path, "rb") as file:
        content = file.read()
    email_msg.add_attachment(content,maintype="image",subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER,password)
    gmail.sendmail(SENDER,receiver,email_msg.as_string())
    gmail.quit()
if __name__=="__main__":
    send_email("images/0.png")