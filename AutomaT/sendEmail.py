import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime

# current date
now = datetime.datetime.now()

# extracting Hacker News


def extract_news(url):
    print("Extracting Hacker News Stories...")

    # connecting and getting the "new title"
    connection = requests.get(url)
    html_text = connection.text
    bs4 = BeautifulSoup(html_text, "lxml")
    news_title = bs4.find_all("a", class_="titlelink")

    return "".join(f'{str(i+1)} :: {title_tag.text}----' + title_tag.get("href") + "\n" for i, title_tag in enumerate(news_title))


content = extract_news("https://news.ycombinator.com/")

# print(content)

print("Composing Email")

# Email details

SERVER = "smtp.gmail.com"
PORT = 587
FROM = "2320161150@estudiantesunibague.edu.co"
TO = ["juanfelipehdezm@gmail.com", "paulausechec@gmail.com"]
PASS = "**********"

# message body
msg = MIMEMultipart()

msg["Subject"] = "TOP News Stories HN [Automated Email]" + " " + \
    str(now.day) + "-" + str(now.month) + "-" + str(now.year)

msg["From"] = FROM
msg["To"] = TO

# adding the email body which is what we extracted from the HN page
msg.attach(MIMEText(content, "html"))

print("Initiating Server...")

server = smtplib.SMTP(SERVER, PORT)
server.set_debuglevel(1)  # 1 if i want to see errors of connection, 0 if not
server.ehlo()
server.starttls()
server.login(FROM, PASS)
server.sendmail(FROM, TO, msg.as_string())

print("Email Sent...")

server.quit()

print(content)
