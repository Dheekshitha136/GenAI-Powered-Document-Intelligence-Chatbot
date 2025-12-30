def speak(text:str,enable_voice: bool=False):
    if not enable_voice:
        return
    try:
        import pyttsx3
        engine=pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    except Exception:
        pass
