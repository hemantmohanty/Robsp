import pyttsx3

if __name__ == '__main__':
    print("Welcome to roboSpeaker 1.1 Created by Hemant!")
    while True:
        x = input("Enter what you want me to speak: ")
        if x == 'q':
            break
        engine = pyttsx3.init()
        engine.say(x)
        engine.runAndWait()
