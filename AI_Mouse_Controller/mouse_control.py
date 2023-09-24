import pyautogui
import logging

class MouseController:
    def __init__(self):
        self.screen_width, self.screen_height = pyautogui.size()

    def move_mouse(self, x, y):
        pyautogui.moveTo(x, y)
        logging.info(f'Moving mouse to ({x}, {y})')

    def click(self, button='left'):
        pyautogui.click(button=button)
        logging.info(f'Clicked {button} button')

    def double_click(self):
        pyautogui.doubleClick()
        logging.info('Performed double click')

    def right_click(self):
        pyautogui.click(button='right')
        logging.info('Performed right click')

    def scroll(self, clicks):
        pyautogui.scroll(clicks)
        logging.info(f'Scrolled {clicks} clicks')

    def drag(self, x, y, button='left'):
        pyautogui.dragTo(x, y, button=button)
        logging.info(f'Dragged mouse to ({x}, {y}) with {button} button')
