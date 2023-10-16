import os
from twilio.rest import Client

def sendsms():

    # Find your Account SID and Auth Token at twilio.com/console
    # and set the environment variables. See http://twil.io/secure
    account_sid = "ACd529c0b158503a0aead4db34d59ac39e"
    auth_token = "d23e17e0e9d0f2ffbf8d0ada62a1adc5"
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body="Checklist send to You Please check...!.",
                        from_='+14253584249',
                        to='+91 8459909882'
                    )
