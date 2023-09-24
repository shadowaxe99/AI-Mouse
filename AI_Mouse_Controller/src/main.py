import voice_recognition
import mouse_control
import learning_mode

def main():
    while True:
        command = voice_recognition.VoiceRecognition().listen()
        if command == "start learning":
            learning_mode.LearningMode().record_mouse_movement()
            learning_mode.LearningMode().train_model()
            learning_mode.LearningMode().move_mouse()
        elif command == "stop learning":
            break
        elif command == "move mouse":
            mouse_control.MouseController().move_mouse(100, 100)
        elif command == "click":
            mouse_control.MouseController().click()
        elif command == "double click":
            mouse_control.MouseController().double_click()
        elif command == "right click":
            mouse_control.MouseController().right_click()
        elif command == "exit":
            break

if __name__ == "__main__":
    main()
