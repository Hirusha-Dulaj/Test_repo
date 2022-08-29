import schedule
import time
import os
from twilio.rest import Client

def job():
	account_sid = 'AC713ee05b931d2914accbdf18245294a2'
	auth_token  = '3104e6ad80d25dc9a3bac8ec53140dbc'
	client = Client(account_sid, auth_token)

	from_whatsapp_number = 'whatsapp:+14155238886'
	to_whatsapp_number = 'whatsapp:+94763705333'

	message = client.messages.create(body='Good Moring!',
		media_url='https://source.unsplash.com/random/?productivity,Girl',
		from_=from_whatsapp_number,
		to=to_whatsapp_number)

	print(message.sid)



# schedule.every(1).seconds.do(job)
schedule.every(2).seconds.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
