import pyttsx3
friend = pyttsx3.init()
text = input("Please say something: ")
friend.say(text)
friend.runAndWait()
