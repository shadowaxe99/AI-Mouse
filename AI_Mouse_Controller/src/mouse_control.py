import pyautogui

class MouseController:
    def __init__(self):
        self.screen_width, self.screen_height = pyautogui.size()

    def move_mouse(self, x, y):
        pyautogui.moveTo(x, y)

    def click(self, button='left'):
        pyautogui.click(button=button)

    def double_click(self):
        pyautogui.doubleClick()

    def right_click(self):
        pyautogui.click(button='right')

    def scroll(self, clicks):
        pyautogui.scroll(clicks)

    def drag(self, x, y, button='left'):
        pyautogui.dragTo(x, y, button=button)
