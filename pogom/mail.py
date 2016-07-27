import logging
import yagmail
from datetime import datetime
from mailjet import Client

key = 'key-879026018cfa93cd484a3a819b218339'
sandbox = 'sandbox2689eea951c741a79298ac186e00ebe0.mailgun.org'

log = logging.getLogger(__name__)

mail_list =['rikkajounin@gmail.com'
            #,'Biagiopain@hotmail.it'
            #,'Samuele.banchelli@gmail.com'
            ]


def send(name, lat , long, timeString):
    subject =  '{} appears!'.format(name)
    mapString ='https://www.google.com/maps/place/{}+{}/@{},{},15z'.format(lat, long, lat, long)

    time = 'disappear time: {}'.format(timeString)
    text = '{} appears... coordinates:\n {} \n'.format( name, mapString, ), time, '\n'

   #yag = yagmail.SMTP('davidegiretti@gmail.com', 'heisenberg44')

    for email in mail_list:
        #yag.send(email, subject, text)
        api_key = "d5cd7c3268efce6a2174114bdfbfc4af"
        api_secret = "e0ae54a66eacbf0a1fc81b9f5a59683c"
        mailjet = Client(auth=(api_key, api_secret))
        data = {
          'FromEmail': 'davidegiretti@gmail.com',
          'FromName': 'davide giretti',
          'Subject': subject,
          'Text-part': text,
          'Recipients': [
        				{
        						"Email": email
        				}
        		]
        }
        result = mailjet.send.create(data=data)
