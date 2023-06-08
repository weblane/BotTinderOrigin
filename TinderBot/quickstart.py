'''
Created by Frederikme (TeetiFM)
'''

from tinderbotz.session import Session
from tinderbotz.helpers.constants_helper import *
from tinderbotz.helpers.gpt import *
import time

if __name__ == "__main__":
    #session = Session(user_data='/home/user/.mozilla/firefox/s2iziws9.google')
    session = Session(user_data='/root/.mozilla/firefox/f5iy44up.default')
    # Or if you want to use a proxy
    # AUTHORISED BY IP -> "HOST:PORT"
    # AUTHORISED BY USERNAME, PASSWORD -> "username:password@HOST:PORT"
    #session = Session(proxy="173.176.92.161:3128")

    session.set_custom_location(latitude=48.8662621247601, longitude=2.341623510348358)
    """ new_matches = session.get_new_matches(amount=3, quickload=False)
    messaged_matches = session.get_messaged_matches(amount=3)
    for match in messaged_matches:
        session.store_local(match)

    for match in messaged_matches:
        name = match.get_name()
        id = match.get_chat_id()
        conv = session.get_messages(id)
        #session.send_message(chatid=id, message=pickup_line)
        #session.send_socials(chatid=id, media=Socials.INSTAGRAM, value="Fredjemees") """

    
    # Main loop
    # Do 360 swipes (around 1h, 10sec per swipe)
    # Then permanently scan new matchs to send the first message,
    # and scan new messages to answer, during 2 hours
    # Then reswipe during 1 hour
    """ while True:
        session.like(amount=360, ratio="75%", sleep=10)

        start_time = time.time()
        while time.time() - start_time < 7200:
            new_matches = session.get_new_matches(amount=10000, quickload=False)
            for match in new_matches:
                id = match.get_chat_id()
                message = 'Salut, comment tu vas ? :)'
                session.send_message(chatid=id, message=message)
            messaged_matches = session.get_messaged_matches(amount=10000)
            for match in messaged_matches:
                id = match.get_chat_id()
                conv = session.get_messages(id)
                if conv[-1][:3] == 'me:':
                    continue
                message = generate_answer(conv)
                session.send_message(chatid=id, message=message) """

    while True:
        session.like(amount=10, ratio="75%", sleep=2)
        time.sleep(60)
        start_time = time.time()
        while time.time() - start_time < 900:
            new_matches = session.get_new_matches(amount=2, quickload=False)
            for match in new_matches:
                id = match.get_chat_id()
                message = 'Salut, comment tu vas ? :)'
                session.send_message(chatid=id, message=message)
            messaged_matches = session.get_messaged_matches(amount=10)
            for match in messaged_matches:
                id = match.get_chat_id()
                conv = session.get_messages(id)
                if conv[-1][:3] == 'me:':
                    continue
                msg_sent = len([msg for msg in conv if msg[:3] == 'me:'])
                if msg_sent < 6:
                    message = generate_answer(conv)
                    session.send_message(chatid=id, message=message)
                else:
                    message = end_conv(conv)
                    session.send_message(chatid=id, message=message)
                    session.send_socials(chatid=id, media=Socials.INSTAGRAM)

