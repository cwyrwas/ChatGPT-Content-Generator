import pyttsx3


def save_audio(script, current_working_dir, file_name):
    engine = pyttsx3.init()
    voice = engine.getProperty('voices') #get the available voices
    engine.setProperty('voice', voice[1].id) #changing voice to index 1 for female voice
    engine.setProperty('rate', 165) # setting the speed of the voice
    engine.save_to_file(script, current_working_dir + "/audio/" + file_name + ".mp3")
    engine.runAndWait()

