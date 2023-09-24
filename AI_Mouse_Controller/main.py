import voice_recognition
import mouse_control
import learning_mode
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    while True:
        command = voice_recognition.VoiceRecognition().listen()
        if command == "start learning":
            logging.info('Starting learning mode...')
            learning_mode.LearningMode().load_model()
            learning_mode.LearningMode().record_mouse_movement()
            learning_mode.LearningMode().train_model()
            learning_mode.LearningMode().move_mouse()
            logging.info('Learning mode completed.')
        elif command == "stop learning":
            break
        elif command == "move mouse":
            x = int(input('Enter the X coordinate: '))
            y = int(input('Enter the Y coordinate: '))
            mouse_control.MouseController().move_mouse(x, y)
        elif command == "click":
            mouse_control.MouseController().click()
        elif command == "double click":
            mouse_control.MouseController().double_click()
        elif command == "right click":
            mouse_control.MouseController().right_click()
        elif command == "exit":
            break
        else:
            logging.warning('Invalid command. Please try again.')

if __name__ == "__main__":
    main()
