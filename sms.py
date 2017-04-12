# sms.py
# Python 3.5

"""
Python library to send SMS using Twilio API
src: https://www.twilio.com/blog/2016/10/how-to-send-an-sms-with-python-using-twilio.html
"""

from twilio.rest import Client
from IGNORE import twilio_secrets

# Define constants
TWILIO_ACCOUNT_SID = twilio_secrets.TWILIO_AUTH["TWILIO_ACCOUNT_SID"]
TWILIO_AUTH_TOKEN = twilio_secrets.TWILIO_AUTH["TWILIO_AUTH_TOKEN"]

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

TWILIO_MOBILE = twilio_secrets.TWILIO_MOBILE["UK"]
RECIEVER_MOBILE = twilio_secrets.RECIEVER_MOBILE["ME"]  # Verified receiver number

def send_sms(msg_body):
    """
    function to send sms using Twilio API
    TODO: Configure receiver mobile through parameter
    """
    msg = client.messages.create(body=msg_body,
                                from_ = TWILIO_MOBILE,
                                to = RECIEVER_MOBILE)

    return msg.status

if __name__ == "__main__":
    """ starting block """

    status = send_sms("Hi, This is a sms sent by me")
    print(status)
