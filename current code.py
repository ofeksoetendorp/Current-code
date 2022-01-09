#importing all of the neccesary libaries
import webbrowser
import pyjokes
import keyboard
from playsound import playsound
import datetime
#imports the games
from games import Games
#imports all the function we use
import funcs
#creating for the AI to speak
speak = funcs.speak
#saying a one time thing at the start
speak("how can I help you today?")
#for easier use of the games
game = Games()
#always running
while True:
    #does every thing in try and if it raises and error it will just say he doesn't understand
    try:
        #calls text as the main listening command
        text = funcs.takeCommand().lower()
        #if you want to add you can make it so only when a certain name is called it will listen to you
        if "" in text.lower():
            #prints the text for the user to see what the program understood
            print(text)
            #if open is found start this
            if "open" in text.lower():
                #if specificly open google is said he will open google, because with the other command it will just open an image of google
                if "open google" == text.lower():
                    webbrowser.open("www.google.com")
                    speak ("opening google")
                #if not open google do this
                else:
                    #get's the text for the website
                    website = funcs.name()
                    #opens the website
                    funcs.open(website)
                    #says he is opening that
                    speak("opening"+ text.replace("open",""))
            #a joke command will just play a funny audio file
            elif "send nudes" in text.lower():
                playsound('audio.mp3')
            elif "why am i single" in text.lower() or "am i ugly" in text.lower():
                try:
                    speak ("to close press escape")
                    funcs.camera()
                #if there isn't a camera it will raise an error and say you don't have one
                except:
                    speak ("no camera found")
            #another joke commmand will open the front camera using camera()
            #searching anything on google currently not in use for upgrading it
            elif "search" in text.lower():
                text2 = text.lower().replace("search", "").replace("luigi", "")
                funcs.search(text2)
                speak("searching" + text2)
            #get's a joke from python it self, most jokes are nerdy jokes
            elif "joke" in text.lower():
                #the language is english and it gives all jokes
                My_joke = pyjokes.get_joke(language="en", category="all")
                #speaks the joke
                speak(My_joke)
             #if you want the program to stop listening it will
            elif "pause" in text.lower():
                speak ("pausing...")
                #enters an always running while for it not to hear the user
                while True:
                    try:
                        #checks if you said "continue" if yes he will start the program again
                        check = funcs.check_true().lower()
                        if check.lower() == "continue":
                            speak ("continuing...")
                            break
                    except:
                        pass
            #opens your txt file of notes and starts writing
            elif "write a note" in text:
                file = open("note.txt", "a")
                while True:
                    try:
                        #the note get's name and listening for what the user said
                        speak("What should I write?")
                        note = funcs.name()
                        speak("Should I include date and time?")
                        #asks if you want to add date and time to the note
                        print ("yes                      no")
                        break
                    except:
                        pass
                try:
                    #checks if check is yes or no if it isn't it will return to the start of the while true
                    check = funcs.check_true().lower()
                    while True:
                        if check == "yes":
                            #get's the datetime through the libary of date time
                            e = datetime.datetime.now()
                            #makes the date as day, month, year (you can also add minutes,hours and seconds)
                            date = e.strftime((e.strftime("%d/%m/%Y")))
                            #writes the date
                            file.write(date)
                            #adds a :- for better visual exprience
                            file.write(" :- ")
                            #writes the actual note and goes down a line
                            file.write(note + '\n')
                            speak ("ok the note has been added")
                            #breaks into the main while true loop
                            break
                            #if note it will just write the note
                        elif check == "no":
                            file.write(note + '\n')
                            speak ("ok the note has been added")
                            break
                        else:
                            speak ("please choose one")
                except:
                    speak ("sorry I couldn't understand")
                #closes note
                file.close()
                #reads the note
            elif "read my note" in text.lower() or "what is my note" in text.lower():
                #opens the note
                file = open("note.txt")
                #starts reading it
                speak (file.read())
                #closes note
                file.close()
            elif "write" in text.lower():
                #writes what ever the user said
                text2 = text.lower().replace("write", "")
                keyboard.write(text2)
            #stops the program complete
            elif "stop" == text:
                speak("stopping...")
                break
            #delete your notes
            elif "delete" in text.lower():
                #opens the note with r+ meaning overwrite
                file = open("note.txt", "r+")
                #ask you to confirm to delete them
                speak ("are you sure you want to delete your notes?")
                print ("yes                        no")
                while True:
                    try:
                        check = funcs.check_true().lower()
                        if check == "yes":
                            #if yes it sets the notes to 0 value meaning nothing
                            speak ("okay deleting your notes")
                            file.truncate(0)
                            break
                        elif check == "no":
                            #if no it will just break out of the loop
                            break
                        else:
                            #will return to the start of the while true
                            speak ("please choose one")
                    except:
                        speak ("sorry couldn't understand")
            #starts the recording
            elif "record" in text.lower():
                    #listens to you until it hears 1 second of silence
                    recording = funcs.record()
                    while True:
                        try:
                            #asks the name of the file to be
                            speak("what name will you give it?")
                            name_file = funcs.name()
                            #wants to confirm if you want to name it as
                            speak("are you sure you want to save it as '" + name_file + "'")
                            print ("Yes                          No")
                            check = funcs.check_true().lower()
                            if check.lower() == "yes":
                                #of yes opens/create a file as wav and writes the recording in it, if already there is a wav file called that it will overwrite it
                                with open(name_file + ".wav", "wb") as file:
                                    file.write(recording.get_wav_data())
                                speak("saving...")
                                break
                            elif check.lower() == "no":
                                #returns to the name selection
                                pass
                            else:
                                speak ("please choose one, yes or no")
                        except:
                            speak ("sorry I couldn't understand")
                    #closes the audio file
                    file.close()
            elif "game" in text.lower():
                #asks the user which game it wants to play
                speak("which game should we play?")
                print ("tic tac toe       snake       ball(pong)")
                while True:
                    try:
                        #checks the game and says how to play them
                        check = funcs.check_true().lower()
                        if check == "snake":
                            speak ("the keys are the arrow keys")
                            game.snake()
                            break
                        elif "tic-tac-toe" in check:
                            game.tictactoe()
                            break
                        elif check == "ball":
                            speak ("the keys are w and s")
                            game.pong()
                            break
                        elif check == "stop":
                            break
                        else:
                          speak("please choose one")
                    except:
                        speak ("sorry I don't understand")
                        break
            #for playing the audio files you recorded
            elif "play" in text.lower():
                speak ("which file should I play?")
                try:
                    #get's the name of the file and plays it
                    name_file = funcs.name()
                    funcs.play(name_file)
                except:
                    #if the files does not exist it will raise an error and go to the except and it will say it
                    speak("sorry the file '" + name_file + "' does not exist")
            elif "change my name" in text.lower():
                #will change your name to your choosing
                file = open("name.txt", "r+")
                speak("ok what should I change it to?")
                while True:
                    try:
                        #asks to what to change and gets it
                        username = funcs.name()
                        speak ("are you sure you want to change it to " + username)
                        print ("yes                      no")
                        #asks you to confirm
                        check = funcs.check_true().lower()
                        if check == "yes":
                            #if it is yes it will delete the name and write it for what you said
                            file.truncate(0)
                            file.write(username)
                            break
                        elif check == "no":
                            #if no it will return to the while true
                            speak ("ok what should I change it to then?")
                        else:
                            speak ("please choose one yes or no")
                    except:
                        speak ("sorry I don't understand")
                #says your name
                speak ("ok your name is now " + username)
                #closes file
                file.close()
            elif "my name" in text.lower():
                #opens the name and reads the name
                file = open("name.txt")
                username = file.read()
                if username == "":
                    #if user did not have a previous name it will say it
                    speak ("you don't have a name. what should I call you?")
                    while True:
                        try:
                            #asks to what to call you and gets it
                            username = funcs.name()
                            speak("are you sure you want me to name you " + username)
                            print ("yes                       no")
                            check = funcs.check_true().lower()
                            #confirms if you want to name your self as that
                            if "yes" == check:
                                #if yes it opens name text and starts to write
                                file = open("name.txt", "w")
                                file.write(username)
                                speak ("okay your name is now " + username)
                                break
                            elif "no" == check:
                                #returns to the while true start
                                speak ("okay what is your name then?")
                            else:
                                speak ("please choose yes or no")
                        except:
                            pass
                else:
                    #if the user already has a name it will say it
                    speak("your name is " + username)
                #closes file
                file.close()
            elif 'the time' in text.lower():
                #get's the time
                e = datetime.datetime.now()
                #speaks the time as hour, minute and seconds
                speak("the time is "+ (e.strftime("%H:%M:%S")))
            elif "what day is it" in text.lower() or "what day is today" in text.lower():
                #get's the time and speaks it as the day(sunday,monday ect.), month, day (08 or 12 ect) and year
                e = datetime.datetime.now()
                speak ("today is " + (e.strftime("%a, %b %d, %Y")))
            else:
                #if no one of the command is used it will say he doesn't understand
                speak ("sorry I don't understand")
    except UnboundLocalError:
    #if the error is specificly not getting any text it will just return the the start of while true
        pass
