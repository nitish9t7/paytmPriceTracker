import requests
from bs4 import BeautifulSoup
import smtplib

URL = input('Enter The Product URL')
header = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

def check():
    page = requests.get(URL, headers=header)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find('h1', {'class': 'NZJI'}, {'data-reactid': '167'}).text

    price = (soup.find('span', {'class': '_1V3w'}, {'data-reactid': '171'}).text)
    price = int(price.replace(',', ''))

    if price < 8000:
        print("boooyahh")
        sendMail()

    print(title)
    print(price)



def sendMail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    #loginID= input('Login Id :  ')
    #appPass= input("App Password :  ")
    #tkumvrppbcffircg
    server.login('nitish9t7@gmail.com', 'udidmvzbwrpaoumf')

    subject = 'price fell down'
    body = URL
    msg = f"Subject: { subject}\n\n{body}"

    server.sendmail(
        'nitish9t7@gmail.com',
        input('To:  '),
        msg
    )
    server.quit()
    print('sent')


check()
