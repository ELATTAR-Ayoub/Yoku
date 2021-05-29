# This is the class of the quotes


import random
import time
from ..Yoku import text_to_voice

# ========================


class quote:
    # this will help us write quoteX = quote(text, saider, desc)
    def __init__(self, text, sayer, desc):
        self.text = text
        self.sayer = sayer
        self.desc = desc

    def say_quote(self):
        try:
            print(f"{self.text} \n ~{self.sayer} ({self.desc}).")
            text_to_voice(self.text)
            time.sleep(1)
            text_to_voice('it was from ' + self.sayer + ',from ' + self.desc)
        except:
            text_to_voice('maybe next time.')


# The quotes list
quote_list = []

quote1 = quote(
    "I am the hope of the universe, I am the answer to all living things that cry out for peace, I am protector of the innocent, I am the light in the darkness. I am truth. Ally to good! Nightmare to you!", "Son Goku", "Dragon ball Z.")
quote_list.append(quote1)

quote2 = quote(
    "The world isn't perfect. But it's there for us, doing the best it can....that's what makes it so damn beautiful.",
    "Roy Mustang", "Full Metal Alchemist")
quote_list.append(quote2)

quote3 = quote(
    "We are all like fireworks: we climb, we shine and always go our separate ways and become further apart. But even when that time comes, let's not disappear like a firework and continue to shine.. forever.", "Hitsugaya Toshiro", "Bleach.")
quote_list.append(quote3)

quote4 = (
    "Those who stand at the top determine what's wrong and what's right! This very place is neutral ground! Justice will prevail, you say? But of course it will! Whoever wins this war becomes justice!", "Don Quixote Doflamingo", "One piece.")
quote_list.append(quote4)

quote5 = quote(
    "Religion, ideology, resources, land, spite, love or just because… No matter how pathetic the reason, it’s enough to start war. War will never cease to exist… reasons can be thought up after the fact… Human nature pursues strife.", "Pain", "Naruto Shippuden")
quote_list.append(quote5)


# =====================
def say_random_quote():
    # Finally let Yoku randomly say one of the quotes
    random_int = random.randint(0, len(quote_list) - 1)
    quote_list[random_int].say_quote()
