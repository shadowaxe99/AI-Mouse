import unittest
from voice_recognition import VoiceRecognition

class TestVoiceRecognition(unittest.TestCase):
    def test_listen(self):
        voice_recognition = VoiceRecognition()
        command = voice_recognition.listen()
        # Add assertions here

if __name__ == '__main__':
    unittest.main()
