import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText


number = random.randint(1, 21)

my_email = "Your Email"
password = "Your Password"

message = MIMEMultipart()
message['Subject'] = 'Capibara Daily'
message['From'] = 'Your Email'
message['To'] = 'Destination Email'

with open("quotes.txt") as quote_file:
    all_quotes = quote_file.readlines()
    quote = random.choice(all_quotes)

# Open the file as binary mode
with open(f"./photos/capi-{number}.jpg", 'rb') as f:
    img = MIMEImage(f.read())
    img.add_header('Content-Disposition', 'attachment', filename=f"capi-{number}.jpg")
    message.attach(img)

msgText = MIMEText(quote, 'html')
message.attach(msgText)

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.ehlo()
    connection.starttls()
    connection.ehlo()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="Destination Email",
        msg=message.as_string()
    )
