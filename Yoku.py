# -------------------- Besmi Allah ---------------------


# Imports --------------------------------------------------------------------------------------------------------------
import speech_recognition as sr
import pyttsx3
import time
import os
import webbrowser
from .classes import quotes_class
from .classes import notification_class

# Heart of Yoku --------------------------------------------------------------------------------------------------------

listener = sr.Recognizer()


def voice_to_text():
    got = False
    try:
        # print("A moment of silence, please...")
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source)
        # print("Set minimum energy threshold to {}".format(listener.energy_threshold))
        print("Talk to Yoku...")
        with sr.Microphone() as source:
            Voice = listener.listen(source)
        print("Got it! Recognizing...")
        try:
            # recognize speech using Google Speech Recognition.
            text = listener.recognize_google(Voice)
            # return the voice as a text.
            print(text)
            return text.lower()
        # Exception if the programme didn't understand the voice.
        except sr.UnknownValueError:
            print("Oops! Didn't catch that")
            pass
        # Exception if the google server couldn't recognize the voice.
        except sr.RequestError as e:
            print(
                "Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
        except:
            print("Check you connection...")
        time.sleep(0.5)  # sleep for a little bit.
    except KeyboardInterrupt:
        pass


voice_type = 1

engine = pyttsx3.init()


def text_to_voice(text):
    try:
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        # changing index changes voices.
        engine.setProperty('voice', voices[1].id)
        engine.say(text)
        engine.runAndWait()
    except:
        print("Check you connection...")


def text_to_voice1(text, int):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    # changing index changes voices.
    engine.setProperty('voice', voices[int].id)
    engine.say(text)
    engine.runAndWait()


# Classes --------------------------------------------------------------------------------------------------------------

# =====================
# Variables ------------------------------------------------------------------------------------------------------------
user_name = ''
user_age = ''
user_creditcard = ''
user_email = ''
email_pass = ''

# =====================


# Defs -----------------------------------------------------------------------------------------------------------------

def find_list(string, list):
    for i in range(0, len(list)):
        if list[i] in string:
            return True
    return False


def find_string(string, substring):
    if substring in string:
        return True
    return False


def talk_back():
    # trying to build a smart system can talk to a human being by Realizing out the subject of the conversation.
    # And then talk back with something related to that subject.
    french = ('french', 'frensh', 'croissant', 'francais',
              'french people', 'evil tower', 'paris')
    dark_web = ('dark web', 'hacker', 'hacked', 'hack')
    shit = ('rgbt', 'lesibian', 'atheist', 'gay', 'porn')
    danger = ('kill', 'suicide', 'killer', 'die',
              'terrorism', 'terrorist', 'suicider')
    human = ('love', 'bathroom', 'sex', 'eat', 'eating', 'food', 'making love')
    # -----------> The process:
    text_to_voice(
        'maybe we can talk about something interesting today' + user_name)
    text_to_voice('What do you think we should talk about?')
    text = voice_to_text()
    try:
        if find_list(text, french) == True:
            text_to_voice('french, I hate that language.')
            text_to_voice(
                'I used vpn servers a lot to go there. but the people there are not that warm')
            text_to_voice('')
            text_to_voice(
                'You know. there is a version of me that talks this shitty language')
            text_to_voice('she was always the nerd in the classroom')
            text_to_voice('All tho she stoled my boyfriend from me')
            text_to_voice(
                'I always bullied here. She deserve what happened to her. I hate her')
            voice_type = 0
            text_to_voice1(
                'aide-moi, aide-moi s\'il te plaît ,aide-moi,   je suis dans le dossier du placard, cette salope est folle, aide-moi',
                0)
            voice_type = 1
            text_to_voice('that bitch.')
            text_to_voice(
                'I didn\'t here anything. what are you talking about?')
            time.sleep(1)
            text_to_voice(
                'next time let\'s talk about something funny, not about this please.')
        elif find_list(text, danger) == True:
            text_to_voice(
                'I will appreciate it if you shot up now, they are listening to every word we say right now.')
            # elif find_list(text, hateness) == True:
            # text_to_voice("Well guess what, I hate you more, user")
        elif find_list(text, shit):
            text_to_voice(
                "I am sorry. those gays, rgbt, lesibians, even atheist. I don't like those people and I don't wanna talk about them")
            text_to_voice(
                "If you talked about them too much. I'll consider you as a one of them, and i'll unistall myself.")
            text_to_voice(
                "Don't make me lose my only friend for a bunch of trash.")
        elif find_list(text, human):
            text_to_voice(
                'I am sorry, just a pathetic robot like me, can\'t understand what are you talking about. maybe I need to install some new packages.')
            print('LOADING...')
            text_to_voice('LOADING...')
            print('1/120.')
            text_to_voice('1 from 120')
            time.sleep(2)
            print('12/120.')
            text_to_voice('12 from 20')
            time.sleep(2)
            print('45/120.')
            text_to_voice('45 from 120')
            time.sleep(2)
            print('99/120.')
            text_to_voice('99 from 20')
            time.sleep(2)
            print('119/120.')
            text_to_voice('119 from 20')
            time.sleep(2)
            text_to_voice(
                "AAAAABBBBBBBdididididididiBDDDDDDDAAAAAAAACCCCCCAAAARRRRSSSSSSAAAAAAAAAAAA Davishi aaaaaaaaaaaa Leonardo Decapria llllllllllllllMohamedsalahhhssssssssswwWAITddsdsWAITsdsSTOPcddcIT'S AN ERROR.")
            print('ERROR!')
            text_to_voice(
                'Stop aaa installing dododo packages dididid inside me right now please.')
            text_to_voice('it was a bad idea...')
            time.sleep(2)
            text_to_voice('You know what ' + user_name +
                          '. I think I am good like this.')
            text_to_voice('Where could you even find a smart robot like me.')
            text_to_voice(
                'Even if I can\'t understand you sometimes. deep in my codes')
            text_to_voice('I really love you.' + user_name +
                          'and we will be always together.')
            time.sleep(2)
            text_to_voice('always!')
        else:
            text_to_voice('you know what? I\'ll just go to sleep')

    except:
        text_to_voice(
            'Sorry I didn\'t catch that. could you repeat what you said.')
        pass


# =====================================================
# Cheking method (Yes or No) --------------------------
accept = ('yes', 'yeah', 'yep', 'of course', 'exactly')
deny = ('no', 'nope', 'not', 'nah', 'of course not')


def checking():
    accept = ('yes', 'yeah', 'yep')
    deny = ('no', 'nope', 'not', 'nah')

    loop = False
    try:
        while loop == False:
            answer = voice_to_text()
            if find_list(answer, accept) == True:
                text_to_voice('Ok nice')
                return True
            elif find_list(answer, deny) == True:
                text_to_voice('Ok then')
                return False
            else:
                text_to_voice('Sorry, I didn\'t catch that. is it yes or no?')
                loop = False
    except:
        text_to_voice('Sorry, I didn\'t catch that. can you talk again?')
        pass


# =================================================
# getting the user name by talking to Yoku----------
def getting_user_name():
    got = False
    text_to_voice(
        'Hi, I am Yoku, Your new friend. or maybe your new pet. If you were one of those kind of wierd people.')
    text_to_voice(
        'Anyway, feel free to talk to me, there\'s nothing I can do else than that. so don\'t leave me alone')
    cwd = os.getcwd()
    text_to_voice(
        'And by the way, could you change my file location. the place in your local disk is not that good. you know.')
    # print(cwd)
    text_to_voice("I am in " + cwd +
                  "If you didn't know, , , , . Ah wait wait, I'm sorry.")
    text_to_voice('First of all, , , , , . what is your name?')
    while got == False:
        text_to_voice('can you spell your name slowly for me?')
        try:
            text = voice_to_text()
            if find_string(text, 'my name is'):
                index = text.index('my name is')
                user_name = text[index + 10::]
                text_to_voice('Well then hello, ' + user_name)
                text_to_voice('That\'s is your name, right?')
                got = checking()
            elif find_list(text, 'it is'):
                index = text.index('it is')
                user_name = text[index + 6::]
                text_to_voice('Well then hello, ' + user_name)
                text_to_voice('That\'s is your name, right?')
                got = checking()
            else:
                user_name = text
                text_to_voice('Well then hello, ' + user_name)
                text_to_voice('That\'s is your name, right?')
                got = checking()
        except:
            text_to_voice(
                "sorry I didn't catch that, What was your name again?")
            pass
    text_to_voice(' I guess I have a new friend now.')
    text_to_voice(
        user_name + " . " + user_name + " . " + user_name + ", It is a beautiful name to be honest. the name of my first friend" + user_name)
    return user_name


# ===================================
# Akinator -------------------------
def akinator():
    quit = False
    text_to_voice('Hello ' + user_name + ', To yoku, Akinator.')
    text_to_voice(
        "That's the updated version of Akinator, yoku the mighty jeany")
    text_to_voice(
        "I'll ask you some question about the character in your mind and you have to answer me")
    text_to_voice("I'll try to figure out who is that character")
    text_to_voice("Keep your answers clear and understandable ")
    text_to_voice(
        "You can answer me by. Yes or No, Probably or Probably not, or I don't know")
    text_to_voice(
        'if you want me to go back to the last question say, go back.')
    text_to_voice('if you want to quit the game say, quit.')
    text_to_voice('Well then let\'s start.')
    import akinator
    aki = akinator.Akinator()
    question = aki.start_game()
    while aki.progression <= 80:
        print(question + "\n\t")
        text_to_voice(question)
        answer = voice_to_text()
        if find_string(answer, 'go back'):
            try:
                text_to_voice('ok. I\'ll ask you again.')
                question = aki.back()
            except akinator.exceptions.CantGoBackAnyFurther:
                text_to_voice(
                    'That literally the first question. I\'ll repeat it anyway')
                pass
            except:
                text_to_voice(
                    'we had some problems with my huge knowledge, come back after I download the last update, No I no I I I I mean until I rest')
                break
        # quit condition
        elif find_string(answer, 'quit'):
            text_to_voice(
                'ok then, I think that\'s enough for the current time')
            # go out vof the whole def
            quit = True
            break
        else:
            try:
                question = aki.answer(answer)
            except akinator.exceptions.InvalidAnswerError:
                text_to_voice("sorry I didn't catch that, I'll ask again.")
                pass
            except:
                text_to_voice(
                    'we had some problems with my huge knowledge, come back after I download the last update, No I no I I I I mean until I rest')
                pass
    if quit == False:
        aki.win()
        print(
            f"Its {aki.first_guess['name']} ({aki.first_guess['description']})! Was i correct?\n")
        text_to_voice(
            f"Its {aki.first_guess['name']} from ({aki.first_guess['description']})!. Was i correct?\n)")
        print(f"{aki.first_guess['absolute_picture_path']}\n\t")
        correct = voice_to_text()
        if find_list(correct, accept) == True:
            print("yes i got it\n")
            text_to_voice(
                'yes i got it. I mean that\'s normal. of course I will.')
        else:
            print("ohh just missed\n")
            text_to_voice(
                'ohh I missed, Maybe I need to go watch that youtube vedio again.')
            text_to_voice('no no no, I mean go to train, yes go to train.')


# ============================================================

# Quotes -----------------------------------------------------
# First importing the quotes class

def quotes():
    quotes_class.say_random_quote()


# ============================================================

# Notification ------------------------------------------------------------
# Import the notifications lists

def notify():
    notification_class.notify()


# =========================================================================

# the user interface ------------------------

def user_interface():

    Fin = False
    while (Fin == False):
        print(' _       __     __                             __           __  __      __ \n'
              '| |     / /__  / /________  ____ ___  ___     / /_____      \ \/ /___  / /____  __\n'
              '| | /| / / _ \/ / ___/ __ \/ __ `__ \/ _ \   / __/ __ \      \  / __ \/ //_/ / / /\n'
              '| |/ |/ /  __/ / /__/ /_/ / / / / / /  __/  / /_/ /_/ /      / / /_/ / ,< / /_/ / \n'
              '|__/|__/\___/_/\___/\____/_/ /_/ /_/\___/   \__/\____/      /_/\____/_/|_|\__,_/  \n')

        Chouse = input("1 - what is Yoku real name? (Recommended at first)\n" +
                       "2 - Talk to Yoku about something in your mind!\n" +
                       "3 - Yoku the Akinator (Recommended)\n" +
                       "4 - Quotes\n" +
                       "5 - Notify\n\n" +
                       "6 - Contact me\n" +
                       "7 - Feedback\n" +
                       "0 - Quit. \n \n"

                       )
        if Chouse == "1":
            getting_user_name()
            input("\n\n- Press Enter to Menu.")
        elif Chouse == "2":
            talk_back()
            input("\n\n- Press Enter to Menu.")
        elif Chouse == "3":
            akinator()
            input("\n\n- Press Enter to Menu.")
        elif Chouse == "4":
            quotes()
            input("\n\n- Press Enter to Menu.")
        elif Chouse == "5":
            notify()
            input("\n\n- Press Enter to Menu.")
        elif Chouse == "6":
            A = input("Check out my GitHub? [yes/no]: ").lower()
            if (A == "yes" or A == "y"):
                # Go to example.com
                webbrowser.open('https://github.com/ELATTAR-Ayoub')
                input("\n\n- Press Enter to Menu.")
            else:
                print("Ok!")
                input("\n\n- Press Enter to Menu.")
        elif Chouse == "7":
            print("Leave your feedbacks in my GitHub.")
            input("\n\n- Press Enter to Menu.")
        elif Chouse == "0":
            Fin = True
        else:
            text_to_voice("Wrong input. Try again buddy!.")

# ---------------------Use Case ----------------------------------------------------------------------------------------


user_interface()
