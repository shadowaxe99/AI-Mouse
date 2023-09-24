import unittest
from unittest.mock import patch
import main


class TestMain(unittest.TestCase):
    @patch('builtins.input', side_effect=['500', '500'])
    def test_move_mouse(self, mock_input):
        with patch('voice_recognition.VoiceRecognition.listen', return_value='move mouse'):
            main.main()
            # Add assertions here

    @patch('voice_recognition.VoiceRecognition.listen', return_value='click')
    def test_click(self, mock_listen):
        main.main()
        # Add assertions here

    @patch('voice_recognition.VoiceRecognition.listen', return_value='double click')
    def test_double_click(self, mock_listen):
        main.main()
        # Add assertions here

    @patch('voice_recognition.VoiceRecognition.listen', return_value='right click')
    def test_right_click(self, mock_listen):
        main.main()
        # Add assertions here

    @patch('voice_recognition.VoiceRecognition.listen', return_value='exit')
    def test_exit(self, mock_listen):
        main.main()
        # Add assertions here

if __name__ == '__main__':
    unittest.main()
