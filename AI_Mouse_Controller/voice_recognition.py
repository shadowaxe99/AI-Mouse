import speech_recognition as sr
import logging

class VoiceRecognition:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def listen(self):
        with sr.Microphone() as source:
            logging.info('Listening...')
            audio = self.recognizer.listen(source)
            try:
                command = self.recognizer.recognize_google(audio)
                logging.info(f'Recognized command: {command}')
                return command
            except sr.UnknownValueError:
                logging.warning('Could not understand audio')
                return None
            except sr.RequestError as e:
                logging.error(f'Could not request results; {e}')
                return None
