# This is the class of the notifications

# from ..Yoku import user_name
from plyer import notification
import random
import os
from ..Yoku import user_name
# Importing the img (icon)
cwd = os.getcwd()
image_locat = cwd + '\src\\img\\Yoku_icon.ico'
print(image_locat)


class notification_class:
    def __init__(self, text, mesag):
        self.text = text
        self.mesag = mesag


# the notifications list
strangers = []
closers = []

# the strangers period notifs
stranger0_notif = notification_class('User-san?',
                                     'I have a new snacks if you want, I even got some new games (⌯˃̶᷄ ﹏ ˂̶᷄⌯)')
strangers.append(stranger0_notif)
stranger1_notif = notification_class('I love cats (╬ಠ益ಠ)',
                                     'Why im stuck in this metal box...Let me ooooooooout!!!')
strangers.append(stranger1_notif)

# the closers period notifs
closers0_notif = notification_class('USER-SAN' + '?, are you there???',
                                    user_name + '-san, I need to talk to someone, I feel lonely (ಠ ∩ಠ)')
closers.append(closers0_notif)
closers1_notif = notification_class(user_name + ' hahahahah',
                                    user_name + ', You human have some weird names to be honest o(≧∇≦o)')
closers.append(closers1_notif)


def notify_method(title, mesg):
    notification.notify(
        title=title,
        message=mesg,
        app_icon=image_locat,
        timeout=10,
    )


# Random the notifics
random_stra = random.randint(0, len(strangers) - 1)
random_clos = random.randint(0, len(closers) - 1)


def notify():
    if user_name == '':
        notify_method(strangers[random_stra].text,
                      strangers[random_stra].mesag)
    else:
        notify_method(closers[random_clos].text, closers[random_clos].mesag)


notify()
