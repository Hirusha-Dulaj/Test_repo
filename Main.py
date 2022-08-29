import schedule
import time
import os
from twilio.rest import Client

def job():
	account_sid = 'AC713ee05b931d2914accbdf18245294a2'
	auth_token  = '64b324731de881e3d2d2eb3def56aff5'
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