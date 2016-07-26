import logging
import yagmail
from datetime import datetime



log = logging.getLogger(__name__)

mail_list =['rikkajounin@gmail.com'
            ,'Biagiopain@hotmail.it'
            ,'Samuele.banchelli@gmail.com'
            ]


def send(name, lat , long, timeString):
    subject =  '{} appears!'.format(name)
    mapString ='https://www.google.com/maps/place/{}+{}/@{},{},15z'.format(lat, long, lat, long)

    time = 'disappear time: {}'.format(timeString)
    text = '{} appears... coordinates:\n {} \n'.format( name, mapString, ), time, '\n'

    yag = yagmail.SMTP('davidegiretti@gmail.com', 'heisenberg44')

    for email in mail_list:
        yag.send(email, subject, text)
