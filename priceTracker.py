import time
import requests
from bs4 import BeautifulSoup
import smtplib
URL = input('Enter The Product URL')    //URL of Product
header = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
to = input("To : ")                     //Email of Reciever
def check():
    page = requests.get(URL, headers=header)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find('h1', {'class': 'NZJI'}, {'data-reactid': '167'}).text
    price = (soup.find('span', {'class': '_1V3w'}, {'data-reactid': '171'}).text)
    price = int(price.replace(',', ''))
    if price <8000:
        print("Price Fell Down, sending mail")
        sendMail()
    print(title)
    print(price)
def sendMail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('*******@gmail.com', '**************')             //loginId and Apppassword of Sender

    subject = 'price fell down'
    body = URL
    msg = f"Subject: { subject}\n\n{body}"
    server.sendmail(
        '********@gmail.com',                           // Email of Sender
        to,                                                // Emailof Reciever
        msg                                                 // Message 
    )
    server.quit()
    print('sent')
while(True):                                                   //checking at Specified interval of time
    check()
    time.sleep(3)						//Sleep
