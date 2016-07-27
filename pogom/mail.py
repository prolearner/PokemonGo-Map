import logging
import yagmail
from datetime import datetime
import requests

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

        request_url = 'https://api.mailgun.net/v3/{0}/messages'.format(sandbox)
        request = requests.post(request_url, auth=('api', key), data={
            'from': 'hello@example.com',
            'to': email,
            'subject': subject,
            'text': text
        })

        print 'Status: {0}'.format(request.status_code)
        print 'Body:   {0}'.format(request.text)
