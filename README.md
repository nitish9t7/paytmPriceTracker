# paytmPriceTracker
This script will send you an email when the price for specific items you followed on Paytm drops beneath a certain price you set.

You can parse the price without Paytm API !

# Installation
pip install -r requirements.txt

Then you need to edit the config.json first,

1. email → sender, sender-password, receivers
2. amazon-base_url (change to amazon store where your target item is)
3. item-to-parse (add item id which you want to track)
After installed required package and finished config.json, you can use it by python crawler.py

# Required Accounts
1. Google Mail

# Dependencies
Python 2
lxml
json
requests
smtplib
MIMEText
ConfigParser, argparse, urlparse
# Future feature
1. Direct message notification via Twitter
2. Direct message notification via Telegram
